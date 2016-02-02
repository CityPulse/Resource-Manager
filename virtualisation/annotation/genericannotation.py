from virtualisation.clock.abstractclock import AbstractClock

__author__ = 'Marten Fischer (m.fischer@hs-osnabrueck.de)'

from abstractannotation import AbstractAnnotation
import saopy
import uuid
import rdflib

class GenericAnnotation(AbstractAnnotation):
    """
    Class to annotate observation.
    """
    # avoid namespace prefixes in the exported graph, that are not required.
    # namespaceBindings = {
    #     # "owl":"http://www.w3.org/2002/07/owl#",
    #     "sao": "http://purl.oclc.org/NET/UNIS/sao/sao#",
    #     # "xs": "http://www.w3.org/2001/XMLSchema",
    #     # "skos": "http://www.w3.org/2004/02/skos/core#",
    #     "qoi": "http://purl.oclc.org/NET/UASO/qoi#",
    #     # "xml": "http://www.w3.org/XML/1998/namespace",
    #     # "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    #     # "wot": "http://xmlns.com/wot/0.1/",
    #     # "daml": "http://www.daml.org/2001/03/daml+oil#",
    #     "muo": "http://purl.oclc.org/NET/muo/muo#",
    #     "foaf": "http://xmlns.com/foaf/0.1/",
    #     # "DUL": "http://www.loa-cnr.it/ontologies/DUL.owl#",
    #     # "time": "http://www.w3.org/2006/time#",
    #     "dc": "http://purl.org/dc/elements/1.1/",
    #     "ssn": "http://purl.oclc.org/NET/ssnx/ssn#",
    #     "ces": "http://www.insight-centre.org/ces#",
    #     # "tzont": "http://www.w3.org/2006/timezone#",
    #     # "go": "http://www.daml.org/services/owl-s/1.2/Grounding.owl#",
    #     # "geo": "http://www.w3.org/2003/01/geo/wgs84_pos#",
    #     # "so": "http://www.daml.org/services/owl-s/1.2/Service.owl#",
    #     # "sp": "http://www.daml.org/services/owl-s/1.2/ServiceParameter.owl#",
    #     # "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    #     # "xsd": "http://www.w3.org/2001/XMLSchema#",
    #     "prov": "http://www.w3.org/ns/prov#",
    #     "tl": "http://purl.org/NET/c4dm/timeline.owl#",
    #     "ct": "http://ict-citypulse.eu/city#"
    # }

    allowedNamespaceBindings = ["sao", "muo", "ssn", "ces", "geo", "owlss", "prov", "tl", "qoi"]
    namespaceBindings = {}
    for anb in allowedNamespaceBindings:
        namespaceBindings[anb] = saopy.model.namespaceBindings[anb]
    namespaceBindings["ct"] = "http://ict-citypulse.eu/city#"

    QOI_METRIC_FUNCTION_MAP = {} #{'Correctness': , 'Latency': , 'Age': , 'Frequency': , 'Completeness': }

    def annotateObservation(self, data, sensordescription, clock, quality):
        saoOut = saopy.SaoInfo()
        saoOut.namespaceBindings = GenericAnnotation.namespaceBindings

        if not isinstance(data, list):
            data = [data]
        if not isinstance(quality, list):
            quality = [quality]

        # for data_item in data:
        for i in range(0, len(data)):
            data_item = data[i]
            quality_item = quality[i] if i < len(quality) else None
            samplingTime = None
            resultTime = None
            qualityProperties = []
            if len(data_item.fields) > 0:
                # prepare sampling and result time
                firstField = data_item[data_item.fields[0]]
                samplingTime = saopy.tl.Instant("%s/SamplingTime-%s" % (sensordescription.fullSensorID, firstField.observationID))
                samplingTime.at = rdflib.Literal(str(firstField.observationSamplingTime), datatype=rdflib.XSD.dateTime) #firstField.observationSamplingTime
                saoOut.add(samplingTime)

                resultTime = saopy.tl.Instant("%s/ResultTime-%s" % (sensordescription.fullSensorID, firstField.observationID))
                if sensordescription.isTimestampedStream():
                    resultTime.at = rdflib.Literal(str(firstField.observationResultTime), datatype=rdflib.XSD.dateTime)
                else:
                    resultTime.at = rdflib.Literal(str(firstField.observationSamplingTime), datatype=rdflib.XSD.dateTime)
                saoOut.add(resultTime)

                # prepare the quality properties
                if quality_item:
                    for qoiName in quality_item:
                        qoiMetric = getattr(saopy.qoi, qoiName)("%scity#%s-%s" % (sensordescription.namespace, qoiName, data_item[data_item.fields[0]].observationID))
                        setattr(qoiMetric, "hasRatedQuality", "%.3f" % float(quality_item[qoiName].ratedValue))
                        setattr(qoiMetric, "hasAbsoluteQuality", "%.3f" % float(quality_item[qoiName].absoluteValue))
                        setattr(qoiMetric, "hasUnitOfMeasurement", saopy.muo.UnitOfMeasurement("%s" % quality_item[qoiName].unit))
                        qualityProperties.append(qoiMetric)
                        saoOut.add(qoiMetric)

            # sensor = saopy.ssn.Sensor(sensordescription.namespace + sensordescription.sensorName)
            sensor = saopy.ssn.Sensor(sensordescription.namespace + "SensorID-" + sensordescription.uuid)

            for fieldname in data_item.fields:
                if sensordescription.isTimestampedStream() and fieldname == sensordescription.timestamp.inField:
                    continue
                if "skip_annotation" in sensordescription.field[fieldname] and sensordescription.field[fieldname].skip_annotation:
                    continue
                # TODO missing fields can not be annotated
                if not fieldname in data_item:
                    continue
                field = data_item[fieldname]
                observation = saopy.sao.Point("%s/Observation-%s" % (sensordescription.fullSensorID, field.observationID))
                observation.value = str(field.value)
                observation.observedBy = sensor

                if samplingTime:  # in this case there should also be a result time
                    observation.observationSamplingTime = samplingTime
                    observation.observationResultTime = resultTime

                # if "unit" in field:
                if "unit" in sensordescription.field[fieldname]:
                    mu = saopy.muo.UnitOfMeasurement(sensordescription.field[fieldname].unit)
                    observation.hasUnitOfMeasurement = mu
                    saoOut.add(mu)
                prop = saopy.ssn.Property("".join([field.propertyURI, "-", sensordescription.uuid]))
                observation.observedProperty = prop
                saoOut.add(observation)

                # add quality data
                for qProperty in qualityProperties:
                    observation.hasQuality.add(qProperty)

        return saopy.RDFInterface.exportRDFGraph(saoOut)

    def annotateAggregation(self, aggregationdata, sensordescription):
        saoOut = saopy.SaoInfo()
        saoOut.namespaceBindings = GenericAnnotation.namespaceBindings
        sensor = saopy.ssn.Sensor(sensordescription.fullSensorID)
        sensorproperty = saopy.ssn.Property(aggregationdata.data['field'].propertyURI)
        sensorproperty.description = aggregationdata.data['field'].propertyName
        sensor.observes.add(sensorproperty)

        interval = saopy.tl.Interval(sensordescription.namespace+"timeinterval")
        interval.beginsAtDateTime = str(aggregationdata.start)
        interval.endsAtDateTime = str(aggregationdata.end)

        aggregationId = sensordescription.namespace + "Aggregation-" + str(uuid.uuid4())
        if aggregationdata.aggregationMethod is 'dft':
            aggregation = saopy.sao.DiscreteFourierTransform(aggregationId)
        if aggregationdata.aggregationMethod is 'paa':
            aggregation = saopy.sao.PiecewiseAggregateApproximation(aggregationId)
        if aggregationdata.aggregationMethod is 'sensorsax':
            aggregation = saopy.sao.SensorSAX(aggregationId)
        else: #if aggregationdata.aggregationMethod is 'sax':
            aggregation = saopy.sao.SymbolicAggregateApproximation(aggregationId)
        aggregation.value = aggregationdata.graph
        aggregation.wasAttributedTo = sensorproperty
        aggregation.time = interval
        aggregation.alphabetsize
        aggregation.segmentsize = aggregationdata.size
        mu = saopy.muo.UnitOfMeasurement(sensordescription.namespace+'unit:'+ aggregationdata.data['field'].unit)
        aggregation.hasUnitOfMeasurement = mu

        saoOut.add(aggregation)
        saoOut.add(sensorproperty)
        saoOut.add(sensor)
        return saopy.RDFInterface.exportRDFGraph(saoOut)

    def annotateEvent(self, eventdata, eventdescription):
        saoOut = saopy.SaoInfo()
        saoOut.namespaceBindings = GenericAnnotation.namespaceBindings
        event = saopy.sao.StreamEvent(eventdescription.namespace + "StreamEvent-" + str(eventdata.ceID))
        event.openid = saopy.foaf.Document(eventdescription.namespace + str(eventdata.ceID))
        event.name = eventdata.ceName # uco:hasLabel

        location = saopy.prov.Location(eventdescription.namespace + "Location")
        #FIXME where to place to coordinates?
        location.description = eventdata.ceCoordinate # event:place as geo:SpatialThing
        event.atLocation = location

        """
        @Marten Fischer: I am not sure if this is right,
        I will ask Thu what the description of the event is
        """
        event.description = eventdata.ceType # uco:hasCategory (class)
        """
        @Marten Fischer: Possibly ceTime contains more information
        than just the timestamp (e.g. start/end time). In that case,
        this needs to be parsed and annotated.
        @ DanielP: At the moment the timestamp is only a Long. Apparently
        there will be a 'StopEvent'.
        """
        event.Timestamp = eventdescription.parseTimestamp(eventdata[eventdescription.timestamp.inField]).strftime(AbstractClock.format) # event:time as time:TemporalEntity
        """
        @Marten Fischer: Do we have something which is equivalent
        to ceWeight in the ontology?
        @ Daniel P: I haven't seen one.
        """
        agent = saopy.foaf.Agent(eventdescription.namespace + eventdescription.author)

        event.label = str(eventdata.ceLevel) # uco:hasLevel a xsd:integer

        event.creator = agent

        saoOut.add(event)
        saoOut.add(agent)
        saoOut.add(location)
        return saopy.RDFInterface.exportRDFGraph(saoOut)