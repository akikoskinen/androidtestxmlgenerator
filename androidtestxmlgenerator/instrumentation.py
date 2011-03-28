
class Status():
	def __init__(self):
		self.values = []
		self.statusCode = 0

class Instrumentation():
	def __init__(self):
		self._statuses = []
	
	def addStatus(self, status):
		self._statuses.append(status)
		
	def statuses(self):
		return self._statuses
