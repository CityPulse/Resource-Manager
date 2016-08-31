import abc
from datetime import datetime
import os.path
import threading
import zipfile

from Quality.AtomicComputation.cp_qoi_system import CpQoiSystem
from virtualisation.annotation.observationidgenerator import ObservationIDGenerator
from virtualisation.misc.jsonobject import JSONObject
from virtualisation.misc.log import Log as L
from virtualisation.misc.stats import Stats
from virtualisation.misc.utils import cast
from virtualisation.resourcemanagement.resourcemanagement import ResourceManagement
from virtualisation.sensordescription import SensorDescription
from virtualisation.wrapper.connection.splitterconnection import SplitterConnection
from virtualisation.wrapper.faultrecovery.FaultRecovery import FaultRecovery
from virtualisation.wrapper.faultrecovery.dummyfr import FaultRecovery as FR


__author__ = "Marten Fischer (m.fischer@hs-osnabrueck.de)"


class AbstractWrapper(object):

    __metaclass__ = abc.ABCMeta

    FAULT_RECOVERY_SUPPORTED_DATATYPES = ["int", "float", "long"]
    FAULT_RECOVERY_PERFORMANCE_TEST = False

    def __init__(self):
        self.event = threading.Event()
        self.abort = threading.Event()

        # have to be set by the wrapper developer at some point
        self.connection = None
        self.parser = None
        self.historyparser = None
        self.historyreader = None

        # may be set by the wrapper developer
        self.sensordescription = None

        # set by the resourcemanagement
        self.replaymode = False
        self.faultRecoveryActive = True # Fault Recovery must be possible to be turned on/off
        self.clock = None
        self.runthread = None
        self.receiver = []
        if not ResourceManagement.args.noQuality:
            self.qoiSystem = CpQoiSystem()
        else:
            self.qoiSystem = None
        self.faultRecoveries = {}

        # set by other components
        self.parent = None # in case this is a child of a composed wrapper

    @classmethod
    def getFileObject(cls, currentfile, filename, mode="r"):
        parent = os.path.dirname(currentfile)
        if parent.endswith(".zip"):
            zFile = zipfile.ZipFile(parent)
            return zFile.open(filename, mode)
        else:
            return file(os.path.join(parent, filename), mode)

    @abc.abstractmethod
    def getSensorDescription(self):
        """
        :return: a sensor descriptions
        """
        if not self.sensordescription:
            try:
                self.sensordescription = SensorDescription(AbstractWrapper.getFileObject(__file__, "sensordescription.json", "rU"))
            except:
                self.sensordescription = None
        return self.sensordescription

    def start(self):
        """
        initialises the fault recoveries for numeric fields
        :return:
        """
        self.frfiles = {}
        import csv
        for f in self.getSensorDescription().fields:
            field = self.getSensorDescription().field[f]
            if field.dataType in AbstractWrapper.FAULT_RECOVERY_SUPPORTED_DATATYPES:
                if not ResourceManagement.args.nofr:
                    self.faultRecoveries[f] = FaultRecovery()
                    if AbstractWrapper.FAULT_RECOVERY_PERFORMANCE_TEST:
                        myfile = open("%s-%s.csv" % (str(self.getSensorDescription().uuid), f), "wb")
                        w = csv.writer(myfile)
                        w.writerow(["timestamp", "o", "e", "diff"])
                        self.frfiles[f] = (w, myfile)

                else:
                    self.faultRecoveries[f] = FR()
        self.stats = Stats(self.getSensorDescription().uuid)

    def runReplay(self):
        if not self.historyparser:
            self.historyparser = self.parser
        self.run()

    def run(self):
        # self.clock.addJob(self.getSensorDescription().updateInterval, self.update, True)
        self.clock.addNotification(self.getSensorDescription().updateInterval, self.event, True)
        self.runthread = threading.Thread(name="w_" + str(self.getSensorDescription().sensorID), target=self._run)
        self.runthread.start()

    def _run(self):
        self.abort.clear()
        if not self.clock:
            raise Exception("no clock set?")

        while not self.abort.is_set():
            if self.event.wait(1.0):
                if not self.abort.is_set():
                    try:
                        self.update()
                    except Exception as e:
                        L.e("in _run", e.message)
                    finally:
                        self.clock.continue_running()
                self.event.clear()

    def stop(self):
        self.abort.set()
        self.event.set()
        if self.runthread:
            self.runthread.join()
            self.runthread = None

    def setReplayMode(self, mode):
        self.replaymode = mode

    def setTimeframe(self, startdate, enddate):
        if self.historyreader:
            self.historyreader.setTimeframe(startdate, enddate)

    def setClock(self, clock):
        self.clock = clock

    def addReceiver(self, receiver):
        self.receiver.append(receiver)

    def update(self):
        from virtualisation.resourcemanagement.resourcemanagement import ResourceManagement
        # print "time", self.clock.now()
        latStart = datetime.now()
        L.d("processing:", self.getSensorDescription().sensorID)
        # L.d(self.clock.now())
        if self.replaymode:
            self.stats.startMeasurement("Update_replay")
