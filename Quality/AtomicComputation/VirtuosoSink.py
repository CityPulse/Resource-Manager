# coding=utf-8
from messagebus.rabbitmq import RabbitMQ
from reputationsystem.sink import Sink
import saopy
from virtualisation.triplestore.threadedtriplestoreadapter import ThreadedTriplestoreAdapter


__author__ = 'Thorben Iggena (t.iggena@hs-osnabrueck.de)'


class VirtuosoSink(Sink):
    # avoid namespace prefixes in the exported graph, that are not required.
    namespaceBindings = {
        # "owl":"http://www.w3.org/2002/07/owl#",
        "sao": "http://purl.oclc.org/NET/UNIS/sao/sao#",
        # "xs": "http://www.w3.org/2001/XMLSchema",
        # "skos": "http://www.w3.org/2004/02/skos/core#",
        "qoi": "http://purl.oclc.org/NET/UASO/qoi#",
        # "xml": "http://www.w3.org/XML/1998/namespace",
        # "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
        # "wot": "http://xmlns.com/wot/0.1/",
        # "daml": "http://www.daml.org/2001/03/daml+oil#",
        # "muo": "http://purl.oclc.org/NET/muo/muo#",
        # "foaf": "http://xmlns.com/foaf/0.1/",
        # "DUL": "http://www.loa-cnr.it/ontologies/DUL.owl#",
        # "time": "http://www.w3.org/2006/time#",
        # "dc": "http://purl.org/dc/elements/1.1/",
        # "ssn": "http://purl.oclc.org/NET/ssnx/ssn#",
        # "ces": "http://www.insight-centre.org/ces#",
        # "tzont": "http://www.w3.org/2006/timezone#",
        # "go": "http://www.daml.org/services/owl-s/1.2/Grounding.owl#",
        # "geo": "http://www.w3.org/2003/01/geo/wgs84_pos#",
        # "so": "http://www.daml.org/services/owl-s/1.2/Service.owl#",
        # "sp": "http://www.daml.org/services/owl-s/1.2/ServiceParameter.owl#",
        # "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
        # "xsd": "http://www.w3.org/2001/XMLSchema#",
        # "prov": "http://www.w3.org/ns/prov#",
        # "owlssc": "http://www.daml.org/services/owl-s/1.2/ServiceCategory.owl#",
        # "tl": "http://purl.org/NET/c4dm/timeline.owl#",
        "ct": "http://ict-citypulse.eu/city#"
    }

    def __init__(self, messageBusQueue=None):
        super(VirtuosoSink, self).__init__()
        self.GRAPH_BASE_URI = None
        self.messageBusQueue = messageBusQueue

    def update(self, qoiMetric):
        self.metrics[qoiMetric.name] = qoiMetric

    def persist(self, observationIdList):
      
        graphList = []
           
        if not self.GRAPH_BASE_URI:
            self.GRAPH_BASE_URI = self.reputationsystem.description.fullSensorID + "/Quality-"

        for observationId in observationIdList:
            saoOut = saopy.SaoInfo()
            saoOut.namespaceBindings = VirtuosoSink.namespaceBindings
            observation = saopy.sao.Point(self.reputationsystem.description.fullSensorID + "/Observation-" + str(observationId))
            saoOut.add(observation)
            
            mName = self.GRAPH_BASE_URI + "%s-" + str(observationId)

            for metricName in self.metrics:
                m = self.metrics[metricName]

                if m.name == "Latency":
                    latency = saopy.qoi.Latency(mName % m.name)
                    latency.hasLatency = "%f" % (m.ratedValue)
                    observation.hasQuality.add(latency)
                    saoOut.add(latency)
                elif m.name == "Age":
                    age = saopy.qoi.Age(mName % m.name)
                    age.hasAge = "%f" % (m.ratedValue)
                    observation.hasQuality.add(age)
                    saoOut.add(age)
                elif m.name == "Frequency":
                    frequency = saopy.qoi.Frequency(mName % m.name)
                    frequency.hasFrequency = "%f" % (m.ratedValue)
                    observation.hasQuality.add(frequency)
                    saoOut.add(frequency)
                elif m.name == "Completeness":
                    completeness = saopy.qoi.Completeness(mName % m.name)
                    completeness.hasCompleteness = "%f" % (m.ratedValue)
                    observation.hasQuality.add(completeness)
                    saoOut.add(completeness)
                elif m.name == "Correctness":
                    correctness = saopy.qoi.Correctness(mName % m.name)
                    correctness.hasCorrectness = "%f" % (m.ratedValue)
                    observation.hasQuality.add(correctness)
                    saoOut.add(correctness)

            graph = saopy.RDFInterface.exportRDFGraph(saoOut)
#             print graph.serialize(format="n3")
            graphList.append(graph)
        
        if ThreadedTriplestoreAdapter.triplestore:
            virtuosoWriter = ThreadedTriplestoreAdapter(self.reputationsystem.description.graphName)
            virtuosoWriter.addGraphList(graphList)
            
        #check if message bus is used and send graphs to bus
        if self.messageBusQueue:
            for graph in graphList:
                self.messageBusQueue.add((graph.serialize(format="n3"), RabbitMQ.exchange_quality, self.reputationsystem.description.messagebus.routingKey))
