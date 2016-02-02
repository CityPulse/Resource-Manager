__author__ = 'Marten Fischer (m.fischer@hs-osnabrueck.de)'

import uuid

class ObservationIDGenerator(object):

    @classmethod
    def addObservationIDToFields(cls, data):
        if data:
            for f in data.fields:
                if f in data:
                    data[f].observationID = uuid.uuid4()
