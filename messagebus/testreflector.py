from Queue import Queue
from virtualisation.misc.jsonobject import JSONObject as JOb
import os
from rabbitmq import RabbitMQ
from threading import Timer, Thread, Lock
import argparse

__author__ = 'Marten Fischer'


class Reflector(object):
    """
    This programm is only for development purposes. It re-sends annotated data received on the message bus. This way the
    update interval can be shortend even when using live data.
    """

    def __init__(self, exchange, key, seconds_delay, repetitions):
        self.config = JOb(file(os.path.join(os.path.dirname(__file__), "..", "virtualisation", "config.json"), "rb"))
        self.host = self.config.rabbitmq.host
        self.port = self.config.rabbitmq.port
        print "Start listening on", self.host, "with port", self.port
        print "Waiting for topic", key, "on exchange", exchange
        self.connection, self.channel = RabbitMQ.establishConnection(self.host, self.port)
        self.exchange = exchange
        self.routing_key = key
        RabbitMQ.declareExchange(self.channel, self.exchange, _type='topic')
        self.seconds_delay = seconds_delay
        self.repetitions = repetitions
        self.timer = None
        self.q = Queue()
        self.lock = Lock()

    def start(self):
        queue = self.channel.queue_declare()
        queue_name = queue.method.queue
        self.channel.queue_bind(exchange=self.exchange, queue=queue_name, routing_key=self.routing_key)
        self.channel.basic_consume(self.onMessage, no_ack=True)
        # RabbitMQ.sendMessage("Test", self.channel, "annotated_data", "Test.Message")
        self.channel.start_consuming()

    def stop(self):
        self.channel.stop_consuming()
        if self.timer.is_alive():
            self.timer.cancel()

    def onMessage(self, ch, method, properties, body):
        # print properties, method
        print '.',
        self.q.put((body, method.routing_key, self.repetitions), block=False)
        if not self.timer:
            self.timer = Timer(self.seconds_delay, self.process_queue)
            self.timer.start()

    def process_queue(self):
        # connection, channel = RabbitMQ.establishConnection(self.host, self.port)
        # RabbitMQ.declareExchange(channel, self.exchange, _type='topic')
        print
        print "processing", self.q.qsize(), "items ...",
        for i in range(0, self.q.qsize()):
            m, rk, rep = self.q.get()
            self.resend(self.channel, m, rk, rep)
        self.timer = Timer(self.seconds_delay, self.process_queue)
        self.timer.start()
        print 'ok'

    def resend(self, channel, message, routing_key, _repetitions):
        _repetitions -= 1
        # print _repetitions, self.exchange, routing_key
        try:
            if not channel.is_open:
                print "Exiting because channel is closed."
                return
            RabbitMQ.sendMessage(message, channel, self.exchange, routing_key)
        except Exception as e:
            print "failed to resend", routing_key, e
        if _repetitions > 0:
            self.q.put((message, routing_key, _repetitions), block=False)
        else:
            del message
            del routing_key
            del _repetitions


if __name__ == '__main__':

    exchange = 'annotated_data'
    # exchange = 'quality'
    # exchange = 'aggregated_data'
    # exchange = 'wrapper_registration'

    # topic = 'Aarhus.Road.Parking.#'
    topic = 'Aarhus.Road.Traffic.#'
    # topic = 'ABrasov.Air.Pollution.#'
    # topic = 'Romania.Weather.#'

    delay = 16  # seconds to resend
    repetitions = 4  # resend x time

    parser = argparse.ArgumentParser()
    parser.add_argument('-exchange', help="The exchange to listen on", dest='exchange', required=False)
    parser.add_argument('-topic', help="The topic to wait for", dest='topic', required=False)
    parser.add_argument('-delay', help="Number of seconds to wait until a message is re-sent", dest='delay', type=int, required=False)
    parser.add_argument('-repetitions', help="How often is a message re-sent. There is a delay of <DELAY> between two repetitions.", dest='repetitions', type=int, required=False)
    parser.set_defaults(exchange=exchange, topic=topic, delay=delay, repetitions=repetitions)
    args = parser.parse_args()

    consumer = Reflector(args.exchange, args.topic, args.delay, args.repetitions)
    Thread(target=consumer.start).start()
    raw_input("Hit ENTER to stop.\n")
    print "Stopping"
    consumer.stop()
