
from Quality.AtomicComputation.reputationsystem.qoimetric import QoIMetric
from Quality.AtomicComputation.reputationsystem.rewardpunishment import RewardAndPunishment
from virtualisation.misc.jsonobject import JSONObject
from virtualisation.misc.log import Log as L


class Completeness(QoIMetric):
    """docstring for Completeness"""

    def __init__(self):
        QoIMetric.__init__(self, "Completeness")
        self.goal = None
        self.rewardAndPunishment = RewardAndPunishment(5)
        self.updatecounter = 1
        self.unit = "http://purl.oclc.org/NET/muo/ucum/physical-quality/number"

    def update(self, data):
        # special case when no fields are in data
        # (fault recovery is not ready yet)
        if len(data.fields) == 0:
            self.rewardAndPunishment.update(False)
            self.absoluteValue = float("inf")
            self.ratedValue = self.rewardAndPunishment.value()
            return



        # look for expected fields in sensor description, look only for non optional fields
        fields = self.repsys.description.fields
        fields = [x for x in fields if not self.repsys.description.field[x].optional]
        
        
        receivedFields = data.fields

        # check if expected and received identical, how to handle received fields with no values?
        nrOfMissingFields = 0
        missingFields = set()
        if set(fields).difference(set(receivedFields)):
            # lists are different
            missingFields = set(fields).difference(set(receivedFields))
            nrOfMissingFields = len(missingFields)

        # now go through all fields and check for NULL, NA,...
        nrOfWrongFields = 0
        wrongFields = set()
        wrongValues = ['None', 'Null', '', 'NA']  #TODO make the list of wrong values configurable
        for field in data.fields:
            if field in data:
                value = data[field].value
                if value is None or value in wrongValues:
                    nrOfWrongFields += 1
                    wrongFields.add(field)
            else:
                nrOfWrongFields += 1
                wrongFields.add(field)

        L.d("Completeness missing fields:", nrOfMissingFields, "(", ",".join(missingFields), ")")
        L.d("Completeness wrong fields:", nrOfWrongFields, "(", ",".join(wrongFields), ")")

        length = len(self.repsys.description.fields)
        currentLength = length - nrOfMissingFields - nrOfWrongFields
        self.updatecounter += 1
        if not self.goal:
            self.goal = length
            self.min = float(length)
            self.mean = float(length)
        # 			return (length, self.rewardAndPunishment.value())
        else:
            self.min = min(self.min, currentLength)
            self.mean = ((self.updatecounter - 1) * self.mean) / self.updatecounter + float(
                currentLength) / self.updatecounter
                
        if data.recovered:
            self.rewardAndPunishment.update(False)
        else:
            self.rewardAndPunishment.update(self.goal == currentLength)
        self.absoluteValue = currentLength
        self.ratedValue = self.rewardAndPunishment.value()

        completeness = JSONObject()
        completeness.missingFields = list(missingFields | wrongFields)
        completeness.absoluteValue = self.absoluteValue
        completeness.ratedValue = self.ratedValue
        completeness.unit = self.unit


        # 		print completeness.dumps()

        # 		print "completeness:", self.name, completeness
        # 		print (self.name, missingFields)
        return (self.name, completeness)

# if __main__:
#     
#     test = JSONObject()
#     test.fields = ["v1", "v2", "v3"]
#     test.field.v1.optional = True
#     test.field.v1.value = 1
#     test.field.v2.optional = False
#     test.field.v2.value = 2
#     test.field.v3.value = 3
#     
#     print test
#     print test.field["v1"]
#     testList = [x for x in test.fields if not test.field[x].optional]
#     print testList
    