# coding=utf-8
import uuid
from virtualisation.clock.abstractclock import AbstractClock
from virtualisation.wrapper.abstractwrapper import AbstractComposedWrapper, AbstractWrapper
from virtualisation.sensordescription import SensorDescription
from virtualisation.wrapper.history.csvhistory import CSVHistoryReader
from virtualisation.wrapper.parser.csvparser import CSVParser
from virtualisation.wrapper.parser.jsonparser import JSONParser
from virtualisation.wrapper.connection.httpconnection import HttpPullConnection
from virtualisation.misc.log import Log

__author__ = 'Marten Fischer (m.fischer@hs-osnabrueck.de)'

_X = lambda x: x.replace(" ", "_")


"""
Not using a ComposedWrapper this time is on purpose, to test if a AbstractWrapper instance will work on its own.

Service response example:
[   {"id":158,
    "guid":"24c146ba-bad4-e111-9e49-005056a05270",
    "x":543153.95094,
    "y":465010.490411,
    "incidentid":"cdfd420b-712f-e511-be17-005056a05270",
    "i":"Spatii Verzi",
    "title":"Toaletare iarba si gard viu, Strada Lanii, Nr. 140",
    "createdon":"21/07/2015",
    "statecode":1
    "ticketnumber":"CAS-07445-W8V7F7"
    "description":"Solicita toaletare iarba la nr. 140."
    "indsoft_publiclyvisible":true
    "comments":"\u003cbr /\u003e\u003ci style\u003d\u0027color:blue\u0027\u003eRezolvat la data: 28/07/2015\u003cbr /\u003e operatiunile se executa conform graficelor\u003cbr /\u003e\u003c/i\u003e"
    "incidentState":"SOLVED"
    "timestamp":1438176297218}]
"""

incident_types = ["0f75c5c1-b3f2-e111-a5d4-005056a05270",
                "92a136cc-b3f2-e111-a5d4-005056a05270",
                "8796aff1-b3f2-e111-a5d4-005056a05270",
                "e3219619-c3d4-e111-9e49-005056a05270",
                "c32e4f0a-c3d4-e111-9e49-005056a05270",
                "03eaeadd-c1d4-e111-9e49-005056a05270",
                "a37d1750-c2d4-e111-9e49-005056a05270",
                "03a169f2-c2d4-e111-9e49-005056a05270",
                "43798fff-c2d4-e111-9e49-005056a05270",
                "24c146ba-bad4-e111-9e49-005056a05270",
                "164aefaa-1403-e211-85da-005056a05270",
                "9bf5c28b-f00d-e211-8e92-005056a05270"
]

incident_topics = [
    "Animals",
    "Water and sewage",
    "Missing sewerage cover",
    "Construction",
    "road pit",
    "lighting",
    "Urban furniture: e.g park bench",
    "Sanitation",
    "Road signs",
    "Green areas",
    "pole / pillar",
    "Transport"
]

def makeSource(incident_type):
    return "http://www.bamct.siemens.ro:9000/brasovDataCollector/indidentsView?incident_type=%s" % incident_type

class IncidentConnection(HttpPullConnection):
    def __init__(self, wrapper):
        super(IncidentConnection, self).__init__(wrapper)

    def next(self):
        data = super(IncidentConnection, self).next()
        if not data or data.strip() == "Measurement not available":
            return None
        else:
            return data

