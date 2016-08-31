#!/bin/python

__author__ = "Marten Fischer <m.fischer@hs-osnabrueck.de>"

"""
This script receives events on a specific exchange on the MessageBus and republishes them on the 'standard' events exchange in a given interval.
The idea is that mobile devices may report an event only once. Components and other consumers on the MessageBus, which where not active at that
time, would miss it. This script avoids that. The event is as long republished until an other event with identical type and source but with level
0 is received.
"""

import rdflib
import threading
import time
import datetime
import json
import os.path
from rabbitmq import RabbitMQ

### CONFIG START

# specify the MessageBus Exchange where repeatable events shall be received
REPEATABLE_EVENTS_EXCHANGE = RabbitMQ.exchange_repeatable_events #RabbitMQ.exchange_events

# specifiy the MessageBus Exchange where the events will be republished on
EVENTS_EXCHANGE = RabbitMQ.exchange_events

# number of seconds before received events will be republished in the message bus
REPUBLISH_INTERVAL = 60

### CONFIG END

time_format = "%Y-%m-%dT%H:%M:%S.%f"
print_time = lambda time_object: datetime.datetime.strftime(time_object, time_format)

event_buffer = {}
stop_thread = False

class Config(object):
	"""mini config class"""
	def __init__(self):
		f = open(os.path.join(os.path.dirname(__file__), "..", "virtualisation", "config.json"), "rb")
		j = json.load(f)
		self.host = j["rabbitmq"]["host"]
		self.port = j["rabbitmq"]["port"]
		self.username = j["rabbitmq"]["username"] if "username" in j["rabbitmq"] else None
		self.password = j["rabbitmq"]["password"] if "password" in j["rabbitmq"] else None

	def __repr__(self):
		return ", ".join([self.host, str(self.port), str(self.username), str(self.password)])

def republish_thread():
	while not stop_thread:
		time.sleep(REPUBLISH_INTERVAL)
		if stop_thread:
			break
		for _id in event_buffer:
			evt, rk = event_buffer[_id]
			evt.update_time()
			print"republishing event", evt, "on routing key", rk
			# republish on the message bus
			RabbitMQ.sendMessage(evt.n3(), EVENTS_EXCHANGE, rk)
		print "event buffer length", len(event_buffer)

class RepeatableEvent(object):
	def __init__(self, graph_n3, event_id):
		self.g = rdflib.Graph()
		self.g.parse(data=graph_n3, format='n3')
		self.event_type = self.find_event_type()
		info = self.inspect_event(self.g)
		self.event_id, self.lvl = RepeatableEvent.get_id_lvl(info)
		self.event_id = event_id

	def __repr__(self):
		return self.event_id + "@" + self.lvl

	def find_event_type(self):
		for stmt in self.g.subject_objects(rdflib.URIRef("http://www.w3.org/1999/02/22-rdf-syntax-ns#type")):
			if stmt[0].startswith("http://"):
				return str(stmt[1])

	def inspect_event(self, evt):
		lvl = None
		source = None
		_type = None

		q = "select ?s ?o WHERE {?s sao:hasLevel ?o}"
		qres = evt.query(q)
		for _qres in qres:
			_, lvl = _qres

		q = "select ?s ?o WHERE {?s ec:hasSource ?o}"
		qres = evt.query(q)
		for _qres in qres:
			_, source = _qres

		q = "select ?s ?o WHERE {?s sao:hasType ?o}"
		qres = evt.query(q)
		for _qres in qres:
			_, _type = _qres

		q = "select ?s ?o WHERE {?s a <" + str(self.event_type) + "> }"
		# print q
		self.myself = "-"
		qres = evt.query(q)
		for _qres in qres:
			# print "subject %s %s" % _qres
			self.myself, _ = _qres

		t = (lvl, source, _type)
		t = map(lambda x: str(x), t)
		return t

	@classmethod
	def get_id_lvl(cls, evt_details):
		lvl, source, _type = evt_details
		return ''.join([_type, '@', source]), lvl

	def update_time(self):
		"""Updates the timestamp in a RDF event graph"""
		n = rdflib.Namespace("http://purl.org/NET/c4dm/timeline.owl#")
		nt = rdflib.Literal(print_time(datetime.datetime.now()), datatype=rdflib.XSD.dateTime)
		self.g.set( [self.myself, n.time, nt] )
		self.g.commit()

	def n3(self):
		return self.g.serialize(format='n3')

