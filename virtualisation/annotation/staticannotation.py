from virtualisation.triplestore.threadedtriplestoreadapter import ThreadedTriplestoreAdapter
from messagebus.rabbitmq import RabbitMQ
import saopy
import re
import threading

__author__ = 'Marten Fischer (m.fischer@hs-osnabrueck.de)'

# TODO new event streams need to be annotated and saved into the virtuoso store

class StaticAnnotator(object):
    # avoid namespace prefixes in the exported graph, that are not required.
    allowedNamespaceBindings = ["sao", "muo", "ssn", "ces", "geo", "owlss", "prov", "tl", "owlssc"]
    namespaceBindings = {}
    for anb in allowedNamespaceBindings:
        namespaceBindings[anb] = saopy.model.namespaceBindings[anb]
    namespaceBindings["ct"] = "http://ict-citypulse.eu/city#"

    service_repository_name = "citypulse/datasets/servicerepository"

    @classmethod
    def dumpGraph(cls):
        """
        Dumps the graph with the static annotations
        :return:
        """
        if ThreadedTriplestoreAdapter.triplestore:
            ThreadedTriplestoreAdapter.triplestore.deleteGraph(StaticAnnotator.service_repository_name)

    @classmethod
    def threadedStaticAnnotationSensor(cls, wrapper, configuration, messageBusQueue, api=None):
        threading.Thread(target=StaticAnnotator.staticAnnotationSensor, args=(wrapper, configuration, messageBusQueue, api)).start()

    @classmethod
    def staticAnnotationSensor(cls, wrapper, configuration, messageBusQueue, api=None):
        sd = wrapper.getSensorDescription()
        if isinstance(sd, list):
            for _sd in sd:
                graph = StaticAnnotator.__staticAnnotationSesnor(_sd, configuration)
                if messageBusQueue or api:
                    msg = graph.serialize(format='n3')
                if messageBusQueue:
                    messageBusQueue.add((msg, RabbitMQ.exchange_wrapper_registration, _sd.messagebus.routingKey))
                if api:
                    api.set_static_stream_data(str(_sd.uuid), msg)
                if ThreadedTriplestoreAdapter.triplestore:
                    ThreadedTriplestoreAdapter.getOrMake(StaticAnnotator.service_repository_name).saveGraph(graph, StaticAnnotator.service_repository_name)
        else:
            graph = StaticAnnotator.__staticAnnotationSesnor(sd, configuration)
            if messageBusQueue or api:
                msg = graph.serialize(format='n3')
            if messageBusQueue:
                messageBusQueue.add((msg, RabbitMQ.exchange_wrapper_registration, sd.messagebus.routingKey))
            if api:
                api.set_static_stream_data(str(sd.uuid), msg)
            if ThreadedTriplestoreAdapter.triplestore:
                ThreadedTriplestoreAdapter.getOrMake(StaticAnnotator.service_repository_name).saveGraph(graph, StaticAnnotator.service_repository_name)

    @classmethod
    def __staticAnnotationSesnor(cls, sd, configuration):
        saoOut = saopy.SaoInfo()
        saoOut.namespaceBindings = StaticAnnotator.namespaceBindings
        uuid = str(sd.uuid)

        serviceCategory = saopy.owlssc.ServiceCategory(sd.namespace + "ServiceCategory-" + uuid)
        serviceCategory.serviceCategoryName = sd.sensorType

        # city = saopy.foaf.Organization("http://ict-citypulse.eu/cityofaarhus") # this line was useless! I suppose its not needed.
        city = saopy.prov.Agent(sd.namespace + sd.author)

        sensor_name = sd.namespace + "SensorID-" + uuid
        sensor = saopy.ssn.Sensor(sensor_name)
        primitiveEventService = saopy.ces.PrimitiveEventService(sd.namespace + "PrimitiveEventService-" + uuid)
        primitiveEventService.hasPhysicalEventSource = sensor
        eventprofile = saopy.ces.EventProfile(sd.namespace + "EventProfile-" + uuid)

        eventprofile.serviceCategory = serviceCategory
        primitiveEventService.presents = eventprofile

        # Message Bus Grounding
        messagebusgrounding = saopy.ces.MessageBusGrounding(sd.namespace + "MessageBusGrounding-" + uuid)
        messagebusgrounding.hasTopic = sd.messagebus.routingKey
        exchanges = ["annotated_data", "quality", "aggregated_data"]
        for exchange in exchanges:
            messagebusgrounding.hasExchangeName.add(exchange)

        messagebusgrounding.hasServerAddress = str("amqp://guest:guest@%s:%d" % (configuration.rabbitmq.host,
                                                                                        configuration.rabbitmq.port))
        primitiveEventService.supports.add(messagebusgrounding)

        # is this required?
        # will every stream made available via HTTP?
        httpgrouding = saopy.ces.HttpGrounding(sd.namespace + "HttpGrounding-" + uuid)
        httpgrouding.httpService = "http://%s:%d/api/snapshot?uuid=%s" % (str(configuration.interface["global"]["server.socket_host"]), int(configuration.interface["global"]["server.socket_port"]), uuid)  #"http://140.203.155.76:8010/traffic/annotated/" + uuid
        primitiveEventService.supports.add(httpgrouding)

        psourcehttp = saopy.prov.Entity(sd.source)
        psourceid = saopy.prov.Entity(sd.namespace + sd.sensorName) #(sd.fullSensorID)

        foi = saopy.ssn.FeatureOfInterest(sd.namespace + "FeatureOfInterest-" + uuid)

        locations = StaticAnnotator.__annotateLocation(foi, sd, uuid)
        if locations:
            firstlocation, secondlocation = locations
            if "cityName" in sd:
                firstlocation.hasCityName = sd.cityName[0] if isinstance(sd.cityName, list) else sd.cityName
            if "countryName" in sd:
                firstlocation.hasCountryName = sd.countryName[0] if isinstance(sd.countryName, list) else sd.countryName
            if "streetName" in sd:
                firstlocation.hasStreetName = sd.streetName[0] if isinstance(sd.streetName, list) else sd.streetName
            if "postalCode" in sd:
                firstlocation.hasPostCode = sd.postalCode[0] if isinstance(sd.postalCode, list) else sd.postalCode
            saoOut.add(firstlocation)
            if secondlocation:
                if "cityName" in sd:
                    secondlocation.hasCityName = sd.cityName[1] if isinstance(sd.cityName, list) else sd.cityName
                if "countryName" in sd:
                    secondlocation.hasCountryName = sd.countryName[1] if isinstance(sd.countryName, list) else sd.countryName
                if "streetName" in sd:
                    secondlocation.hasStreetName = sd.streetName[1] if isinstance(sd.streetName, list) else sd.streetName
                if "postalCode" in sd:
                    secondlocation.hasPostCode = sd.postalCode[1] if isinstance(sd.postalCode, list) else sd.postalCode
                saoOut.add(secondlocation)

        sensor.hadPrimarySource.add(psourceid)
        sensor.hadPrimarySource.add(psourcehttp)

        # Describing the provenance of the data stream
        sensor.wasAttributedTo = city

        for field in sd.fields:
            if sd.isTimestampedStream() and field == sd.timestamp.inField:
                continue
            if "propertyPrefix" in sd.field[field]:
                _property = getattr(getattr(saopy, sd.field[field].propertyPrefix), sd.field[field].propertyName)("".join([sd.field[field].propertyURI, "-", uuid])) # do we need the propertyURI, or can we do it as below
            else:
                _property = getattr(saopy.ct, sd.field[field].propertyName)("".join([sd.field[field].propertyURI, "-", uuid])) # do we need the propertyURI, or can we do it as below
            # TODO: fix that
            _property._initialised = False
            _property.isPropertyOf = foi
            _property._initialised = True
            sensor.observes.add(_property)
            saoOut.add(_property)

        # According to Sefki,there shall not be a generic way to store  static values.
        # Each static value will be a special case. No idea how to deal with this :( .
        # for staticproperty in sd.staticproperties:
        #     sp = sd.staticproperties[staticproperty]
        #     if "propertyPrefix" in sp:
        #         _property = getattr(getattr(saopy, sp.propertyPrefix), sp.propertyName)("".join([sp.propertyURI, "-", uuid]))
        #     else:
        #         _property = getattr(saopy.ct, sp.propertyName)("".join([sp.propertyURI, "-", uuid]))
        #     _property._initialised = False
        #     _property.isPropertyOf = foi
        #     _property._initialised = True
        #
        #     observation = saopy.sao.Point("%s/Observation-%s" % (sd.fullSensorID, uuid))
        #     observation.value = str(sp.value)
        #     observation.observedBy = sensor
        #     sensor.observes.add(_property)
        #     observation.observedProperty = _property
        #     saoOut.add(observation)
        #     saoOut.add(_property)

        saoOut.add(city)
        saoOut.add(psourceid)

        saoOut.add(psourcehttp)
        saoOut.add(httpgrouding)
        saoOut.add(messagebusgrounding)

        saoOut.add(serviceCategory)
        saoOut.add(eventprofile)

        saoOut.add(foi)
        saoOut.add(sensor)
        saoOut.add(primitiveEventService)
        return saopy.RDFInterface.exportRDFGraph(saoOut)

    @classmethod
    def __annotateLocation(cls, foi, sd, _id):
        # first check if no location is present
        if not "location" in sd:
            return None

        # TODO: POLYGON location
        linestr_re = re.compile('LINESTRING\((\d+.\d+) (\d+.\d+) *, *(\d+.\d+) (\d+.\d+)\)')
        point_re = re.compile('POINT\((\d+.\d+) (\d+.\d+)\)')
        l = sd.location

        # try linestring
        m = linestr_re.match(l)
        if m:
            firstlocation = saopy.geo.SpatialThing(sd.namespace + "BeginsAtLocation-" + _id)
            firstlocation.lat = m.group(2)
            firstlocation.long = m.group(1)
            secondlocation = saopy.geo.SpatialThing(sd.namespace + "EndsAtLocation-" + _id)
            secondlocation.lat = m.group(4)
            secondlocation.long = m.group(3)
            foi.beginsAtLocation = firstlocation
            foi.endsAtLocation = secondlocation
            return firstlocation, secondlocation
        else:
            # try point
            m = point_re.match(l)
            if m:
                firstlocation = saopy.geo.SpatialThing(sd.namespace + "Location-" + _id)
                firstlocation.lat = m.group(2)
                firstlocation.long = m.group(1)
                foi.hasLocation = firstlocation
                return firstlocation, None
            else:
                return None


