__author__ = 'Daniel Puschmann'

from virtualisation.events.genericeventwrapper import GenericEventWrapper
from virtualisation.events.eventdescription import EventDescription
from virtualisation.misc.jsonobject import JSONObject

"""
    private String ceID = UUID.randomUUID().toString();
	private String ceType = "";
	private String ceName = "";
	private long ceTime;
	private Coordinate ceCoordinate;
	private int ceLevel;
"""

class AarhusTrafficEventWrapper():

    def __init__(self):
        eventdescription = EventDescription()
        eventdescription.namespace = "http://ict-citypulse.eu/"
        eventdescription.graphName = "aarhus_road_traffic_event#"
        eventdescription.author = "cityofaarhus"

        eventdescription.timestamp.inField = "ceTime"
        eventdescription.timestamp.format = "UNIX5"

        # added after telco with Dan
        eventdescription.uuid = "0815-0815-0815"
        eventdescription.location = "POINT (56.45 10.11)"

        # optional?
        eventdescription.source = "TODO (Possibly messsage bus grounding?)"
        eventdescription.eventType = "Aarhus_Road_Traffic_Event"
        eventdescription.sourceType = "message_bus"
        eventdescription.sourceFormat = "application/json"
        eventdescription.information = "Traffic event for the City of Aarhus"

        """@Daniel P: Now I had time to look a bit closer into your code. I would suggest to make just an example
        EventDescription to show Dan what we need and to test the annotation part. You will probably need a pseudo
        EventGenerator for that.
        Later, the ResourceManagement API will receive new EventDescriptions and instanciate EventWrapper
        (or best case we can reuse one instance). There is no need to make the metadata file nor to instanciate an
        EventWrapper for each REPORT_ID."""

        self.eventDescription = eventdescription

    def getEventDescription(self):
        return self.eventDescription

if __name__ == "__main__":
    atew = AarhusTrafficEventWrapper()
    from virtualisation.annotation.genericannotation import GenericAnnotation
    annotator = GenericAnnotation()
    eventData = JSONObject()
    eventData.ceID = 123456
    eventData.ceType = "traffic"
    eventData.ceName = "traffic jam"
    eventData.ceTime = 1438591234000L
    eventData.ceCoordinate = "(56.12 10.13)"
    eventData.ceLevel = 1

    print "Incoming event data", eventData.dumps()
    print

    g = annotator.annotateEvent(eventData, atew.getEventDescription())
    print "Resulting graph", g.serialize(format='n3')
    print

    print atew.getEventDescription().dumps()