#             self.clock.pause()
            if self.historyreader:
                L.d2("abstractwrapper get data")
                self.stats.startMeasurement("Update_replay.Historyreader")
                data_raw = self.historyreader.tick(self.clock)
                self.stats.stopMeasurement("Update_replay.Historyreader")
                L.d2("abstractwrapper received data:", str(data_raw))
                if data_raw:
                    data_list = [data_raw] if not self.historyreader.multiple_observations else data_raw
                    for data in data_list:
                        try:
                            L.d2("abstractwrapper parse data")
                            #print "data to parse", data
                            self.stats.startMeasurement("Update_replay.Historyparser")
                            parsed = self.historyparser.parse(data, self.clock)
                            self.stats.stopMeasurement("Update_replay.Historyparser")
                            L.d2("abstractwrapper parsed data:", str(parsed))
                            del data
                            if parsed:
                                self.stats.startMeasurement("Update_replay.Preparation")
                                ObservationIDGenerator.addObservationIDToFields(parsed)
                                parsed.producedInReplayMode = True
                                parsed.recovered = False
                                parsed.latency = (datetime.now() - latStart).total_seconds()
                                self.stats.stopMeasurement("Update_replay.Preparation")

                                #QoI Start
                                quality = None
                                if self.qoiSystem:
                                    L.d2("abstractwrapper get quality")
                                    self.stats.startMeasurement("Update_replay.Quality")
                                    quality = self.qoiSystem.addData(self.getSensorDescription(), parsed, self.clock)
                                    self.stats.stopMeasurement("Update_replay.Quality")
                                    L.d2("abstractwrapper quality:", quality)
                                if self.faultRecoveryActive:
                                    L.d2("abstractwrapper update fault recovery")
                                    self.stats.startMeasurement("Update_replay.FaultRecoveryUpdate")
                                    self.updateFaultRecoveries(parsed, quality)
                                    self.stats.stopMeasurement("Update_replay.FaultRecoveryUpdate")
                                    L.d2("abstractwrapper fault recovery updated")

                                self.stats.startMeasurement("Update_replay.Receiver")
                                for r in self.receiver:
                                    L.d2("abstractwrapper start receiver", r)
                                    r.receive(parsed, self.getSensorDescription(), self.clock, quality)
                                    L.d2("abstractwrapper receiver", r, "finished")
                                self.stats.stopMeasurement("Update_replay.Receiver")
                        except Exception as e:
                            L.e("Error while updating sensor", self.getSensorDescription().fullSensorID, e)
                        finally:
                            if ResourceManagement.args.gentle:
                                self.clock.sleep()
                else:
                    L.d("there is no data, ask fault recovery1")
                    # L.i(self.getSensorDescription().sensorID)
                    # L.i(self.clock.now())
                    try:
                        self.stats.startMeasurement("Update_replay.Recovery")
                        data = JSONObject()
                        data.latency = 0
                        data.producedInReplayMode = True
                        data.recovered = True

                        data.fields = []
                        for n in self.getSensorDescription().fields:
                            if n in self.faultRecoveries and self.faultRecoveries[n].isReady():
                                data.fields.append(n)
                                data[n] = JSONObject()
                                # at this point the dataType is in FAULT_RECOVERY_SUPPORTED_DATATYPES and we can safely use cast
                                data[n].value = self.faultRecoveryCast(self.faultRecoveries[n].getEstimation(), self.getSensorDescription().field[n].dataType)
                                data[n].propertyName = self.getSensorDescription().field[n].propertyName
                                data[n].propertyURI = self.getSensorDescription().field[n].propertyURI
                                if "unit" in self.getSensorDescription().field[n]:
                                    data[n].unit = self.getSensorDescription().field[n].unit
                                data[n].sensorID = self.getSensorDescription().fullSensorID
                                data[n].observationSamplingTime = self.clock.timeAsString()
                                data[n].observationResultTime = data[n].observationSamplingTime
                        self.stats.stopMeasurement("Update_replay.Recovery")

                        self.stats.startMeasurement("Update_replay.ObservationIDGenerator")
                        ObservationIDGenerator.addObservationIDToFields(data)
                        self.stats.stopMeasurement("Update_replay.ObservationIDGenerator")
                        
                        quality = None
                        if self.qoiSystem:
                            self.stats.startMeasurement("Update_replay.Quality")
                            quality = self.qoiSystem.addData(self.getSensorDescription(), data, self.clock)
                            self.stats.stopMeasurement("Update_replay.Quality")
                            
                        self.stats.startMeasurement("Update_replay.Receiver")
                        for r in self.receiver:
                            r.receive(data, self.getSensorDescription(), self.clock, quality)
                        self.stats.stopMeasurement("Update_replay.Receiver")
                    except Exception as e:
                        L.e("Error while updating sensor", self.getSensorDescription().fullSensorID, e)
                    finally:
                        pass
                        # if ResourceManagement.args.gentle:
                        #     self.clock.sleep()
            else:
                pass  # no history reader - nothing to do
            self.stats.stopMeasurement("Update_replay")
        else:  # no replay mode
            self.stats.startMeasurement("Update_live")
            if self.connection:
                try:
                    self.stats.startMeasurement("Update_live.Connection")
                    data_raw = self.connection.next()
                    self.stats.stopMeasurement("Update_live.Connection")
                    if data_raw:
                        data_list = [data_raw] if not self.connection.multiple_observations else data_raw
                        for data in data_list:
                            self.stats.startMeasurement("Update_live.Parser")
                            parsed = self.parser.parse(data, self.clock)
                            self.stats.stopMeasurement("Update_live.Parser")
                            if parsed:
                                self.stats.startMeasurement("Update_live.Preparation")
                                ObservationIDGenerator.addObservationIDToFields(parsed)
                                parsed.producedInReplayMode = False
                                parsed.recovered = False
                                parsed.latency = (datetime.now() - latStart).total_seconds()
                                self.stats.stopMeasurement("Update_live.Preparation")

                                #QoI Start
                                quality = None
                                if self.qoiSystem:
                                    #TODO update the timestamp
                                    self.stats.startMeasurement("Update_live.Quality")
                                    quality = self.qoiSystem.addData(self.getSensorDescription(), parsed, self.clock)
                                    self.stats.stopMeasurement("Update_live.Quality")
                                if self.faultRecoveryActive:
                                    L.d2("abstractwrapper update fault recovery")
                                    self.stats.startMeasurement("Update_live.FaultRecoveryUpdate")
                                    self.updateFaultRecoveries(parsed, quality)
                                    self.stats.stopMeasurement("Update_live.FaultRecoveryUpdate")
                                    L.d2("abstractwrapper fault recovery updated")

                                self.stats.startMeasurement("Update_live.Receiver")
                                for r in self.receiver:
                                    r.receive(parsed, self.getSensorDescription(), self.clock, quality)
                                self.stats.stopMeasurement("Update_live.Receiver")
                    else:
                        # fault recovery
                        L.i("there is no data, ask fault recovery2")
                        try:
                            self.stats.startMeasurement("Update_live.Recovery")
                            data = JSONObject()
                            data.latency = 0
                            data.recovered = True
                            data.fields = []
                            for n in self.getSensorDescription().fields:
                                if n in self.faultRecoveries and self.faultRecoveries[n].isReady():
                                    data.fields.append(n)
                                    data[n] = JSONObject()
                                    data[n].value = self.faultRecoveryCast(self.faultRecoveries[n].getEstimation(), self.getSensorDescription().field[n].dataType)
                                    data[n].propertyName = self.getSensorDescription().field[n].propertyName
                                    data[n].propertyURI = self.getSensorDescription().field[n].propertyURI
                                    if "unit" in self.getSensorDescription().field[n]:
                                        data[n].unit = self.getSensorDescription().field[n].unit
                                    data[n].sensorID = self.getSensorDescription().fullSensorID
                                    data[n].observationSamplingTime = self.clock.timeAsString()
                                    data[n].observationResultTime = data[n].observationSamplingTime
                            self.stats.stopMeasurement("Update_live.Recovery")

                            ObservationIDGenerator.addObservationIDToFields(data)
                            quality = None
                            if self.qoiSystem:
                                self.stats.startMeasurement("Update_live.Quality")
                                quality = self.qoiSystem.addData(self.getSensorDescription(), data, self.clock)
                                self.stats.stopMeasurement("Update_live.Quality")
                            
                            self.stats.startMeasurement("Update_live.Receiver")
                            for r in self.receiver:
                                r.receive(data, self.getSensorDescription(), self.clock, quality)
                            self.stats.stopMeasurement("Update_live.Receiver")
                        except Exception as e:
                            L.e("Error while updating sensor (fault recovery)", self.getSensorDescription().fullSensorID, str(e))
                        finally:
                            pass
                            # if ResourceManagement.args.gentle:
                            #     self.clock.sleep()
                except Exception as e:
                    L.e("Error while updating sensor (not fault recovery)", self.getSensorDescription().fullSensorID, str(e))
            else:
                pass # no live mode supported
            self.stats.stopMeasurement("Update_live")

    def updateAsync(self):
        threading.Thread(target=self.update).start()
        
    def setMessageBusQueue(self, messageBusQueue):
        if self.qoiSystem:
            self.qoiSystem.setMessageBusQueue(messageBusQueue)

    def activateFaultRecovery(self):
        self.faultRecoveryActive = True

    def deactivateFaultRecovery(self):
        self.faultRecoveryActive = False

    def updateFaultRecoveries(self, data, quality):
        if not quality:
            return
        for fieldname in self.faultRecoveries:
            if self.replaymode:
                self.stats.startMeasurement("Update_replay.FaultRecoveryUpdate." + fieldname)
            else:
                self.stats.startMeasurement("Update_live.FaultRecoveryUpdate." + fieldname)
            if fieldname in data:
                if fieldname not in quality["Completeness"].missingFields and fieldname not in quality["Correctness"].wrongFields:
                    if AbstractWrapper.FAULT_RECOVERY_PERFORMANCE_TEST:
                        o = data[fieldname].value
                        e = self.faultRecoveries[fieldname].getEstimation()
                        e = e if e else 0
                        #r = 1 if o == e else float(o) / (e if e != 0 else 1)
                        w, f = self.frfiles[fieldname]
                        w.writerow([self.clock.now(), o, e, o - e])
                        f.flush()

                    self.faultRecoveries[fieldname].addValidMeasurement(data[fieldname].value)
                else:
