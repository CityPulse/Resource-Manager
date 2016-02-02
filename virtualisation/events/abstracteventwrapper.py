import json
import threading

__author__ = 'Daniel Puschmann'

import abc
import os
from virtualisation.misc.jsonobject import JSONObject
from messagebus.rabbitmq import RabbitMQ
from virtualisation.misc.threads import QueueThread
from virtualisation.annotation.genericannotation import GenericAnnotation
from virtualisation.triplestore.threadedtriplestoreadapter import ThreadedTriplestoreAdapter
import zipfile

class AbstractEventWrapper(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        self.config = JSONObject(file(os.path.join(os.path.dirname(__file__), "..", "config.json"), "rb"))
        self.host = self.config.rabbitmq.host
        self.port = self.config.rabbitmq.port
        # self.rabbitmqconnection, self.rabbitmqchannel = RabbitMQ.establishConnection(self.host, self.port)
        self.messageBusReceiveQueue = QueueThread(handler=self.receiveEventHandler)
        self.messageBusSendQueue = QueueThread(handler=self.sendAnnotatedEventHandler)
        self.wrappers = []
        self.splitters = None
        self.annotator = GenericAnnotation()
        self.exchange = RabbitMQ.exchange_annotated_event

    @abc.abstractmethod
    def getEventDescription(self):
        """
        :return: a event description
        """
        pass

    @classmethod
    def getFileObject(cls, currentfile, filename, mode="r"):
        parent = os.path.dirname(currentfile)
        if parent.endswith(".zip"):
            zFile = zipfile.ZipFile(parent)
            return zFile.open(filename, mode)
        else:
            return file(os.path.join(parent, filename), mode)
    # def addWrapper(self, wrapper):
    #     """
    #     adds a wrapper to the internal wrapper list
    #     :param wrapper:
    #     :return:
    #     """
    #     if not isinstance(wrapper, AbstractEventWrapper):
    #         raise Exception(error="trying to add a wrapper of the wrong instance. Requires AbstractEventWRapper")
    #     self.wrappers.append(wrapper)

    def start(self):
        "@Daniel P: The ResourceManagement declares all available exchanges. I guess this is unnecessary therefore."
        # RabbitMQ.declareExchange(self.rabbitmqchannel, self.exchange, _type="topic")
        queue = RabbitMQ.channel.queue_declare()
        queue_name = queue.method.queue
        # in the following line the exchange should be RabbitMQ.exchange_event
        RabbitMQ.channel.queue_bind(exchange=self.exchange, queue=queue_name,
                                        routing_key=self.getEventDescription().messagebus.routingKey)


    def run(self):
        """
        start listening on the event detection component
        :return:
        """
        # self.__forEachWrapper("run")
        self.runthread = threading.Thread(target=self._run)
        self.runthread.start()

    def _run(self):
        self.channel.basic_consume(self.receiveEventHandler, no_ack=True)
        self.channel.start_consuming()

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
        event = json.loads(body)
        annotatedevent = self.annotateEvent(event)
        self.messageBusSendQueue.add(annotatedevent)

    def annotateEvent(self, event):
        """
        Annotates the event and saves the graph in the triple store
        :param event:
        :return: returns the annotated graph of the event
        """
        graph = self.annotator.annotateEvent(event, self.getEventDescription())
        ThreadedTriplestoreAdapter.getOrMake(self.getEventDescription().graphname)
        return graph

    def sendAnnotatedEventHandler(self, annotatedevent):
        key = self.getEventDescription().messagebus.routingKey
        message = annotatedevent.serialize(format='n3')
        RabbitMQ.sendMessage(message, self.exchange, key)