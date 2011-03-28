
import re
from instrumentation import Status

def ParseInstrumentation(data):
	instrumentation = Instrumentation()
	
	statusCodeRE = re.compile('INSTRUMENTATION_STATUS_CODE: (?P<statuscode>-?\d+)')
	
	statusCodeMatch = statusCodeRE.match(data)
	
	if statusCodeMatch:
		instrumentation.addStatus(int(statusCodeMatch.group('statuscode')))
	
	return instrumentation

class Instrumentation():
	def __init__(self):
		self._statuses = []
	
	def addStatus(self, statusCode):
		self._statuses.append(Status(statusCode))
		
	def statuses(self):
		return self._statuses
