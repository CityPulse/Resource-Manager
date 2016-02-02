import threading
import time

__author__ = 'Marten Fischer'

import os
from virtualisation.misc.jsonobject import JSONObject
from messagebus.rabbitmq import RabbitMQ
from virtualisation.misc.threads import QueueThread
from virtualisation.triplestore.threadedtriplestoreadapter import ThreadedTriplestoreAdapter

class EventGenerator(object):

    def __init__(self):
        self.config = JSONObject(file(os.path.join(os.path.dirname(__file__), "..", "config.json"), "rb"))
        self.host = self.config.rabbitmq.host
        self.port = self.config.rabbitmq.port
        RabbitMQ.establishConnection(self.host, self.port)
        self.messageBusReceiveQueue = QueueThread(handler=self.receiveEventHandler)
        self.exchange = RabbitMQ.exchange_annotated_event

    def run(self):
        RabbitMQ.declareExchange(self.rabbitmqchannel, self.exchange, _type="topic")
        RabbitMQ.declareExchange(self.rabbitmqchannel, RabbitMQ.exchange_event, _type="topic")
        queue = self.rabbitmqchannel.queue_declare()
        queue_name = queue.method.queue
        RabbitMQ.channel.queue_bind(exchange=RabbitMQ.exchange_event, queue=queue_name, routing_key="#")

        self.runthread = threading.Thread(target=self._run)
        self.runthread.start()

    def _run(self):
        # self.channel.basic_consume(self.receiveEventHandler, no_ack=True)
        # self.channel.start_consuming()
        while True:
            time.sleep(5.0)
            self.sendEvent()

    def receiveEventHandler(self, channel, method, properties, body):
        """
        Receives messages throught the message bus, annotates the event
         and sends the annotated event
        :param channel:
        :param method:
        :param properties:
        :param body:
        :return:
        """
        print "Received:", body
        # event = json.loads(body)
        # annotatedevent = self.annotateEvent(event)
        # self.messageBusSendQueue.add(annotatedevent)

    def sendEvent(self):
        e = self.makeRandomEvent()
        message = e.dumps()
        RabbitMQ.sendMessage(message, RabbitMQ.exchange_event, e.ceType)
        print "sent", message

    def makeRandomEvent(self):
        eventData = JSONObject()
        eventData.ceID = 123456
        eventData.ceType = "Aarhus_Road_Traffic_Event"
        eventData.ceName = "traffic jam"
        eventData.ceTime = 1438591234000L
        eventData.ceCoordinate = "(56.12 10.13)"
        eventData.ceLevel = 1
        eventData.dummy = True

        return eventData

if __name__ == "__main__":
    eg = EventGenerator()
    eg.run()