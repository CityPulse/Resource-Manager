from math import sin, radians

from virtualisation.misc.jsonobject import JSONObject


class QoIMetric(object):
	"""docstring for QoIMetric"""
	def __init__(self, name):
		self.name = name
		def repsys():
			doc = "The repsys property."
			def fget(self):
				return self._repsys
			def fset(self, value):
				self._repsys = value
			def fdel(self):
				del self._repsys
			return locals()
		self.repsys = property(**repsys())
		def weight():
			doc = "The weight property."
			def fget(self):
				return self._weight
			def fset(self, value):
				self._weight = value
			def fdel(self):
				del self._weight
			return locals()
		self.weight = property(**weight())
		self.weight = 1.0
		self.absoluteValue = 0
		self.ratedValue = 1.0
		self.initialValue = 1.0

		# stats
		self.min = None
		self.mean = None

	def update(self, data):
		return (self.initialValue, self.initialValue)

	def getStats(self):
		return (self.min, self.mean)
	
	def nonValueUpdate(self):
		jsonOb = JSONObject()
		jsonOb.absoluteValue = self.absoluteValue
		jsonOb.ratedValue = self.ratedValue
		jsonOb.unit = self.unit
		return (self.name, jsonOb)

class ConstantQoI(QoIMetric):
	"""Simulates a QoIMetric. Just for testing purposes."""
	def __init__(self, name, value):
		super(ConstantQoI, self).__init__(name)
		self.value = value

	def update(self, data):
		self.absoluteValue = self.value
		self.ratedValue = self.value
		
class SinusQoI(QoIMetric):
	"""Simulates a QoIMetric. Just for testing purposes."""
	def __init__(self, name, value, deviation):
		super(SinusQoI, self).__init__(name)
		self.value = value
		self.deviation = deviation
		self.i = 0

	def update(self, data):
		"""return tuple (absoluter Wert, Bewertung) """
		self.i += 1
		x = max(0.0, min(1.0, self.value + sin(radians(self.i)) * self.deviation))
		self.absoluteValue = x * 100
		self.ratedValue = x