class BrasovIncidentWrapper(AbstractWrapper):
    def __init__(self, number, incident_type, incident_topic):
        super(BrasovIncidentWrapper, self).__init__()
        self.number = number
        self.sensordescription = SensorDescription()
        self.sensordescription.namespace = "http://ict-citypulse.eu/"

        self.sensordescription.sensorID = "brasov_incidents_" + _X(incident_topic)
        self.sensordescription.sensorName = self.sensordescription.sensorID
        self.sensordescription.fullSensorID = self.sensordescription.namespace + "brasov/" + self.sensordescription.sensorID
        self.sensordescription.location = "n/a"

        self.sensordescription.source = makeSource(incident_type)
        self.sensordescription.author = "cityofbrasov"
        self.sensordescription.sensorType = "Brasov_Incidents"
        self.sensordescription.graphName = "brasov_incidents#"
        self.sensordescription.sourceType = "pull_http"
        self.sensordescription.sourceFormat = "application/json"
        self.sensordescription.information = "List of incidents reported by citizens starting from November 2014 about " + incident_topic
        self.sensordescription.cityName = "Brasov"
        self.sensordescription.countryName = "Romania"
        self.sensordescription.movementBuffer = 0
        self.sensordescription.maxLatency = 2
        self.sensordescription.updateInterval = 60 * 60
        self.sensordescription.messagebus.routingKey = "Brasov.Incidents." + _X(incident_topic)
        self.sensordescription.fields = ["id",
                                         "comments",
                                         "createdon",
                                         "description",
                                         "guid",
                                         "incidentState",
                                         "incidentid",
                                         "indsoft_publiclyvisible",
                                         "statecode",
                                         "ticketnumber",
                                         "timestamp",
                                         "title",
                                         "x",
                                         "y"
                                         ]

        self.sensordescription.field.id.propertyName = "Property"
        self.sensordescription.field.id.propertyPrefix = "ssn"
        self.sensordescription.field.id.propertyURI = self.sensordescription.namespace + "brasov/incidents#ID"
        self.sensordescription.field.id.min = 0
        self.sensordescription.field.id.max = 99999999
        self.sensordescription.field.id.dataType = "int"

        self.sensordescription.field.comments.propertyName = "Property"
        self.sensordescription.field.comments.propertyPrefix = "ssn"
        self.sensordescription.field.comments.propertyURI = self.sensordescription.namespace + "brasov/incidents#Comments"
        self.sensordescription.field.comments.min = ""
        self.sensordescription.field.comments.max = ""
        self.sensordescription.field.comments.dataType = "str"

        self.sensordescription.field.createdon.propertyName = "MeasuredTime"
        self.sensordescription.field.createdon.propertyURI = self.sensordescription.namespace + "brasov/incidents#CreatedOn"
        self.sensordescription.field.createdon.unit = self.sensordescription.namespace + "unit:time"
        self.sensordescription.field.createdon.min = "2012-01-01T00:00:00"
        self.sensordescription.field.createdon.max = "2099-12-31T23:59:59"
        self.sensordescription.field.createdon.dataType = "datetime.datetime"
        self.sensordescription.field.createdon.format = "%d/%m/%Y"

        self.sensordescription.field.description.propertyName = "Property"
        self.sensordescription.field.description.propertyPrefix = "ssn"
        self.sensordescription.field.description.propertyURI = self.sensordescription.namespace + "brasov/incidents#Description"
        self.sensordescription.field.description.min = ""
        self.sensordescription.field.description.max = ""
        self.sensordescription.field.description.dataType = "str"

        self.sensordescription.field.guid.propertyName = "Property"
        self.sensordescription.field.guid.propertyPrefix = "ssn"
        self.sensordescription.field.guid.propertyURI = self.sensordescription.namespace + "brasov/incidents#IncidentType"
        self.sensordescription.field.guid.min = ""
        self.sensordescription.field.guid.max = ""
        self.sensordescription.field.guid.dataType = "str" #enum

        self.sensordescription.field.i.propertyName = "Property"
        self.sensordescription.field.i.propertyPrefix = "ssn"
        self.sensordescription.field.i.propertyURI = self.sensordescription.namespace + "brasov/incidents#IncidentCategory"
        self.sensordescription.field.i.min = ""
        self.sensordescription.field.i.max = ""
        self.sensordescription.field.i.dataType = "str"

        self.sensordescription.field.incidentState.propertyName = "Property"
        self.sensordescription.field.incidentState.propertyPrefix = "ssn"
        self.sensordescription.field.incidentState.propertyURI = self.sensordescription.namespace + "brasov/incidents#State"
        self.sensordescription.field.incidentState.min = 0
        self.sensordescription.field.incidentState.max = 2
        self.sensordescription.field.incidentState.dataType = "int"

        self.sensordescription.field.incidentid.propertyName = "Property"
        self.sensordescription.field.incidentid.propertyPrefix = "ssn"
        self.sensordescription.field.incidentid.propertyURI = self.sensordescription.namespace + "brasov/incidents#IncedentID"
        self.sensordescription.field.incidentid.min = ""
        self.sensordescription.field.incidentid.max = ""
        self.sensordescription.field.incidentid.dataType = "str"

        self.sensordescription.field.indsoft_publiclyvisible.propertyName = "Property"
        self.sensordescription.field.indsoft_publiclyvisible.propertyPrefix = "ssn"
        self.sensordescription.field.indsoft_publiclyvisible.propertyURI = self.sensordescription.namespace + "brasov/incidents#Public"
        self.sensordescription.field.indsoft_publiclyvisible.min = 0
        self.sensordescription.field.indsoft_publiclyvisible.max = 1
        self.sensordescription.field.indsoft_publiclyvisible.dataType = "int"

        self.sensordescription.field.statecode.propertyName = "Property"
        self.sensordescription.field.statecode.propertyPrefix = "ssn"
        self.sensordescription.field.statecode.propertyURI = self.sensordescription.namespace + "brasov/incidents#StateCode"
        self.sensordescription.field.statecode.min = 0
        self.sensordescription.field.statecode.max = 10
        self.sensordescription.field.statecode.dataType = "int"

        self.sensordescription.field.ticketnumber.propertyName = "Property"
        self.sensordescription.field.ticketnumber.propertyPrefix = "ssn"
        self.sensordescription.field.ticketnumber.propertyURI = self.sensordescription.namespace + "brasov/incidents#TicketNumber"
        self.sensordescription.field.ticketnumber.min = ""
        self.sensordescription.field.ticketnumber.max = ""
        self.sensordescription.field.ticketnumber.dataType = "str"

        self.sensordescription.field.timestamp.propertyName = "MeasuredTime"
        self.sensordescription.field.timestamp.propertyURI = self.sensordescription.namespace + "city#MeasuredTime"
        self.sensordescription.field.timestamp.unit = self.sensordescription.namespace + "unit:time"
        self.sensordescription.field.timestamp.min = "2012-01-01T00:00:00"
        self.sensordescription.field.timestamp.max = "2099-12-31T23:59:59"
        self.sensordescription.field.timestamp.dataType = "datetime.datetime"
        self.sensordescription.field.timestamp.format = "UNIX5"
        self.sensordescription.field.timestamp.skip_annotation = True

        self.sensordescription.field.title.propertyName = "Property"
        self.sensordescription.field.title.propertyPrefix = "ssn"
        self.sensordescription.field.title.propertyURI = self.sensordescription.namespace + "brasov/incidents#Title"
        self.sensordescription.field.title.min = ""
        self.sensordescription.field.title.max = ""
        self.sensordescription.field.title.dataType = "str"

        self.sensordescription.field.x.propertyName = "Property"
        self.sensordescription.field.x.propertyPrefix = "ssn"
        self.sensordescription.field.x.propertyURI = self.sensordescription.namespace + "brasov/incidents#LocationX"
        self.sensordescription.field.x.min = ""
        self.sensordescription.field.x.max = ""
        self.sensordescription.field.x.dataType = "float"

        self.sensordescription.field.y.propertyName = "Property"
        self.sensordescription.field.y.propertyPrefix = "ssn"
        self.sensordescription.field.y.propertyURI = self.sensordescription.namespace + "brasov/incidents#LocationY"
        self.sensordescription.field.y.min = ""
        self.sensordescription.field.y.max = ""
        self.sensordescription.field.y.dataType = "float"

        self.sensordescription.timestamp.inField = "timestamp"
        self.sensordescription.timestamp.format = "UNIX5"

        self.parser = JSONParser(self)
        self.connection = IncidentConnection(self)

    def getSensorDescription(self):
        return self.sensordescription

    def setReplayMode(self, mode):
        super(BrasovIncidentWrapper, self).setReplayMode(mode)
        # fieldnames of service: "id", "comments", "createdon", "description", "guid", "incidentState", "incidentid", "indsoft_publiclyvisible", "statecode", "ticketnumber", "timestamp", "title", "x", "y"
        fieldnames = ["id", "comments", "createdon", "description", "guid", "i", "incidentState", "incidentid", "indsoft_publiclyvisible", "statecode", "ticketnumber", "timestamp", "title", "x", "y"]
        try:
            fobj = AbstractWrapper.getFileObject(__file__, "incidents%d.csv" % self.number, "rU")
            self.historyreader = CSVHistoryReader(self, fobj, delimiter=',')
            self.historyreader.multiple_observations = False
            self.historyparser = CSVParser(self, fieldnames)

        except Exception as e:
            Log.e("setReplayMode in Brasov Incident Wrapper", self.number, e)
            self.historyreader = None

