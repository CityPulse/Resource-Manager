# from __future__ import unicode_literals

# from virtualisation.clock.abstractclock import AbstractClock
import datetime
import glob
import os.path
import sys
import threading
import zipfile

import cherrypy

from messagebus.rabbitmq import RabbitMQ, MessageBusConnectionError
#from virtualisation.aggregation.genericaggregation import GenericAggregator
from virtualisation.annotation.genericannotation import GenericAnnotation
from virtualisation.annotation.staticannotation import StaticAnnotator
from virtualisation.clock.realclock import RealClock
from virtualisation.clock.replayclock import ReplayClock
from virtualisation.events.eventdescription import EventDescription
from virtualisation.events.genericeventwrapper import GenericEventWrapper
from virtualisation.misc.jsonobject import JSONObject as JOb
from virtualisation.misc.log import Log as L
from virtualisation.misc.threads import QueueThread
from virtualisation.resourcemanagement.api import Api
from virtualisation.resourcemanagement.ui import Ui
from virtualisation.triplestore.threadedtriplestoreadapter import ThreadedTriplestoreAdapter
from virtualisation.triplestore.triplestorefactory import TripleStoreFactory
import virtualisation.wrapper.wrapperoutputreceiver
from virtualisation.resourcemanagement.sql import SQL
from Quality.Average.averageStreamQuality import AverageStreamQuality
from virtualisation.misc.utils import dictdeepcopy
from virtualisation.misc.stat_api import Stat_Api

__author__ = 'Marten Fischer (m.fischer@hs-osnabrueck.de)'

