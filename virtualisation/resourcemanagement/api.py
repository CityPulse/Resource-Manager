import cherrypy
import os.path

from virtualisation.misc.jsonobject import JSONObject as JOb
from virtualisation.misc.utils import formatSensorID
from virtualisation.triplestore.threadedtriplestoreadapter import ThreadedTriplestoreAdapter


__author__ = 'Marten Fischer (m.fischer@hs-osnabrueck.de)'

class Api(object):
    def __init__(self, resourcemanagement):
        self.rm = resourcemanagement
        self.observation_cache = {}
        self.static_stream_data_cache = {}

    def update_observation_cache(self, sensor_uuid, observation):
        self.observation_cache[sensor_uuid] = observation

    def set_static_stream_data(self, sensor_uuid, data):
        self.static_stream_data_cache[sensor_uuid] = data

    @cherrypy.expose
    def listwrapper(self):
        r = JOb()
        c = 0
        r.wrappers = []
        for w in self.rm.wrappers:
            sd = w.getSensorDescription()
            if isinstance(sd, list):
                for _sd in sd:
                    r.wrappers.append(JOb())
                    r.wrappers[c].information = _sd.information
                    r.wrappers[c].uuid = _sd.uuid
                    r.wrappers[c].sensorName = _sd.sensorName
                    r.wrappers[c].author = _sd.author
                    r.wrappers[c].sensorID = _sd.sensorID
                    r.wrappers[c].fullSensorID = _sd.fullSensorID
                    r.wrappers[c].source = _sd.source
                    r.wrappers[c].sensorType = _sd.sensorType
                    r.wrappers[c].sourceFormat = _sd.sourceFormat
                    r.wrappers[c].messagebus.routingKey = _sd.messagebus.routingKey
                    c += 1
            else:
                r.wrappers.append(JOb())
                r.wrappers[c].information = sd.information
                r.wrappers[c].uuid = sd.uuid
                r.wrappers[c].sensorName = sd.sensorName
                r.wrappers[c].author = sd.author
                r.wrappers[c].sensorID = sd.sensorID
                r.wrappers[c].fullSensorID = sd.fullSensorID
                r.wrappers[c].source = sd.source
                r.wrappers[c].sensorType = sd.sensorType
                r.wrappers[c].sourceFormat = sd.sourceFormat
                r.wrappers[c].messagebus.routingKey = sd.messagebus.routingKey
                c += 1
        return r.dumps()

    @cherrypy.expose
    def listeventwrapper(self):
        r = JOb()
        r.eventwrapper = []
        eds = self.rm.getEventWrapperDescriptions()
        for ed in eds:
            r.eventwrapper.append(ed)
        return r.dumps()

    @cherrypy.expose
    def listwrapperfull(self):
        r = JOb()
        r.wrappers = []
        for w in self.rm.wrappers:
            sd = w.getSensorDescription()
            if isinstance(sd, list):
                for _sd in sd:
                    r.wrappers.append(_sd)
            else:
                r.wrappers.append(sd)
        return r.dumps()

    @cherrypy.expose
    def get_static_stream_data(self, uuid):
        resp = JOb()
        resp.uuid = uuid
        if uuid in self.static_stream_data_cache:
            resp.status = "Ok"
            resp.message = ""
            resp.data = self.static_stream_data_cache[uuid]
        else:
            resp.status = "Fail"
            resp.message = "No sensor stream with uuid " + uuid + " known."
        return resp.dumps()

    @cherrypy.expose
    def deploy(self, deployunit):
        resp = JOb()
        if deployunit.filename.endswith(".zip"):
            from virtualisation.resourcemanagement.resourcemanagement import ResourceManagement
            trg = os.path.join(ResourceManagement.deployfoldername, deployunit.filename)
            dst = open(trg, "w")
            dst.write(deployunit.file.read())
            dst.close()
            try:
                resp.status, resp.message, resp.sensordescriptions = self.rm.deploy(trg, True)
            except Exception as e:
                resp.status = "Fail"
                resp.message = e.message
        else:
            resp.status = "Fail"
            resp.message = "Wrong file type."
        return resp.dumps()

    @cherrypy.expose
    def register_event(self, eventdescription):
        resp = JOb()
        if eventdescription.filename.endswith(".json"):
            from virtualisation.resourcemanagement.resourcemanagement import ResourceManagement
            trg = os.path.join(ResourceManagement.eventdescriptionfoldername, eventdescription.filename)
            dst = open(trg, "w")
            dst.write(eventdescription.file.read())
            dst.close()
            try:
                resp.status, resp.message = self.rm.registerEvent(trg)
            except Exception as e:
                resp.status = "Fail"
                resp.message = e.message
        else:
            resp.status = "Fail"
            resp.message = "Wrong file type."
        return resp.dumps()

    @cherrypy.expose
    def snapshot(self, uuid, start=None, end=None):
        """
        Get previous observations
        :param uuid: The uuid of the wrapper
        :param start: The start date in the format %Y-%m-%dT%H:%M:%S
        :param end: The end date in the format %Y-%m-%dT%H:%M:%S
        :return: a JSON answer
        """
        resp = JOb()
        resp.uuid = uuid
        try:
            from virtualisation.resourcemanagement.resourcemanagement import ResourceManagement
            if ResourceManagement.args.triplestore:
                sd = self.rm.getSensorDescriptionByUUID(uuid)
                if sd:
                    data = ThreadedTriplestoreAdapter.triplestore.getObservationGraph(sd.graphName, formatSensorID(sd), start, end, False)
                    resp.status = "Ok"
                    resp.message = ""
                    resp.data = data
                else:
                    raise Exception("no stream with given uuid known")
            else:
                raise Exception("Triplestore not enabled in Resource Management")

        except Exception as e:
            resp.status = "Fail"
            resp.message = e.message

        return resp.dumps()

    @cherrypy.expose
    def snapshot_last(self, uuid):
        """
        Get previous observations
        :param uuid: The uuid of the wrapper
        :param start: The start date in the format %Y-%m-%dT%H:%M:%S
        :param end: The end date in the format %Y-%m-%dT%H:%M:%S
        :return: a JSON answer
        """
        resp = JOb()
        resp.uuid = uuid
        if uuid in self.observation_cache:
            resp.status = "Ok"
            resp.message = ""
            resp.data = self.observation_cache[uuid]
        else:
            resp.status = "Fail"
            resp.message = "No observation with the UUID " + uuid + " cached."
        return resp.dumps()

    @cherrypy.expose
    def snapshot_sql(self, uuid, start=None, end=None, format='json', last=False, fields=None):
        if self.rm.sql:
            data = self.rm.sql.get_observations(uuid, start, end, format, last, fields)
            return data
        else:
            return "error"

    @cherrypy.expose
    def uuids_by_servicecategory(self, service_category, start=None, end=None):
        if self.rm.sql:
            data = self.rm.sql.get_observations_service_category(service_category, start, end)
            return data
        else:
            return "error"

    @cherrypy.expose
    def snapshot_quality(self, uuid, start=None, end=None):
        """
        Get previous quality annotations
        :param uuid: The uuid of the wrapper/stream
        :param start: The start date in the format %Y-%m-%dT%H:%M:%S
        :param end: The end date in the format %Y-%m-%dT%H:%M:%S
        :return: a JSON answer
        """
        resp = JOb()
        resp.uuid = uuid
        resp.result = []
        uuid = uuid.split(",")
        
        try:
            from virtualisation.resourcemanagement.resourcemanagement import ResourceManagement
            if ResourceManagement.args.triplestore:
                graphMap = {}
                working_uuids = []
                for _id in uuid:
                    sd = self.rm.getSensorDescriptionByUUID(_id)
                    if sd is not None:
                        if not graphMap.has_key(sd.graphName):
                            graphMap[sd.graphName] = [formatSensorID(sd)]
                        else:
                            graphMap[sd.graphName].append(formatSensorID(sd))
                        working_uuids.append(_id)
                    else:
                        d = JOb()
                        d.message = "Wrong UUID"
                        resp.result.append(JOb({"uuid": _id, "error": d}))    
                resp.status = "Ok"
                
                sortedReturn = {}
                for graph in graphMap:
                    tmpData = ThreadedTriplestoreAdapter.triplestore.getLastQoIData_List(graph, graphMap[graph], start, end)
                    if tmpData is None:
                        raise Exception("Virtuoso Exception or no data for given start/end date")
                    else:
                        if len(tmpData["results"]["bindings"]) == 0:
                            pass
                        else:
                            for key in tmpData["results"]["bindings"]:
                                sensorUUID = key["sensor"]["value"].replace("http://ict-citypulse.eu/SensorID-", "")
                                if sensorUUID in sortedReturn:
                                    sortedReturn[sensorUUID].append(key)
                                else:
                                    sortedReturn[sensorUUID] = []
                                    sortedReturn[sensorUUID].append(key)
                
                for _id in working_uuids:
                    if _id in sortedReturn:
                        data = []
                        for tmp in sortedReturn[_id]:
                            d = JOb()
                            d.time = tmp["resultTimeValue"]["value"]
                            d.data = tmp
                            data.append(d) 
                        data.sort(cmp=lambda x, y: cmp(x.time, y.time))
                        resp.result.append(JOb({"uuid": _id, "dataset": data}))
                    else:
                        d = JOb()
                        d.message = "No data available"
                        resp.result.append(JOb({"uuid": _id, "error": d}))    
                    
                resp.result.sort(cmp=lambda x, y: uuid.index(x.uuid) - uuid.index(y.uuid))    
            else:
                raise Exception("Triplestore not enabled in Resource Management")

        except Exception as e:
            resp.status = "Fail"
            resp.message = e.message

        return resp.dumps()
    
    def strcmp(self, str1,str2):
        if(str1 == str2):
            return 0
        if(str1 > str2):
            return 1
        if(str1 < str2):
            return -1

    @cherrypy.expose
    def data_timeframe(self, uuid):
        """
        Returns the time frame (start and end date) for which data from the stream, identified by the UUID,
        is available.
        :param uuid:
        :return:
        """
        resp = JOb()
        resp.uuid = uuid
        try:
            if ThreadedTriplestoreAdapter.triplestore:
                sd = self.rm.getSensorDescriptionByUUID(uuid)
                if sd:
                    data = ThreadedTriplestoreAdapter.triplestore.getStreamMinMaxDate(sd.graphName, formatSensorID(sd))
                    resp.status = "Ok"
                    resp.message = ""
                    resp.data = data
                else:
                    raise Exception("no stream with given uuid known")
            else:
                resp.status = "Fail"
                resp.message = "Triplestore not activated."
        except Exception as e:
            resp.status = "Fail"
            resp.message = e.message

        return resp.dumps()

    @cherrypy.expose
    def data_timeframe_sql(self, uuid):
        """
        Returns the time frame (start and end date) for which data from the stream, identified by the UUID,
        is available.
        :param uuid:
        :return:
        """
        resp = JOb()
        resp.uuid = uuid
        try:
            if self.rm.sql:
                data = self.rm.sql.data_timeframe(uuid)
                resp.status = "Ok"
                resp.message = ""
                resp.data = data
            else:
                resp.status = "Fail"
                resp.message = "SQL feature not activated."
        except Exception as e:
            resp.status = "Fail"
            resp.message = e.message

        return resp.dumps()

    @cherrypy.expose
    def activate_fault_recovery(self, uuid):
        """
        Enable the fault recovery for a wrapper
        :param uuid: UUID identifying the wrapper
        :return:
        """
        resp = JOb()
        resp.uuid = uuid
        w = self.rm.getWrapperByUUID(uuid)
        if w:
            w.activateFaultRecovery()
            resp.status = "Ok"
            resp.message = ""
        else:
            resp.status = "Fail"
            resp.message = "no stream with given uuid known"
        return resp.dumps()

    @cherrypy.expose
    def deactivate_fault_recovery(self, uuid):
        """
        Disable the fault recovery for a wrapper
        :param uuid: UUID identifying the wrapper
        :return:
        """
        resp = JOb()
        resp.uuid = uuid
        w = self.rm.getWrapperByUUID(uuid)
        if w:
            w.deactivateFaultRecovery()
            resp.status = "Ok"
            resp.message = ""
        else:
            resp.status = "Fail"
            resp.message = "no stream with given uuid known"
        return resp.dumps()

    ## removed since it would allow the get the database password.
    # @cherrypy.expose
    # def get_config(self):
    #     from virtualisation.resourcemanagement.resourcemanagement import ResourceManagement
    #     return ResourceManagement.config.dumps()

    @cherrypy.expose
    def get_description(self, uuid):
        resp = JOb()
        sd = self.rm.getSensorDescriptionByUUID(uuid)
        if sd:
            resp.status = "Ok"
            resp.message = ""
            resp.data = sd
        else:
            ed = self.rm.getEventDescriptionByUUID(uuid)
            if ed:
                resp.status = "Ok"
                resp.message = ""
                resp.data = ed
            else:
                resp.status = "Fail"
                resp.message = "no stream with given uuid known"
        return resp.dumps()

    @cherrypy.expose
    def remove_wrapper(self, uuid):
        if self.rm.removeWrapper(uuid):
            return "OK"
        else:
            return "Fail"

    # @cherrypy.expose
    # def getAllAverageQualities(self):
    #     from virtualisation.wrapper.abstractwrapper import AbstractWrapper, AbstractComposedWrapper
    #     avgQualities = []
    #     wrappers = self.rm.wrappers
    #     for wrapper in wrappers:
    #         if isinstance(wrapper, AbstractWrapper):
    #             if wrapper.qoiSystem.initialised:
    #                 avgQualities.append(wrapper.qoiSystem.reputationSystem.avgQoIManager.getAvgQualities(self.rm.clock.now()))
    #                 avgQualities[-1].uuid = wrapper.getSensorDescription().uuid
    #         elif isinstance(wrapper, AbstractComposedWrapper):
    #             for aWrapper in wrapper.wrappers:
    #                 if aWrapper.qoiSystem.initialised:
    #                     avgQualities.append(aWrapper.qoiSystem.reputationSystem.avgQoIManager.getAvgQualities(self.rm.clock.now()))
    #                     avgQualities[-1].uuid = aWrapper.getSensorDescription().uuid
    #     return JOb(avgQualities).dumps()
    
    # @cherrypy.expose
    # def getAverageQuality(self, uuid):
    #     wrapper = self.rm.getWrapperByUUID(uuid)
    #     message = ""
    #     if wrapper:
    #         if wrapper.qoiSystem.initialised:
    #             qualities = []
    #             qualities.append(wrapper.qoiSystem.reputationSystem.avgQoIManager.getAvgQualities(self.rm.clock.now()))
    #             qualities[-1].uuid = wrapper.getSensorDescription().uuid
    #             return JOb(qualities).dumps()
    #         else:
    #             message = "Quality System not initialised for given uuid"
    #     else:
    #         message = "no stream with given uuid known"
    #     resp = JOb()
    #     resp.uuid = uuid
    #     resp.status = "Fail"
    #     resp.message = message
    #     return resp.dumps()
    #
    # @cherrypy.expose
    # def getLastQuality(self, uuid):
    #     wrapper = self.rm.getWrapperByUUID(uuid)
    #     message = ""
    #     if wrapper:
    #         if wrapper.qoiSystem.initialised:
    #             avgQualities = []
    #             avgQualities.append(wrapper.qoiSystem.getLastQoI())
    #             avgQualities[-1].uuid = wrapper.getSensorDescription().uuid
    #             return JOb(avgQualities).dumps()
    #         else:
    #             message = "Quality System not initialised for given uuid"
    #     else:
    #         message = "no stream with given uuid known"
    #     resp = JOb()
    #     resp.uuid = uuid
    #     resp.status = "Fail"
    #     resp.message = message
    #     return resp.dumps()

    @cherrypy.expose
    def getAllLastQualities(self):
        from virtualisation.wrapper.abstractwrapper import AbstractWrapper, AbstractComposedWrapper
        qualities = []
        wrappers = self.rm.wrappers
        for wrapper in wrappers:
            if isinstance(wrapper, AbstractWrapper):
                if wrapper.qoiSystem.initialised:
                    qualities.append(wrapper.qoiSystem.getLastQoI())
                    qualities[-1].uuid = wrapper.getSensorDescription().uuid
                else:
                    resp = JOb()
                    resp.uuid = wrapper.getSensorDescription().uuid
                    resp.status = "Fail"
                    resp.message = "Quality System not initialised for given uuid"
                    qualities.append(resp)
            elif isinstance(wrapper, AbstractComposedWrapper):
                for aWrapper in wrapper.wrappers:
                    if aWrapper.qoiSystem.initialised:
                        qualities.append(aWrapper.qoiSystem.getLastQoI())
                        qualities[-1].uuid = aWrapper.getSensorDescription().uuid
                    else:
                        resp = JOb()
                        resp.uuid = aWrapper.getSensorDescription().uuid
                        resp.status = "Fail"
                        resp.message = "Quality System not initialised for given uuid"
                        qualities.append(resp)
        return JOb(qualities).dumps()

    @cherrypy.expose
    def getQualityValues(self, uuid=None, types=None, avg=None, minimum=None, maximum=None):
        if types:
            types = types.split(",")
        if uuid:
            uuid = uuid.split(",")
        else:   #get all uuids from wrapper list
            from virtualisation.wrapper.abstractwrapper import AbstractWrapper, AbstractComposedWrapper
            uuid = []
            wrappers = self.rm.wrappers
            for wrapper in wrappers:
                if isinstance(wrapper, AbstractWrapper):
                    uuid.append(wrapper.getSensorDescription().uuid)
                elif isinstance(wrapper, AbstractComposedWrapper):
                    for aWrapper in wrapper.wrappers:
                        uuid.append(aWrapper.getSensorDescription().uuid)

        qualities = []
        for _uuid in uuid:
            message = None
            wrapper = self.rm.getWrapperByUUID(_uuid)
            message = ""
            if wrapper:
                if wrapper.qoiSystem.initialised:
                    avgQualities = []
                    avgQualities.append(wrapper.qoiSystem.getLastQoI(types=types, avg=avg, minimum=minimum, maximum=maximum))
                    avgQualities[-1].uuid = wrapper.getSensorDescription().uuid
                    qualities.extend(JOb(avgQualities))
                else:
                    message = "AVG Quality System not initialised for given uuid"
            else:
                message = "no stream with given uuid known"
            if message:
                resp = JOb()
                resp.uuid = _uuid
                resp.status = "Fail"
                resp.message = message
                qualities.append(resp)
        return JOb(qualities).dumps()
