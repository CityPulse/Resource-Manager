import pika
import pika.exceptions
import time
from virtualisation.misc.log import Log as L
__author__ = 'Daniel Puschmann'

MessageBusConnectionError = pika.exceptions.AMQPConnectionError

class RabbitMQ(object):
    exchangetopics = []
    exchanges = ["annotated_data", "quality", "event", "annotated_event", "aggregated_data", "wrapper_registration"]
    exchange_annotated_data = exchanges[0]
    exchange_quality = exchanges[1]
    exchange_event = exchanges[2]
    exchange_annotated_event = exchanges[3]
    exchange_aggregated_data = exchanges[4]
    exchange_wrapper_registration = exchanges[5]

    reconnection_delay = 10

    @classmethod
    def establishConnection(cls, host, port, username='guest', password='guest'):
        RabbitMQ.connection_params_host = host
        RabbitMQ.connection_params_port = port
        RabbitMQ.connection_params_username = username
        RabbitMQ.connection_params_password = password
        return RabbitMQ.__connect()
        #
        # connection_attempts = 1
        # retry_delay = 1  # in seconds
        # socket_timeout = 5
        # heartbeat_interval = 600
        #
        # if host == 'localhost' and port is not None:
        #     connection = pika.BlockingConnection(pika.ConnectionParameters(host=host, port=port, heartbeat_interval=heartbeat_interval, connection_attempts=connection_attempts, retry_delay=retry_delay, socket_timeout=socket_timeout))
        # elif host == 'localhost':
        #     connection = pika.BlockingConnection(pika.ConnectionParameters(host=host, heartbeat_interval=heartbeat_interval, connection_attempts=connection_attempts, retry_delay=retry_delay, socket_timeout=socket_timeout))
        # else:
        #     credentials = pika.PlainCredentials(username, password)
        #     connection = pika.BlockingConnection(
        #         pika.ConnectionParameters(host=host, heartbeat_interval=heartbeat_interval, port=port, credentials=credentials, connection_attempts=connection_attempts, retry_delay=retry_delay, socket_timeout=socket_timeout))
        # # connection.add_on_close_callback(RabbitMQ.__reconnectMessageBus)
        # # connection.add_on_open_error_callback(RabbitMQ.__connectionOpenError)
        # RabbitMQ.connection = connection
        # channel = connection.channel()
        #
        #
        # return connection, channel

    # use one exchange for each data set
    # use routing key to send to the right subscribers
    @classmethod
    def sendMessage(cls, msg, exchange, routing_key, retry=0):
        try:
            RabbitMQ.channel.basic_publish(exchange=exchange, routing_key=routing_key, body=msg)
        except pika.exceptions.ConnectionClosed:
            if retry < 10:
                print "RabbitMQ connection closed"
                time.sleep(RabbitMQ.reconnection_delay)
                print "reconnecting to message bus", retry
                try:
                    if RabbitMQ.__connect():
                        RabbitMQ.channel.basic_publish(exchange=exchange, routing_key=routing_key, body=msg)
                    else:
                        new_retry = retry + 1
                        RabbitMQ.sendMessage(msg, exchange, routing_key, new_retry)
                except:
                    print "Failed to reconnect to RabbitMQ"

    @classmethod
    def declareExchange(cls, exchange, _type='direct'):
        # Checks if exchange exists and declares the exchange in case it has not been declared before
        if exchange not in RabbitMQ.exchangetopics:
            RabbitMQ.channel.exchange_declare(exchange=exchange, exchange_type=_type, auto_delete=False, nowait=False)
            RabbitMQ.channel.queue_declare(queue='q_' + exchange, passive=False, durable=False, exclusive=False, auto_delete=False, nowait=False, arguments={'x-message-ttl': 600000})
            RabbitMQ.channel.queue_bind(queue='q_' + exchange, exchange=exchange, routing_key='#')
            RabbitMQ.exchangetopics.append(exchange)

    @classmethod
    def registerExchanges(cls):
        try:
            for ex in RabbitMQ.exchanges:
                RabbitMQ.declareExchange(ex, _type="topic")
        except Exception as e:
            L.e('Exchange could not be declared: %s' % e.message)

    @classmethod
    def deleteExchange(cls, exchange):
        RabbitMQ.channel.exchange_delete(exchange=exchange, nowait=True)
        if exchange in RabbitMQ.exchangetopics:
            del RabbitMQ.exchangetopics[RabbitMQ.exchangetopics.index(exchange)]

    @classmethod
    def __connect(cls):
        try:
            connection_attempts = 1
            retry_delay = 1  # in seconds
            socket_timeout = 5
            heartbeat_interval = 600

            if RabbitMQ.connection_params_host == 'localhost' and RabbitMQ.connection_params_port is not None:
                connection = pika.BlockingConnection(pika.ConnectionParameters(host=RabbitMQ.connection_params_host, port=RabbitMQ.connection_params_port, heartbeat_interval=heartbeat_interval, connection_attempts=connection_attempts, retry_delay=retry_delay, socket_timeout=socket_timeout))
            elif RabbitMQ.connection_params_host == 'localhost':
                connection = pika.BlockingConnection(pika.ConnectionParameters(host=RabbitMQ.connection_params_host, heartbeat_interval=heartbeat_interval, connection_attempts=connection_attempts, retry_delay=retry_delay, socket_timeout=socket_timeout))
            else:
                credentials = pika.PlainCredentials(RabbitMQ.connection_params_username, RabbitMQ.connection_params_password)
                connection = pika.BlockingConnection(
                    pika.ConnectionParameters(host=RabbitMQ.connection_params_host, heartbeat_interval=heartbeat_interval, port=RabbitMQ.connection_params_port, credentials=credentials, connection_attempts=connection_attempts, retry_delay=retry_delay, socket_timeout=socket_timeout))

            RabbitMQ.connection = connection
            RabbitMQ.channel = connection.channel()
            RabbitMQ.registerExchanges()
            return True
        except:
            return False
