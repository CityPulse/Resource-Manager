__author__ = 'Marten Fischer (m.fischer@hs-osnabrueck.de)'

from virtualisation.misc.jsonobject import JSONObject
import copy
import _strptime # A bug in Python, that may cause a AttributeError (http://stackoverflow.com/questions/2427240/thread-safe-equivalent-to-pythons-time-strptime)
import datetime
import uuid

class SensorDescription(JSONObject):
    def __init__(self, obj=None):
        super(SensorDescription, self).__init__(obj)

    def deepcopy(self):
        return SensorDescription(copy.deepcopy(self.__dict__["data"]))

    def __deepcopy__(self, memo):
        return SensorDescription(copy.deepcopy(self.__dict__["data"]))

    def test(self):

        # default projection system
        if not "location_epsg" in self.__dict__["data"]:
            self.__dict__["data"]["location_epsg"] = None

        # flag to avoid publishing observations on the messagebus
        if not "no_publish_messagebus" in self.__dict__["data"]:
            self.__dict__["data"]["no_publish_messagebus"] = False

        if not "uuid" in self.__dict__["data"]:
            if "fullSensorID" in self.__dict__["data"]:
                self.__dict__["data"]["uuid"] = str(uuid.uuid5(uuid.NAMESPACE_URL, self.fullSensorID))
            else:
                self.__dict__["data"]["uuid"] = str(uuid.uuid4())
        else:
            if isinstance(self.uuid, int):
                self.uuid = str(self.uuid)

        required = ["sensorName",  "author", "source", "sensorType", "sourceType", "sourceFormat", "information", "sensorID", "fullSensorID", "uuid", "location", "movementBuffer", "updateInterval", "fields", "messagebus", "namespace", "location_epsg"]
        for r in required:
            if not r in self.__dict__["data"]:
                raise Exception("invalid sensor description. Property " + r + " is required.")

        required = ["propertyName", "propertyURI", "dataType"]
        required_datatype = {"str": [], "int": ["min", "max"], "long": ["min", "max"], "float": ["min", "max"], "datetime.datetime": ["min", "format"], "enum": []}
        for f in self.fields:
            if not "aggregationMethod" in self.field[f]:
                self.field[f].aggregagationMethod = None
            if not "showOnCityDashboard" in self.field[f]:
                self.field[f].showOnCityDashboard = False
            for r in required:
                if r not in self.field[f]:
                    raise Exception("invalid sensor description. " + f + " requires field-property" + r + ".")
            # at this point we can be sure there is a 'dataType'
            # let's see if all required attributes for the dataType are present
            for r in required_datatype[self.field[f].dataType]:
                if r not in self.field[f]:
                    raise Exception("The attribute %s is required for dataType %s" % (r, self.field[f].dataType))

        valid_epsg = [None, 4326, 31700]
        if not self.location_epsg in valid_epsg:
            raise Exception("Invalid EPSG. Only " + ", ".join(valid_epsg) + " are supported.")

        # After a telco with Dan and Ioana we agreed to provide the descriptions of all fields also in an array
        # instead of a dictionary. This will allow them to use popular libraries such as GSON to parse the JSON
        # response. In addition each of the field-description in the list will get an attribute 'name', specifying
        # the fieldname.
        self.field_array = []
        for f in self.fields:
            field_description = self.field[f]
            field_description.name = f
            self.field_array.append(field_description)

    def isTimestampedStream(self):
        return "timestamp" in self.__dict__["data"] and "inField" in self.__dict__["data"]["timestamp"]

    def parseTimestamp(self, value):
        if self.timestamp.format == "UNIX5":
            if not isinstance(value, int):
                value = int(value)
            value = value / 1000
            return datetime.datetime.fromtimestamp(value)
        if self.timestamp.format == "UNIX":
            if not isinstance(value, int):
                value = int(value)
            return datetime.datetime.fromtimestamp(value)
        else:
            return datetime.datetime.strptime(value, self.timestamp.format)
