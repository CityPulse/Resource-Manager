import datetime

__author__ = 'Daniel Puschmann'


from virtualisation.misc.jsonobject import JSONObject
import copy

class EventDescription(JSONObject):

    def __init__(self, obj=None):
        super(EventDescription, self).__init__(obj)

    def deepcopy(self):
        return EventDescription(copy.deepcopy(self.__dict__["data"]))

    def __deepcopy__(self, memo):
        return EventDescription(copy.deepcopy(self.__dict__["data"]))

    def test(self):
        required = ["ceID", "ceType", "ceName", "ceTime", "ceCoordinate", "ceLevel", "ceWeight", "graphName", "location", "uuid"]

        for r in required:
            if not r in self.__dict__["data"]:
                raise Exception("Invalid event description. Property %s is required but missing" % r)

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