class StaticEventAnnotator(object):
    # avoid namespace prefixes in the exported graph, that are not required.
    allowedNamespaceBindings = ["sao", "muo", "ssn", "ces", "geo", "owlss", "prov", "tl"]
    namespaceBindings = {}
    for anb in allowedNamespaceBindings:
        namespaceBindings[anb] = saopy.model.namespaceBindings[anb]
    namespaceBindings["ct"] = "http://ict-citypulse.eu/city#"

    event_repository_name = "citypulse/datasets/eventrepository"

    @classmethod
    def threadedStaticEventAnnotation(cls, wrapper, configuration, messageBusQueue):
        threading.Thread(target=StaticEventAnnotator.staticAnnotationEvent, args=(wrapper, configuration, messageBusQueue)).start()

    @classmethod
    def staticAnnotationEvent(cls, wrapper, configuration, messageBusQueue):
        sd = wrapper.getSensorDescription()
        if isinstance(sd, list):
            for _sd in sd:
                graph = StaticEventAnnotator.__staticAnnotationEvent(_sd, configuration)
                #TODO send graph over messagebus?
                # if messageBusQueue:
                #     msg = graph.serialize(format='n3')
                #     messageBusQueue.add((msg, RabbitMQ.exchange_wrapper_registration, _sd.messagebus.routingKey))
                ThreadedTriplestoreAdapter.getOrMake(StaticEventAnnotator.event_repository_name).saveGraph(graph, StaticEventAnnotator.event_repository_name)
        else:
            graph = StaticEventAnnotator.__staticAnnotationEvent(sd, configuration)
            # if messageBusQueue:
            #     msg = graph.serialize(format='n3')
            #     messageBusQueue.add((msg, RabbitMQ.exchange_wrapper_registration, sd.messagebus.routingKey))
            ThreadedTriplestoreAdapter.getOrMake(StaticEventAnnotator.event_repository_name).saveGraph(graph, StaticEventAnnotator.event_repository_name)

    @classmethod
    def __staticAnnotationEvent(cls, sd, configuration):
        saoOut = saopy.SaoInfo()
        saoOut.namespaceBindings = StaticAnnotator.namespaceBindings

        #TODO create the graph

        return saopy.RDFInterface.exportRDFGraph(saoOut)
