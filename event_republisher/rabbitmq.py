import pika
import pika.exceptions
import time
import logging
logging.basicConfig()
MessageBusConnectionError = pika.exceptions.AMQPConnectionError

class RabbitMQ(object):
    """
    Modified version of the RabbitMQ class. This class/file is intented for the event-republish-service.
    TODO: try to reuse the classical RabbitMQ class.
    """
    exchangetopics = []
    exchanges = ["repeatable_events", "events"]
    exchange_repeatable_events = exchanges[0]
    exchange_events = exchanges[1]

    reconnection_delay = 10

    @classmethod
    def establishConnection(cls, host, port, username='guest', password='guest'):
        RabbitMQ.connection_params_host = host
        RabbitMQ.connection_params_port = port
        RabbitMQ.connection_params_username = username
        RabbitMQ.connection_params_password = password
        return RabbitMQ.__connect()

    # use one exchange for each data set
    # use routing key to send to the right subscribers
    @classmethod
    def sendMessage(cls, msg, exchange, routing_key, retry=0):
        try:
            RabbitMQ.sendChannel.basic_publish(exchange=exchange, routing_key=routing_key, body=msg)
        except pika.exceptions.ConnectionClosed:
            if retry < 10:
                print "RabbitMQ connection closed"
                time.sleep(RabbitMQ.reconnection_delay)
                print "reconnecting to message bus", retry
                try:
                    if RabbitMQ.__connect():
                        RabbitMQ.sendChannel.basic_publish(exchange=exchange, routing_key=routing_key, body=msg)
                    else:
                        new_retry = retry + 1
                        RabbitMQ.sendMessage(msg, exchange, routing_key, new_retry)
                except:
                    print "Failed to reconnect to RabbitMQ"

    @classmethod
    def declareExchange(cls, channel, exchange, _type='topic'):
        global exchangetopics
        # Checks if exchange exists and declares the exchange in case it has not been declared before
        if exchange not in RabbitMQ.exchangetopics:
            channel.exchange_declare(exchange=exchange, exchange_type=_type, auto_delete=False, nowait=False)
            channel.queue_declare(queue='q_' + exchange, passive=False, durable=False, exclusive=False, auto_delete=False, nowait=False, arguments={'x-message-ttl': 600000})
            channel.queue_bind(queue='q_' + exchange, exchange=exchange, routing_key='#')
            #exchangetopics.append(exchange)

    @classmethod
    def registerExchanges(cls, channel):
        for ex in RabbitMQ.exchanges:
            try:
                RabbitMQ.declareExchange(channel, ex, _type="topic")
            except Exception as e:
                print ('Exchange %s could not be declared: %s' % (ex, e.message))
                print ('Exception:', str(e))

    @classmethod
    def deleteExchange(cls, channel, exchange):
        channel.exchange_delete(exchange=exchange, nowait=True)
        if exchange in RabbitMQ.exchangetopics:
            del RabbitMQ.exchangetopics[RabbitMQ.exchangetopics.index(exchange)]

    @classmethod
    def __connect(cls):
        try:
            connection_attempts = 1
            retry_delay = 1  # in seconds
            socket_timeout = 1
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
            RabbitMQ.registerExchanges(RabbitMQ.channel)


            if RabbitMQ.connection_params_host == 'localhost' and RabbitMQ.connection_params_port is not None:
                connection = pika.BlockingConnection(pika.ConnectionParameters(host=RabbitMQ.connection_params_host, port=RabbitMQ.connection_params_port, heartbeat_interval=heartbeat_interval, connection_attempts=connection_attempts, retry_delay=retry_delay, socket_timeout=socket_timeout))
            elif RabbitMQ.connection_params_host == 'localhost':
                connection = pika.BlockingConnection(pika.ConnectionParameters(host=RabbitMQ.connection_params_host, heartbeat_interval=heartbeat_interval, connection_attempts=connection_attempts, retry_delay=retry_delay, socket_timeout=socket_timeout))
            else:
                credentials = pika.PlainCredentials(RabbitMQ.connection_params_username, RabbitMQ.connection_params_password)
                connection = pika.BlockingConnection(
                    pika.ConnectionParameters(host=RabbitMQ.connection_params_host, heartbeat_interval=heartbeat_interval, port=RabbitMQ.connection_params_port, credentials=credentials, connection_attempts=connection_attempts, retry_delay=retry_delay, socket_timeout=socket_timeout))

            RabbitMQ.sendConnection = connection
            RabbitMQ.sendChannel = connection.channel()
            RabbitMQ.registerExchanges(RabbitMQ.sendChannel)
            return True
        except:
            return False