class BrasovIncidentWrapper0(BrasovIncidentWrapper):
    def __init__(self):
        super(BrasovIncidentWrapper0, self).__init__(0, incident_types[0], incident_topics[0])

class BrasovIncidentWrapper1(BrasovIncidentWrapper):
    def __init__(self):
        super(BrasovIncidentWrapper1, self).__init__(1, incident_types[1], incident_topics[1])

class BrasovIncidentWrapper2(BrasovIncidentWrapper):
    def __init__(self):
        super(BrasovIncidentWrapper2, self).__init__(2, incident_types[2], incident_topics[2])

class BrasovIncidentWrapper3(BrasovIncidentWrapper):
    def __init__(self):
        super(BrasovIncidentWrapper3, self).__init__(3, incident_types[3], incident_topics[3])

class BrasovIncidentWrapper4(BrasovIncidentWrapper):
    def __init__(self):
        super(BrasovIncidentWrapper4, self).__init__(4, incident_types[4], incident_topics[4])

class BrasovIncidentWrapper5(BrasovIncidentWrapper):
    def __init__(self):
        super(BrasovIncidentWrapper5, self).__init__(5, incident_types[5], incident_topics[5])

class BrasovIncidentWrapper6(BrasovIncidentWrapper):
    def __init__(self):
        super(BrasovIncidentWrapper6, self).__init__(6, incident_types[6], incident_topics[6])

class BrasovIncidentWrapper7(BrasovIncidentWrapper):
    def __init__(self):
        super(BrasovIncidentWrapper7, self).__init__(7, incident_types[7], incident_topics[7])

class BrasovIncidentWrapper8(BrasovIncidentWrapper):
    def __init__(self):
        super(BrasovIncidentWrapper8, self).__init__(8, incident_types[8], incident_topics[8])

class BrasovIncidentWrapper9(BrasovIncidentWrapper):
    def __init__(self):
        super(BrasovIncidentWrapper9, self).__init__(9, incident_types[9], incident_topics[9])

class BrasovIncidentWrapper10(BrasovIncidentWrapper):
    def __init__(self):
        super(BrasovIncidentWrapper10, self).__init__(10, incident_types[10], incident_topics[10])

class BrasovIncidentWrapper11(BrasovIncidentWrapper):
    def __init__(self):
        super(BrasovIncidentWrapper11, self).__init__(11, incident_types[11], incident_topics[11])
