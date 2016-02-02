import json
import threading

__author__ = 'Daniel Puschmann'

import os
from virtualisation.misc.jsonobject import JSONObject
from messagebus.rabbitmq import RabbitMQ
from virtualisation.misc.threads import QueueThread
from virtualisation.annotation.genericannotation import GenericAnnotation
from virtualisation.triplestore.threadedtriplestoreadapter import ThreadedTriplestoreAdapter

class GenericEventWrapper(object):

    def __init__(self, messageBusQueue=None):
        from virtualisation.resourcemanagement.resourcemanagement import ResourceManagement
        self.rm = ResourceManagement
        self.rabbitmqconnection, self.rabbitmqchannel = RabbitMQ.establishConnection(str(ResourceManagement.config.rabbitmq.host), ResourceManagement.config.rabbitmq.port)
        self.messageBusReceiveQueue = QueueThread(handler=self.receiveEventHandler)
        self.messageBusSendQueue = messageBusQueue
        self.eventDescriptions = {}
        self.splitters = None
        self.annotator = GenericAnnotation()
        self.exchange = RabbitMQ.exchange_event
        self.consumer_tag = None
        self.runthread = None

    def registerEvent(self, eventDescription):
        self.eventDescriptions[eventDescription.eventType] = eventDescription

    def getEventDescriptionByUUID(self, uuid):
        """
        Get an event description identified by an UUID
        :param uuid:
        :return:
        """
        for edt in self.eventDescriptions:
            if self.eventDescriptions[edt].uuid == uuid:
                return self.eventDescriptions[edt]
        return None

    def start(self):
        # RabbitMQ.declareExchange(self.rabbitmqchannel, self.exchange, _type="topic")
        queue = self.rabbitmqchannel.queue_declare()
        queue_name = queue.method.queue
        self.rabbitmqchannel.queue_bind(exchange=RabbitMQ.exchange_event, queue=queue_name, routing_key="#")

        self.runthread = threading.Thread(target=self._run)
        self.runthread.start()
        
    def isStarted(self):
        return self.runthread and self.runthread.is_alive()

    def _run(self):
        self.consumer_tag = self.rabbitmqchannel.basic_consume(self.receiveEventHandler, no_ack=True)
        self.rabbitmqchannel.start_consuming()

    def stop(self):
        self.rabbitmqchannel.stop_consuming(self.consumer_tag)

    def receiveEventHandler(self, channel, method, properties, body):

        """
        Receives messages through the message bus, annotates the event
         and sends the annotated event
        :param channel:
        :param method:
        :param properties:
        :param body:
        :return:
        """
        event = JSONObject(str(body))
        if event.ceType in self.eventDescriptions:
            # annotatedevent = self.annotator.annotateEvent(event, self.eventDescriptions[event.ceType])
            # if self.rm.args.messagebus and self.messageBusSendQueue:
            #     message = annotatedevent.serialize(format='n3')
            #     self.messageBusSendQueue.add((message, RabbitMQ.exchange_annotated_event, event.ceType))
            if self.rm.args.triplestore:
                ThreadedTriplestoreAdapter.getOrMake(self.eventDescriptions[event.ceType].graphName)