class MessageBusConsumer(object):
    """Listener for new events on the message bus."""

    def __init__(self, exchange, key):
    	c = Config()

        self.exchange = exchange
        self.routing_key = key
        rmq_host = str(c.host)
        rmq_port = c.port
        rmq_username = c.username
        rmq_password = c.password
        print "connecting with username", rmq_username, "and password", rmq_password

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
        if hasattr(RabbitMQ, 'channel'):
            queue = RabbitMQ.channel.queue_declare()
            queue_name = queue.method.queue
            RabbitMQ.channel.queue_bind(exchange=self.exchange, queue=queue_name, routing_key=self.routing_key)
            RabbitMQ.channel.basic_consume(self.onMessage, no_ack=True)
            # register Exchange and Queue for repeatable events
            RabbitMQ.registerExchanges()
            print "start consuming ..."
            RabbitMQ.channel.start_consuming()
        else:
        	print "Can not start the MessageBusConsumer. Not connected."

    def stop(self):
        RabbitMQ.channel.stop_consuming()

    def onMessage(self, ch, method, properties, body):
        # print method.routing_key
        evt_received(body, method.routing_key)

def main():
	global stop_thread
	# start thread to republish received events until one with level 0 was received
	threading.Thread(target=republish_thread).start()

	# start listening on the message bus for new 'repeatable' events
	mbc = MessageBusConsumer(REPEATABLE_EVENTS_EXCHANGE, "#")
	threading.Thread(target=mbc.start).start()

	raw_input("Press ENTER to stop.\n")
	print "stoping threads...",
	stop_thread = True
	mbc.stop()
	print "done"


def evt_received(evt, routing_key):
	re = RepeatableEvent(evt, routing_key)
	if re.lvl == "0":
		if re.event_id in event_buffer:
			# remove the event from the buffer
			del event_buffer[re.event_id]
	else:
		# add the event to the buffer
		event_buffer[re.event_id] = (re, routing_key)

	# print re.n3()

if __name__ == '__main__':
	main()

	#TODO remove test for processing events
# 	td = """@prefix geo:   <http://www.w3.org/2003/01/geo/wgs84_pos#> .
# @prefix sao:   <http://purl.oclc.org/NET/UNIS/sao/sao#> .
# @prefix tl:    <http://purl.org/NET/c4dm/timeline.owl#> .
# @prefix xsd:   <http://www.w3.org/2001/XMLSchema#> .
# @prefix prov:  <http://www.w3.org/ns/prov#> .
# @prefix ec:    <http://purl.oclc.org/NET/UNIS/sao/ec#> .
# sao:4d2aebf3-eb0d-4cb2-9837-9f408017af12         a                ec:PublicParking ;
#         ec:hasSource     "SENSOR_0816d088-3af8-540e-b89b-d99ac63fa886" ;
#         sao:hasLevel     "2"^^xsd:long ;
#         sao:hasLocation  [ a        geo:Instant ;
#                            geo:lat  "56.15"^^xsd:double ;
#                            geo:lon  "10.216667"^^xsd:double
#                          ] ;
#         sao:hasType      ec:TransportationEvent ;
#         tl:time          "2016-08-30T06:57:55.911Z"^^xsd:dateTime .
# """
# 	re = RepeatableEvent(td, "none")
# 	print re.find_event_type(td)

# 	td2 = """
# 	@prefix geo:   <http://www.w3.org/2003/01/geo/wgs84_pos#> .
# @prefix sao:   <http://purl.oclc.org/NET/UNIS/sao/sao#> .
# @prefix tl:    <http://purl.org/NET/c4dm/timeline.owl#> .
# @prefix xsd:   <http://www.w3.org/2001/XMLSchema#> .
# @prefix prov:  <http://www.w3.org/ns/prov#> .
# @prefix ec:    <http://purl.oclc.org/NET/UNIS/sao/ec#> .

# sao:4d2aebf3-eb0d-4cb2-9837-9f408017af12
#         a                ec:PublicParking ;
#         ec:hasSource     "SENSOR_0816d088-3af8-540e-b89b-d99ac63fa886" ;
#         sao:hasLevel     "0"^^xsd:long ;
#         sao:hasLocation  [ a        geo:Instant ;
#                            geo:lat  "56.15"^^xsd:double ;
#                            geo:lon  "10.216667"^^xsd:double
#                          ] ;
#         sao:hasType      ec:TransportationEvent ;
#         tl:time          "2016-08-30T06:57:55.911Z"^^xsd:dateTime .
# """

# 	evt_received(td)
# 	raw_input("enter to continue")
# 	evt_received(td2)
	# raw_input("enter to continue")
	# stop_thread = True
