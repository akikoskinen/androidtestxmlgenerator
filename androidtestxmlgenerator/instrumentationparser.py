
import re
from instrumentation import Status, Instrumentation

def ParseInstrumentation(data):
	instrumentation = Instrumentation()
	
	statusRE = re.compile('INSTRUMENTATION_STATUS: (?P<key>[^=]+)=(?P<value>.*)')
	statusCodeRE = re.compile('INSTRUMENTATION_STATUS_CODE: (?P<statuscode>-?\d+)')
	
	status = None
	
	for line in data.splitlines():
		statusMatch = statusRE.match(line)
		if statusMatch:
			if status == None:
				status = Status()
			keyValuePair = {'key': statusMatch.group('key'), 'value': statusMatch.group('value')}
			status.values.append(keyValuePair)
			continue
		
		statusCodeMatch = statusCodeRE.match(line)
		if statusCodeMatch:
			if status == None:
				status = Status()
			status.statusCode = int(statusCodeMatch.group('statuscode'))
			instrumentation.addStatus(status)
	
	return instrumentation