if __name__ == "__main__":
    import rdflib
    g = rdflib.graph.Graph()
    test_data = """
@prefix ces: <http://www.insight-centre.org/ces#> .
@prefix ct: <http://ict-citypulse.eu/city#> .
@prefix geo: <http://www.w3.org/2003/01/geo/wgs84_pos#> .
@prefix muo: <http://purl.oclc.org/NET/muo/muo#> .
@prefix owlss: <http://www.daml.org/services/owl-s/1.2/Service.owl#> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix qoi: <http://purl.oclc.org/NET/UASO/qoi#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix sao: <http://purl.oclc.org/NET/UNIS/sao/sao#> .
@prefix ssn: <http://purl.oclc.org/NET/ssnx/ssn#> .
@prefix tl: <http://purl.org/NET/c4dm/timeline.owl#> .
@prefix xml: <http://www.w3.org/XML/1998/namespace> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<http://ict-citypulse.eu/sensor/184621/Observation-49c5d469-e5b5-49f2-b889-cbabeb7bf109> a sao:Point ;
    qoi:hasQuality ct:Age-5c829612-f08b-40d9-a25d-10aeb673e0db,
        ct:Completeness-5c829612-f08b-40d9-a25d-10aeb673e0db,
        ct:Correctness-5c829612-f08b-40d9-a25d-10aeb673e0db,
        ct:Frequency-5c829612-f08b-40d9-a25d-10aeb673e0db,
        ct:Latency-5c829612-f08b-40d9-a25d-10aeb673e0db ;
    sao:hasUnitOfMeasurement <http://purl.oclc.org/NET/muo/ucum/unit/time/minute> ;
    sao:value "124" ;
    ssn:observationResultTime <http://ict-citypulse.eu/sensor/184621/ResultTime-5c829612-f08b-40d9-a25d-10aeb673e0db> ;
    ssn:observationSamplingTime <http://ict-citypulse.eu/sensor/184621/SamplingTime-5c829612-f08b-40d9-a25d-10aeb673e0db> ;
    ssn:observedBy <http://ict-citypulse.eu/SensorID-d0367e44-2bad-56c1-b881-a5dc89aee27e> ;
    ssn:observedProperty ct:AvgMeasuredTime-d0367e44-2bad-56c1-b881-a5dc89aee27e .

<http://ict-citypulse.eu/sensor/184621/Observation-5c829612-f08b-40d9-a25d-10aeb673e0db> a sao:Point ;
    qoi:hasQuality ct:Age-5c829612-f08b-40d9-a25d-10aeb673e0db,
        ct:Completeness-5c829612-f08b-40d9-a25d-10aeb673e0db,
        ct:Correctness-5c829612-f08b-40d9-a25d-10aeb673e0db,
        ct:Frequency-5c829612-f08b-40d9-a25d-10aeb673e0db,
        ct:Latency-5c829612-f08b-40d9-a25d-10aeb673e0db ;
    sao:hasUnitOfMeasurement <http://ict-citypulse.eu/unit:km-per-hour> ;
    sao:value "22.0" ;
    ssn:observationResultTime <http://ict-citypulse.eu/sensor/184621/ResultTime-5c829612-f08b-40d9-a25d-10aeb673e0db> ;
    ssn:observationSamplingTime <http://ict-citypulse.eu/sensor/184621/SamplingTime-5c829612-f08b-40d9-a25d-10aeb673e0db> ;
    ssn:observedBy <http://ict-citypulse.eu/SensorID-d0367e44-2bad-56c1-b881-a5dc89aee27e> ;
    ssn:observedProperty ct:AverageSpeed-d0367e44-2bad-56c1-b881-a5dc89aee27e .

<http://ict-citypulse.eu/sensor/184621/Observation-cd94028c-1e56-4ad0-966e-5ce8de329357> a sao:Point ;
    qoi:hasQuality ct:Age-5c829612-f08b-40d9-a25d-10aeb673e0db,
        ct:Completeness-5c829612-f08b-40d9-a25d-10aeb673e0db,
        ct:Correctness-5c829612-f08b-40d9-a25d-10aeb673e0db,
        ct:Frequency-5c829612-f08b-40d9-a25d-10aeb673e0db,
        ct:Latency-5c829612-f08b-40d9-a25d-10aeb673e0db ;
    sao:hasUnitOfMeasurement <http://ict-citypulse.eu/unit:number-of-vehicle-per-5min> ;
    sao:value "0" ;
    ssn:observationResultTime <http://ict-citypulse.eu/sensor/184621/ResultTime-5c829612-f08b-40d9-a25d-10aeb673e0db> ;
    ssn:observationSamplingTime <http://ict-citypulse.eu/sensor/184621/SamplingTime-5c829612-f08b-40d9-a25d-10aeb673e0db> ;
    ssn:observedBy <http://ict-citypulse.eu/SensorID-d0367e44-2bad-56c1-b881-a5dc89aee27e> ;
    ssn:observedProperty ct:StreetVehicleCount-d0367e44-2bad-56c1-b881-a5dc89aee27e .

<http://ict-citypulse.eu/unit:km-per-hour> a muo:UnitOfMeasurement .

<http://ict-citypulse.eu/unit:number-of-vehicle-per-5min> a muo:UnitOfMeasurement .

<http://purl.oclc.org/NET/muo/ucum/unit/time/minute> a muo:UnitOfMeasurement .

ct:Age-5c829612-f08b-40d9-a25d-10aeb673e0db a qoi:Age ;
    qoi:hasAbsoluteQuality "311.000" ;
    qoi:hasRatedQuality "0.000" ;
    qoi:hasUnitOfMeasurement <http://purl.oclc.org/NET/muo/ucum/unit/time/second> .

ct:Completeness-5c829612-f08b-40d9-a25d-10aeb673e0db a qoi:Completeness ;
    qoi:hasAbsoluteQuality "4.000" ;
    qoi:hasRatedQuality "1.000" ;
    qoi:hasUnitOfMeasurement <http://purl.oclc.org/NET/muo/ucum/physical-quality/number> .

ct:Correctness-5c829612-f08b-40d9-a25d-10aeb673e0db a qoi:Correctness ;
    qoi:hasAbsoluteQuality "1.000" ;
    qoi:hasRatedQuality "1.000" ;
    qoi:hasUnitOfMeasurement <http://purl.oclc.org/NET/muo/ucum/unit/fraction/percent> .

ct:Frequency-5c829612-f08b-40d9-a25d-10aeb673e0db a qoi:Frequency ;
    qoi:hasAbsoluteQuality "0.003" ;
    qoi:hasRatedQuality "1.000" ;
    qoi:hasUnitOfMeasurement <http://purl.oclc.org/NET/muo/ucum/unit/frequency/Herz> .

ct:Latency-5c829612-f08b-40d9-a25d-10aeb673e0db a qoi:Latency ;
    qoi:hasAbsoluteQuality "0.012" ;
    qoi:hasRatedQuality "1.000" ;
    qoi:hasUnitOfMeasurement <http://purl.oclc.org/NET/muo/ucum/unit/time/second> .

<http://ict-citypulse.eu/sensor/184621/ResultTime-5c829612-f08b-40d9-a25d-10aeb673e0db> a tl:Instant ;
    tl:at "2015-11-17T08:50:00"^^xsd:dateTime .

<http://ict-citypulse.eu/sensor/184621/SamplingTime-5c829612-f08b-40d9-a25d-10aeb673e0db> a tl:Instant ;
    tl:at "2015-11-17T08:55:11"^^xsd:dateTime .


    """
    g.parse(data=test_data, format='n3')
    # for s,o,p in g.triples( (None, rdflib.RDF.type, None )):
    for s,o,p in g.triples( (None, rdflib.RDF.type, rdflib.URIRef('http://purl.oclc.org/NET/UNIS/sao/sao#Point') )):
        print s,o,p
