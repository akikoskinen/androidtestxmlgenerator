#!/usr/bin/env python

from instrumentationparser import ParseInstrumentation

import unittest

class TestInstrumentationParser(unittest.TestCase):
	# Can be overriden if initialization code is needed
	#def setUp(self):
		#pass

	# Can be overriden if deinitialization code is needed
	#def tearDown(self):
		#pass
        
	def testEmptyInstrumentation(self):
		result = ParseInstrumentation('')
		self.assertEqual(len(result.statuses()), 0)
	
	def _runStatusReportWithCodeTest(self, code):
		data = 'INSTRUMENTATION_STATUS_CODE: %d' % code
		result = ParseInstrumentation(data)
		self.assertEqual(len(result.statuses()), 1)
		self.assertEqual(result.statuses()[0].statusCode, code);
	
	def testOneStatusReportWithCode(self):
		self._runStatusReportWithCodeTest(1)
		
	def testOneStatusReportWithNegativeCode(self):
		self._runStatusReportWithCodeTest(-1)
	
	def _runStatusReportWithKeyValuesTest(self, keyValues):
		data = ''
		for kv in keyValues:
			data += "INSTRUMENTATION_STATUS: %s=%s\n" % (kv['key'], kv['value'])
		data += 'INSTRUMENTATION_STATUS_CODE: 1'
		
		result = ParseInstrumentation(data)
		
		self.assertEqual(len(result.statuses()), 1)
		status = result.statuses()[0]
		self.assertEqual(len(status.values), len(keyValues))
		i = 0
		for kv in keyValues:
			self.assertEqual(status.values[i], kv)
			i += 1
	
	def testOneStatusReportWithOneKeyValuePair(self):
		self._runStatusReportWithKeyValuesTest([{'key': 'key1', 'value': 'value1'}])
		
	def testOneStatusReportWithTwoKeyValuePairs(self):
		self._runStatusReportWithKeyValuesTest([{'key': 'key1', 'value': 'value1'}, {'key': 'key2', 'value': 'value2'}])

def main():    
	suite = unittest.TestLoader().loadTestsFromTestCase(TestInstrumentationParser)
	unittest.TextTestRunner(verbosity = 2).run(suite)

if __name__ == '__main__':
	main()
