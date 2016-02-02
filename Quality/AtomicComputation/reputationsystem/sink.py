import sys

class Sink(object):
	"""docstring for Sink"""
	def __init__(self):
		self.metrics = {}
		self.reputation = 1.0
		self.reputationsystem = None
# 		self.timestamp = None #to be set by a (all) QoIMetric

	def qoiMetricAdded(self, qoiMetricName, initValue):
		""" called when a new qoiMetric is added to the reputation system """
		pass

	def startup(self):
		"""This method is called immediately before the reputation system starts"""
		raw_input("enter to stop")
		if self.reputationsystem != None:
			self.reputationsystem.feed.stop1()
		sys.exit()

	def update(self, qoiMetric):
		""" qoiMetric = tuple (absoluter Wert, Bewertung) """
		self.metrics[qoiMetric.name] = qoiMetric
		print "%s updated to %f (%f)" % (qoiMetric.name, qoiMetric.absoluteValue, qoiMetric.ratedValue)

	def persist(self, observationIdList):
		print "persist called in Sink"
		