#                     print "CALL FAULT RECOVERY"
                    self.faultRecoveries[fieldname].reportInvalidMeasurement()
                    data[fieldname].value = self.faultRecoveries[fieldname].getEstimation() or data[fieldname].value
#                     print "RECOVERED VALUE:", data[fieldname].value
                    data[fieldname].recoverd = True
            
            if self.replaymode:
                self.stats.stopMeasurement("Update_replay.FaultRecoveryUpdate." + fieldname)
            else:
                self.stats.stopMeasurement("Update_live.FaultRecoveryUpdate." + fieldname)

    def faultRecoveryCast(self, value, dataType):
        if dataType == "int" or dataType == "long":
            return cast(round(value, 0), dataType)
        else:
            return cast(value, dataType)

    def getGraphName(self):
        return self.getSensorDescription().graphName

class AbstractComposedWrapper(object):
    def __init__(self):
        self.wrappers = []
        self.splitter = None
        self.connection = None
        self.clock = None
        self.event = threading.Event()
        self.abort = threading.Event()
        self.runthread = None

    @classmethod
    def getFileObject(cls,  currentfile, filename, mode="r"):
        return AbstractWrapper.getFileObject(currentfile, filename, mode)

    def getSensorDescription(self):
        """
        :return: a list of sensor descriptions
        """
        return map(lambda x: x.getSensorDescription(), self.wrappers)

    def addWrapper(self, w):
        """
        add a wrapper to the internal wrapper list
        :param w: the wrapper to add
        :return:
        """
        if not isinstance(w, AbstractWrapper):
            raise Exception(error="trying to add a wrapper which is not an instance of AbstractWrapper")
        self.wrappers.append(w)

    def setReplayMode(self, mode):
        self.__forEachWrapper("setReplayMode", mode)

    def setTimeframe(self, startdate, enddate):
        self.__forEachWrapper("setTimeframe", (startdate, enddate))

    def startReplay(self):
        self.__forEachWrapper("startReplay")

    def setClock(self, clock):
        self.clock = clock
        self.__forEachWrapper("setClock", clock)
    
    def setMessageBusQueue(self, messageBusQueue):
        self.__forEachWrapper("setMessageBusQueue", messageBusQueue)

    def activateFaultRecovery(self):
        self.__forEachWrapper("activateFaultRecovery")

    def deactivateFaultRecovery(self):
        self.__forEachWrapper("deactivateFaultRecovery")

    def start(self):
        # set a SplitterConnection on all wrappers
        self.setDefaultConnection()
        self.__forEachWrapper("start")

    def run(self):
        self.clock.addNotification(self.getSensorDescription()[0].updateInterval, self.event, True)
        self.runthread = threading.Thread(target=self._run)
        self.runthread.start()
        # self.__forEachWrapper("run")

    def _run(self):
        self.abort.clear()
        if not self.clock:
            raise Exception("no clock set?")

        while not self.abort.is_set():
            if self.event.wait(0.1):
                if not self.abort.is_set():
                    self.update()
            self.event.clear()


    def runReplay(self):
        # self.__forEachWrapper("run")
        self.clock.addNotification(self.getSensorDescription()[0].updateInterval, self.event, True)
        self.runthread = threading.Thread(target=self._runReplay)
        self.runthread.start()

    def _runReplay(self):
        self.abort.clear()
        if not self.clock:
            raise Exception("no clock set?")

        while not self.abort.is_set():
            if self.event.wait(1.0):
                if not self.abort.is_set():
                    try:
                        self.__forEachWrapper("update")
                    except Exception as e:
                        L.e("in _run", e.message)
                    finally:
                        self.clock.continue_running()
                        pass

                self.event.clear()

    def stop(self, subwrapper=-1):
        if subwrapper >= 0:
            self.wrappers[subwrapper].stop()
            self.wrappers[subwrapper:subwrapper+1] = []
        else:
            self.abort.set()
            self.event.set()
            self.__forEachWrapper("stop")
            if self.runthread:
                self.runthread.join()
                self.runthread = None

    def update(self):
        if self.connection:
            data = self.connection.next()
            if data:
                self.splitter.update(data)
                self.__forEachWrapper("update")
        else:
            self.__forEachWrapper("update")

    def addReceiver(self, receiver):
        self.__forEachWrapper("addReceiver", receiver)

    def setDefaultConnection(self):
        """
        sets a SplitterConnection for all internal wrappers with no connection
        :return:
        """
        connectionlessWrappers = filter(lambda w: not w.connection, self.wrappers)
        for w in connectionlessWrappers:
            sc = SplitterConnection(w, self)
            w.connection = sc

    def __forEachWrapper(self, func, args=None):
        for w in self.wrappers:
            m = getattr(w, func, None)
            if m:
                if isinstance(args, bool) or args:
                    if isinstance(args, tuple) and len(args) == 2:
                        a, b = args
                        m(a, b)
                    else:
                        m(args)
                else:
                    m()
                    
    def getGraphName(self):
        sensorDescriptions = self.getSensorDescription()
        graphNames = set()
        for description in sensorDescriptions:
            graphNames.add(description.graphName)
        return graphNames
    
    