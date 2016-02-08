__author__ = 'Marten Fischer (m.fischer@hs-osnabrueck.de)'

import csv
import os.path

if __name__ == "__main__":
    writers = {}
    for i in range(1, 6):
        _id = "BV-%d" % (i,)
        fileobj = open(os.path.join("historicdata", "pollution-%s.csv" % (_id,)), "wb")
        writers[_id] = csv.writer(fileobj, delimiter=';')

    src = open(os.path.join("historicdata", "pollutionevent.csv"), "rb")
    src = csv.reader(src, quotechar='"', delimiter=';')

    headers = src.next()
    headers = ["id", "aqisitionStation", "eventTypeName", "qualityLevelType", "timestamp"]
    eventTypeNames = {"0": "SO2", "1": "PM10", "2": "NO2", "3": "O3", "4": "CO"}
    qualityLevelTypeNames = {"0": "NOT_AVAILABLE", "1": "EXCELLENT", "2": "VERY_GOOD", "3": "GOOD", "4": "MEDIUM", "5": "BAD", "6": "VERY_BAD"}
    for w in writers:
        writers[w].writerow(headers)

    for row in src:
        _id = row[1]
        row[2] = eventTypeNames[row[2]]
        row[3] = qualityLevelTypeNames[row[3]]
        writers[_id].writerow(row)
