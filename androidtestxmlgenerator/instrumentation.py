
class Status():
	def __init__(self):
		self._values = {}
		self.statusCode = 0
	
	def __getitem__(self, key):
		return self._values[key]
	
	def __setitem__(self, key, value):
		self._values[key] = value

class Instrumentation():
	def __init__(self):
		self._statuses = []
	
	def addStatus(self, status):
		self._statuses.append(status)
		
	def statuses(self):
		return self._statuses
