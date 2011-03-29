
import re
from instrumentation import Status, Instrumentation

_statusBlockRE = re.compile(r'(?P<keyvalues>(?:INSTRUMENTATION_STATUS: [^=]+=.*?)*)'
                             'INSTRUMENTATION_STATUS_CODE: (?P<statuscode>-?\d+)', re.DOTALL)

_keyValuesSplitterRE = re.compile(r'INSTRUMENTATION_STATUS: ')
_keyValueRE = re.compile(r'(?P<key>[^=]+)=(?P<value>.*)', re.DOTALL)


def _ParseStatus(statusBlockString):
	status = Status()
	
	statusMatch = _statusBlockRE.match(statusBlockString)
	if statusMatch:
		for keyvalue in _keyValuesSplitterRE.split(statusMatch.group('keyvalues')):
			keyValueMatch = _keyValueRE.match(keyvalue)
			if keyValueMatch:
				status.values[keyValueMatch.group('key')] = keyValueMatch.group('value').strip()
		status.statusCode = int(statusMatch.group('statuscode'))
	
	return status


def ParseInstrumentation(data):
	instrumentation = Instrumentation()
	
	statusBlockString = ''
	for line in data.splitlines():
		statusBlockString += line + '\n'

		if line.startswith("INSTRUMENTATION_STATUS_CODE:"):
			status = _ParseStatus(statusBlockString)
			instrumentation.addStatus(status)
			statusBlockString = ""
	
	return instrumentation
