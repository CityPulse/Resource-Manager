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
        # self.host = self.config.rabbitmq.host
        # self.port = self.config.rabbitmq.port

        self.exchange = exchange
        self.routing_key = key
        rmq_host = str(self.config.rabbitmq.host)
        rmq_port = self.config.rabbitmq.port
        rmq_username = self.config.rabbitmq.username if "username" in self.config.rabbitmq else None
        rmq_password = self.config.rabbitmq.password if "password" in self.config.rabbitmq else None
        print "connecting with", rmq_username, "and", rmq_password

        if rmq_username:
            if rmq_password:
                print ("Connection established" if RabbitMQ.establishConnection(rmq_host, rmq_port, rmq_username, rmq_password) else "Failed to connect")
            else:
                print ("Connection established" if RabbitMQ.establishConnection(rmq_host, rmq_port, rmq_username) else "Failed to connect")
        else:
            print ("Connection established" if RabbitMQ.establishConnection(rmq_host, rmq_port) else "Failed to connect")

        print "start listening on", rmq_host, "with port", rmq_port
        print "waiting for", key, "on exchange", exchange

    def start(self):
        # RabbitMQ.declareExchange(self.channel, self.exchange, _type="topic")
        if hasattr(RabbitMQ, 'channel'):
            queue = RabbitMQ.channel.queue_declare(queue='consumer_dummy', auto_delete=True, arguments={'x-message-ttl': 600000})
            queue_name = queue.method.queue
            RabbitMQ.channel.queue_bind(exchange=self.exchange, queue=queue_name, routing_key=self.routing_key)
            RabbitMQ.channel.basic_consume(self.onMessage, no_ack=True)
            print "start consuming ..."
            RabbitMQ.channel.start_consuming()

    def stop(self):
        RabbitMQ.channel.stop_consuming()

    def onMessage(self, ch, method, properties, body):
        # print ch, method, properties
        print method.routing_key
        print body

if __name__ == '__main__':
    # consumer = ConsumerDummy('annotated_data', 'Aarhus.Road.Parking.#')
    consumer = ConsumerDummy('annotated_data', 'Aarhus.Road.Traffic.#')
    # consumer = ConsumerDummy('annotated_data', 'Aarhus.Road.Traffic.158324')
    # consumer = ConsumerDummy('aggregated_data', '#')
    # consumer = ConsumerDummy('quality', 'Aarhus.Road.Traffic.#')
    # consumer = ConsumerDummy('annotated_data', 'Brasov.Air.Pollution.#')
    # consumer = ConsumerDummy('annotated_data', 'Romania.Weather.#')
    # consumer = ConsumerDummy('annotated_data', '#')
    # consumer = ConsumerDummy('wrapper_registration', '#')
    # consumer = ConsumerDummy('events', '#')
    consumer.start()