class ResourceManagement(virtualisation.wrapper.wrapperoutputreceiver.AbstractReceiver):
    deployfoldername = os.path.join(os.path.dirname(__file__), "..", "autodeploy")
    eventdescriptionfoldername = os.path.join(os.path.dirname(__file__), "..", "eventdescriptions")
    args = None
    config = None

    def __init__(self, args):
        L(args.log)
        self.config = JOb(file(os.path.join(os.path.dirname(__file__), "..", "config.json"), "rb"))
        self.wrappers = []
        ResourceManagement.args = args
        ResourceManagement.config = self.config
        self.clock = None
        self.annotator = GenericAnnotation()
        self.stoppedClock = False

        # init triplestore
        if args.triplestore:
            ThreadedTriplestoreAdapter.triplestore = TripleStoreFactory.getTripleStore(self.config.triplestore.driver, self.config.triplestore)
            # dump the graph with the static annotations
            StaticAnnotator.dumpGraph()

        if args.aggregate:
            # self.aggregator = AggregatorFactory.make(self.config.aggregationmethod, self.config.aggregation_configuration)
            # self.aggregator = AggregatorFactory.make()

            #TODO
            #self.aggregator = GenericAggregator()
            self.aggregationQueue = QueueThread(handler=self.aggregateHandler)
        self.receiverQueue = QueueThread(handler=self.receiveHandler)

        # establish connection to the message bus
        if args.messagebus:
            self.messageBusQueue = QueueThread(handler=self.sendMessageHandler)
            try:

                # prepare RabbitMQ configuration
                rmq_host = str(self.config.rabbitmq.host)
                rmq_port = self.config.rabbitmq.port
                rmq_username = self.config.rabbitmq.username if "username" in self.config.rabbitmq else None
                rmq_password = self.config.rabbitmq.username if "password" in self.config.rabbitmq else None
                if rmq_username:
                    if rmq_password:
                        RabbitMQ.establishConnection(rmq_host, rmq_port, rmq_username, rmq_password)
                    else:
                        RabbitMQ.establishConnection(rmq_host, rmq_port, rmq_username)
                else:
                    RabbitMQ.establishConnection(rmq_host, rmq_port)

                ##self.rabbitmqconnection, self.messageBusQueue.rabbitmqchannel = \
                #RabbitMQ.establishConnection(str(self.config.rabbitmq.host), self.config.rabbitmq.port)
                #self.registerExchanges()

                self.messageBusQueue.start()
            except MessageBusConnectionError:
                self.args.messagebus = False
                args.messagebus = False
                L.w("Could not connect to MessageBus server. Disabling MessageBus feature.")
        else:
            self.messageBusQueue = None

        if args.eventannotation:
            self.eventWrapper = GenericEventWrapper(self.messageBusQueue)
        else:
            self.eventWrapper = None

        if args.gdi:
            from CityPulseGdi.eu.citypulse.uaso.gdi.CityPulseGDInterface import CityPulseGDInterface
            self.gdiInterface = CityPulseGDInterface(self.config.gdi_db)
            #
            self.gdiInterface.removeAllSensorStreams()
        else:
            self.gdiInterface = None
            
        self.averageStreamQuality = None

        if args.sql:
            self.sql = SQL(self.config.gdi_db, self)
        else:
            self.sql = None

        self.startInterface()
        self.autodeploy()

    def _startQueues(self):
        if not self.receiverQueue.is_alive():
            self.receiverQueue.start()
        # since we need to send messages when a new wrapper is added, the messageBusQueue needs to be started in __init__
        # if self.args.messagebus:
        #     self.messageBusQueue.start()
        if ResourceManagement.args.aggregate:
            if not self.aggregationQueue.is_alive():
                self.aggregationQueue.start()
        if self.eventWrapper:
            if not self.eventWrapper.isStarted():
                self.eventWrapper.start()

    def __all_sensordescriptions(self):
        sds = []
        for w in self.wrappers:
            if not isinstance(w.getSensorDescription(), list):
                sds += [w.getSensorDescription()]
            else:
                sds += w.getSensorDescription()
        return sds

    def autodeploy(self):
        deployFolder = os.path.join(ResourceManagement.deployfoldername, "*.zip")
        files = glob.glob(deployFolder)
        for f in files:
            self.deploy(f)

    def deploy(self, f, autostart=False):
        """

        :param f:
        :param autostart:
        :return: a tuple with 3 elements. 1. status as string, 2. error message as string, 3. list of uuids of added wrapper
        """
        L.i("Deploying", f)
        sensordescriptions = []
        try:
            zFile = zipfile.ZipFile(f)
            if "deploy.json" in zFile.namelist():
                deployDescription = JOb(zFile.open("deploy.json", "r"))
                sys.path.insert(0, f)
                if deployDescription.isList():
                    for dd in deployDescription:
                        module = __import__(dd.module)
                        wrapper = getattr(module, dd["class"])()
                        self.addWrapper(wrapper)
                        sensordescriptions.append(wrapper.getSensorDescription())
                        if autostart:
                            self.startWrapper(wrapper)
                else:
                    module = __import__(deployDescription.module)
                    wrapper = getattr(module, deployDescription["class"])()
                    self.addWrapper(wrapper)
                    sensordescriptions.append(wrapper.getSensorDescription())
                    if autostart:
                        self.startWrapper(wrapper)
            return "OK", "", sensordescriptions
        except Exception as e:
            L.w("Deployment of wrapper", f, "failed.", e.message)
            return "Fail", e.message, []

    def registerEvent(self, eventDescriptionFile):
        if self.eventWrapper:
            eventDescription = EventDescription(open(eventDescriptionFile, "rb"))
            if not eventDescription.test():
                return "Fail", "Invalid EventDescription"
            self.eventWrapper.registerEvent(eventDescription)
            return "Ok", ""
        else:
            return "Fail", "Event wrapper disabled"

    def startInterface(self):
        self.ui = Ui(self)
        self.ui.api = Api(self)
        self.ui.stat_api = Stat_Api(self)
        threading.Thread(target=cherrypy.quickstart, args=(self.ui, '/', self.config.interface.raw())).start()

    def stopInterface(self):
        cherrypy.engine.exit()

    def test(self):
        # from wrapper_dev.osna_dummy.osna_dummy_wrapper import OsnaDummyWrapper
        # wrapper = OsnaDummyWrapper()
        # self.addWrapper(wrapper)
        # from wrapper_dev.london_traffic.londontrafficwrapper import LondonTrafficWrapper
        # wrapper = LondonTrafficWrapper()
        # self.addWrapper(wrapper)
        # from wrapper_dev.aarhus_traffic.aarhustrafficwrapper import AarhusTrafficWrapper
        # wrapper = AarhusTrafficWrapper()
        # self.addWrapper(wrapper)
        from wrapper_dev.aarhus_parking.aarhusparkingwrapper import AarhusParkingWrapper
        wrapper = AarhusParkingWrapper()
        self.addWrapper(wrapper)
        # from wrapper_dev.brasov_pollution.brasovpollutionwrapper import BrasovPollutionWrapper
        # wrapper = BrasovPollutionWrapper()
        # self.addWrapper(wrapper)
        # from wrapper_dev.romania_weather.romaniaweather_aw import RomanianWeatherAWWrapper
        # wrapper = RomanianWeatherAWWrapper()
        # self.addWrapper(wrapper)
        # from wrapper_dev.romania_weather.romaniaweather_mr import RomanianWeatherMRWrapper
        # wrapper = RomanianWeatherMRWrapper()
        # self.addWrapper(wrapper)
        # from wrapper_dev.brasov_incidents.brasov_incidents import BrasovIncidentWrapper0, BrasovIncidentWrapper1
        # wrapper = BrasovIncidentWrapper0()
        # self.addWrapper(wrapper)
        # wrapper = BrasovIncidentWrapper1()
        # self.addWrapper(wrapper)
