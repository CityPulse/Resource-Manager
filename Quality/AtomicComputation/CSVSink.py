
import csv
import os.path
import time

from reputationsystem.sink import Sink

PATH = "./qoiOutput/"

class CSVSink(Sink):
	def __init__(self):
		super(CSVSink, self).__init__()
		self.converted = False
		self.header = None
		self.csvf = None
		if not os.path.exists(PATH):
			os.mkdir(PATH)

	def update(self, qoiMetric):
		self.metrics[qoiMetric.name] = qoiMetric

	def persist(self, observationIdList):
		
		if not self.csvf:
			sensorType = self.reputationsystem.description.sensorType
			sensorID = str(self.reputationsystem.description.sensorID)
			filename = "qoiOutput_" + sensorType + "_" + sensorID +  ".csv"
			self.csvfile = open(PATH + filename, 'w')
			self.csvf = csv.writer(self.csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		
		if not self.header:
			self.header = ["streamId","location","timestamp"]
			for metricName in self.metrics:
				m = self.metrics[metricName]
				self.header.append(m.name)
			self.csvf.writerow(self.header)
		
		streamId = self.reputationsystem.description.fullSensorID
		location = self.reputationsystem.description.location
		output = [streamId, location]

		output.append(int(time.mktime(self.reputationsystem.timestamp.timetuple())))

		for metricName in self.metrics:
			m = self.metrics[metricName]
			output.append(str(m.ratedValue))

		self.csvf.writerow(output)
		self.csvfile.flush()
		
		
			