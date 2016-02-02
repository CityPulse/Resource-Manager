import csv
import json

from virtualisation.misc.jsonobject import JSONObject as JOb
import os
from rabbitmq import RabbitMQ
__author__ = 'Daniel Puschmann'


class ConsumerDummy(object):
    """
    Default listener, to test if messages are sent through the message bus.
    """

    def __init__(self, exchange, key):
        self.config = JOb(file(os.path.join(os.path.dirname(__file__), "..", "virtualisation", "config.json"), "rb"))
        self.host = self.config.rabbitmq.host
        self.port = self.config.rabbitmq.port
        print "start listening on", self.host, "with port", self.port
        print "waiting for", key, "on exchange", exchange

        self.exchange = exchange
        self.routing_key = key
        print ("Connection established" if RabbitMQ.establishConnection(self.host, self.port) else "Failed to connect")

    def start(self):
        # RabbitMQ.declareExchange(self.channel, self.exchange, _type="topic")
        if hasattr(RabbitMQ, 'channel'):
            queue = RabbitMQ.channel.queue_declare()
            queue_name = queue.method.queue
            RabbitMQ.channel.queue_bind(exchange=self.exchange, queue=queue_name, routing_key=self.routing_key)
            RabbitMQ.channel.basic_consume(self.onMessage, no_ack=True)
            print "start conssuming ..."
            RabbitMQ.channel.start_consuming()

    def stop(self):
        RabbitMQ.channel.stop_consuming()

    def onMessage(self, ch, method, properties, body):
        # print ch, method, properties
        print method.routing_key
        print body

if __name__ == '__main__':
    # consumer = consumerDummy('annotated_data', 'Aarhus.Road.Parking.#')
    # consumer = consumerDummy('annotated_data', 'Aarhus.Road.Traffic.#')
    # consumer = consumerDummy('annotated_data', 'Aarhus.Road.Traffic.158324')
    # consumer = consumerDummy('aggregated_data', '#')
    # consumer = consumerDummy('quality', 'Aarhus.Road.Traffic.#')
    # consumer = consumerDummy('annotated_data', 'Brasov.Air.Pollution.#')
    # consumer = consumerDummy('annotated_data', 'Romania.Weather.#')
    consumer = ConsumerDummy('annotated_data', '#')
    # consumer = consumerDummy('wrapper_registration', '#')
    # consumer = consumerDummy('events', '#')
    consumer.start()