#         from wrapper_dev.aarhus_pollution.aarhuspollutionwrapper import ComposedAarhusPollutionWrapper
#         wrapper = ComposedAarhusPollutionWrapper()
#         self.addWrapper(wrapper)
#         from wrapper_dev.twitter_stream.twitter import AarhusTwitterWrapper
#         wrapper = AarhusTwitterWrapper()
#         self.addWrapper(wrapper)

        if self.args.eventannotation:
            from wrapper_dev.aarhus_traffic.aarhustrafficeventwrapper import AarhusTrafficEventWrapper
            atew = AarhusTrafficEventWrapper()
            self.eventWrapper.registerEvent(atew.getEventDescription())

    def addWrapper(self, wrapper):
        if ResourceManagement.args.cleartriplestore:
            self.deleteGraphs(wrapper)
        sd = wrapper.getSensorDescription()
        try:
            if isinstance(sd, list):
                for _sd in sd:
                    try:
                        _sd.test()
                        if ResourceManagement.args.aggregate:
                            self.aggregator.wrapper_added(_sd)
                        if self.gdiInterface:
                            self.gdiInterface.registerSensorStreamFromWKT(_sd.uuid, _sd.sensorID, _sd.sensorType, _sd.location, _sd.location_epsg or 4326)
                        # if self.sql:
                        #     self.sql.create_table(_sd)
                        L.i("added wrapper with ID", _sd.sensorID)
                    except Exception as ex:
                        L.e("Error deploying wrapper:", ex)
            else:
                try:
                    sd.test()
                    if ResourceManagement.args.aggregate:
                        self.aggregator.wrapper_added(sd)
                    if self.gdiInterface:
                            self.gdiInterface.registerSensorStreamFromWKT(sd.uuid, sd.sensorID, sd.sensorType, sd.location, sd.location_epsg or 4326)
                    # if self.sql:
                    #     self.sql.create_table(sd)
                    L.i("added wrapper with ID", sd.sensorID)
                except Exception as ex:
                    L.e("Error deploying wrapper:", ex)

            if ResourceManagement.args.triplestore or ResourceManagement.args.messagebus:
                # StaticAnnotator.staticAnnotationSensor(wrapper, self.config, self.messageBusQueue, self.rabbitmqchannel)
                StaticAnnotator.threadedStaticAnnotationSensor(wrapper, self.config, self.messageBusQueue, self.ui.api)
            if ResourceManagement.args.messagebus:
                wrapper.setMessageBusQueue(self.messageBusQueue)
            self.wrappers.append(wrapper)
        except Exception as ex:
            L.e(self.__class__.__name__, "Error in addWrapper:", ex)

    def removeWrapper(self, uuid):
        """
        Removes a wrapper identified by its UUID
        :param uuid:
        :return: True if successful, otherwise False
        """
        for i in range(0, len(self.wrappers)):
            sd = self.wrappers[i].getSensorDescription()
            if isinstance(sd, list):
                for j in range(0, len(sd)):
                    if str(sd[j].uuid) == uuid:
                        self.wrappers[i].stop(j)
                        if self.args.gdi:
                            self.gdiInterface.removeSensorStream(uuid)
                        return True
            else:
                if str(sd.uuid) == uuid:
                    self.wrappers[i].stop()
                    self.wrappers[i:i+1] = []
                    self.gdiInterface.removeSensorStream(uuid)
                    return True
        return False

    def getSensorDescriptionByUUID(self, uuid):
        for sd in self.__all_sensordescriptions():
            if str(sd.uuid) == uuid:
                return sd
        return None

    def getEventDescriptionByUUID(self, uuid):
        if self.eventWrapper:
            return self.eventWrapper.getEventDescriptionByUUID(uuid)

    def getWrapperByUUID(self, uuid):
        from virtualisation.wrapper.abstractwrapper import AbstractComposedWrapper, AbstractWrapper
        for w in self.wrappers:
            if isinstance(w, AbstractWrapper):
                if str(w.getSensorDescription().uuid) == uuid:
                    return w
            elif isinstance(w, AbstractComposedWrapper):
                for ww in w.wrappers:
                    if str(ww.getSensorDescription().uuid) == uuid:
                        return ww
        return None
    
    def getUUIDsForCategory(self, category):
        from virtualisation.wrapper.abstractwrapper import AbstractComposedWrapper, AbstractWrapper
        uuidList = []
        for w in self.wrappers:
            if isinstance(w, AbstractWrapper):
                if str(w.getSensorDescription().sensorType) == category:
                    uuidList.append(w.getSensorDescription().uuid)
            elif isinstance(w, AbstractComposedWrapper):
                for ww in w.wrappers:
                    if str(ww.getSensorDescription().sensorType) == category:
                        uuidList.append(ww.getSensorDescription().uuid)
        return uuidList

    def getEventWrapperDescriptions(self):
        if not self.eventWrapper:
            return None

        return map(lambda (k, v): v, self.eventWrapper.eventDescriptions.iteritems())

    def deleteGraphs(self, wrapper):
        graphNames = wrapper.getGraphName()
        if type(graphNames) is str: #abstract wrapper returns one graph name
            ThreadedTriplestoreAdapter.getOrMake(graphNames).deleteGraph(graphNames)
        else:
            for graphName in graphNames:    #composed abstract wrapper returns set with graph names
                ThreadedTriplestoreAdapter.getOrMake(graphName).deleteGraph(graphName)

    def startReplay(self):
        #cherrypy.tree.mount(dowser.Root(), '/dowser')
        self._startQueues()
        method = self.replayEnd
        args = None

        start_time = datetime.datetime.now()
        
        #if continuelive enabled set "start" as method to set the system to live mode if historic replay is finished
        if ResourceManagement.args.continuelive:
            method = self.start
            args = True
            
        if ResourceManagement.args.speed:
            self.clock = ReplayClock(ResourceManagement.args.speed, endCallback=method, endCallbackArgs=args)
        else:
            self.clock = ReplayClock(endCallback=method)

        if ResourceManagement.args.end and ResourceManagement.args.start:
            try:
                startDate = datetime.datetime.strptime(ResourceManagement.args.start, ReplayClock.parserformat)
                endDate = datetime.datetime.strptime(ResourceManagement.args.end, ReplayClock.parserformat)
                # for w in self.wrappers:
                #     w.setTimeframe(startDate, endDate)
                if startDate > endDate:
                    L.w("start date after end date. Changing both")
                    tmp = endDate
                    endDate = startDate
                    startDate = tmp
                self.clock.setTimeframe(startDate, endDate)
            except Exception as e:
                L.e("Problem parsing start- or end date:", e)
                raise e

        else:
            raise Exception("start- and enddate required for replay mode")

        if ResourceManagement.args.pt:
            from virtualisation.resourcemanagement.performancetestreceiver import PerformanceMeterMinutes
            performancetest = PerformanceMeterMinutes() # PerformanceMeterSeconds()

        for w in self.wrappers:
            w.setReplayMode(True)
            w.setClock(self.clock)
            w.setTimeframe(startDate, endDate)
            w.addReceiver(self)
            if ResourceManagement.args.pt:
                w.addReceiver(performancetest)
            w.start()
            w.runReplay()
            
        if not self.args.noQuality:
            if not self.averageStreamQuality:
                self.averageStreamQuality = AverageStreamQuality(self, self.clock)
            else:
                self.averageStreamQuality.setClock(self.clock)
        self.clock.runAsync()
        self.startMonitor()

        if not ResourceManagement.args.continuelive:
            raw_input("press Enter to end.\n")
            self.clock.stop()
            L.i("Runtime", datetime.datetime.now() - start_time)

    def start(self, restart=False):
        self._startQueues()
        if self.clock:
            self.clock.stop()
        self.clock = RealClock(self.end)

        if ResourceManagement.args.pt:
            from virtualisation.resourcemanagement.performancetestreceiver import PerformanceMeterMinutes
            performancetest = PerformanceMeterMinutes()

        for w in self.wrappers:
            self.startWrapper(w, restart)
            if ResourceManagement.args.pt:
                w.addReceiver(performancetest)
        L.i(datetime.datetime.now())
        
        if not self.args.noQuality:
            if not self.averageStreamQuality:
                self.averageStreamQuality = AverageStreamQuality(self, self.clock)
            else:
                self.averageStreamQuality.setClock(self.clock)
        
        self.clock.runAsync()

        raw_input("press Enter to end.\n")
        self.clock.stop()

    def startWrapper(self, w, restart=False):
        w.setReplayMode(False)
        w.setClock(self.clock)
        if not restart:
            w.addReceiver(self)
        w.start()
        w.run()
        w.update()

    def replayEnd(self):
        if self.monitorTimer:
            self.monitorTimer.cancel()
            self.monitorTimer = None
        self.end()

    def end(self):
        for w in self.wrappers:
            w.stop()
        if ResourceManagement.args.messagebus:
            self.messageBusQueue.stop()
        if ResourceManagement.args.aggregate:
            self.aggregationQueue.stop()
        if self.eventWrapper:
            self.eventWrapper.stop()
        self.receiverQueue.stop()
        if ResourceManagement.args.triplestore:
            ThreadedTriplestoreAdapter.stop()
        self.stopInterface()
        L.i("REPLAY ENDED")

    # def registerExchanges(self):
    #     try:
    #         for ex in RabbitMQ.exchanges:
    #             RabbitMQ.declareExchange(ex, _type="topic")
    #     except Exception as e:
    #         L.e('Exchange could not be declare: %s' % e.message)

    def sendMessageHandler(self, item):
        message, exchange, key = item
        L.d2(message)
        RabbitMQ.sendMessage(message, exchange, key)
        del message

    def aggregateHandler(self, item):
        #TODO
        # data, sensordescription = item
        # aggs = self.aggregator.aggregate(data, sensordescription)
        # if ResourceManagement.args.messagebus and aggs:
        #     for agg in aggs:
        #         annotated_agg = self.annotator.annotateAggregation(agg, sensordescription)
        #         msg = annotated_agg.serialize(format='n3')
        #         self.messageBusQueue.add((msg, RabbitMQ.exchange_aggregated_data, sensordescription.messagebus.routingKey))
        #     del aggs
        pass

    def receive(self, parsedData, sensordescription, clock, quality):
        # L.i("Received data from", sensordescription.fullSensorID)
        if len(parsedData.fields) != 0:
            self.receiverQueue.add((parsedData, sensordescription, clock, quality))
            
    def monitor(self):
        #change speed level in replay mode to avoid high memory consumption
        # L.e("Monitor, Queue Size:", self.receiverQueue.getQueueSize())
        if self.receiverQueue.getQueueSize() > 1000:
            if not self.stoppedClock:
                self.clock.pause()
                self.stoppedClock = True
                # L.e("Monitor stop clock, Queue Size:", self.receiverQueue.getQueueSize())
        elif self.receiverQueue.getQueueSize() < 500:
            if self.stoppedClock:
                self.clock.continue_running()
                self.stoppedClock = False
                # L.e("Monitor continue clock, Queue Size:", self.receiverQueue.getQueueSize())
        if self.monitorTimer:
            self.startMonitor()
            
    def startMonitor(self):
        self.monitorTimer = threading.Timer(10, self.monitor)
        self.monitorTimer.start()

    def receiveHandler(self, item):
        parsedData, sensordescription, clock, quality = item
        L.d2(parsedData)
        # print parsedData
        if self.sql:
            self.sql.insert_observation(sensordescription, parsedData, dictdeepcopy(quality))

        if ResourceManagement.args.messagebus or ResourceManagement.args.triplestore:
            # if len(parsedData.fields)>0:
            g = self.annotator.annotateObservation(parsedData, sensordescription, clock, quality)

        del quality
        if ResourceManagement.args.messagebus and not sensordescription.no_publish_messagebus and "fields" in parsedData and len(parsedData.fields) > 0:
            message = g.serialize(format='n3')
            # print message
            key = sensordescription.messagebus.routingKey
            # self.messageBusQueue.add((parsedData.dumps(), self.rabbitmqchannel, RabbitMQ.exchange_data, key))
            self.messageBusQueue.add((message, RabbitMQ.exchange_annotated_data, key))
            if self.ui.api:
                self.ui.api.update_observation_cache(str(sensordescription.uuid), message)
        if ResourceManagement.args.triplestore:
            # TODO: The following line is commented out, since the Virtuoso makes so much trouble
            ThreadedTriplestoreAdapter.getOrMake(sensordescription.graphName).addGraph(g)
            pass
        if ResourceManagement.args.messagebus or ResourceManagement.args.triplestore:
            del g
        if ResourceManagement.args.aggregate:
            self.aggregationQueue.add((parsedData, sensordescription))
        else:
            del parsedData
