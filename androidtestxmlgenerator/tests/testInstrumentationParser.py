#!/usr/bin/env python

from instrumentationparser import ParseInstrumentation

import unittest

class TestInstrumentationParser(unittest.TestCase):
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
		KEY = 0
		VALUE = 1
		data = ''
		for kv in keyValues:
			data += "INSTRUMENTATION_STATUS: %s=%s\n" % (kv[KEY], kv[VALUE])
		data += 'INSTRUMENTATION_STATUS_CODE: 1'
		
		result = ParseInstrumentation(data)
		
		self.assertEqual(len(result.statuses()), 1)
		status = result.statuses()[0]
		
		for kv in keyValues:
			self.assertEqual(status.values[kv[KEY]], kv[VALUE])
	
	def testOneStatusReportWithOneKeyValuePair(self):
		self._runStatusReportWithKeyValuesTest([['key1', 'value1']])
		
	def testOneStatusReportWithTwoKeyValuePairs(self):
		self._runStatusReportWithKeyValuesTest([['key1', 'value1'], ['key2', 'value2']])
	
	def testOneStatusReportWithKeyValuePairWithMultilineValue(self):
		self._runStatusReportWithKeyValuesTest([['key1', 'line1\nline2']])


def main():    
	suite = unittest.TestLoader().loadTestsFromTestCase(TestInstrumentationParser)
	unittest.TextTestRunner(verbosity = 2).run(suite)

if __name__ == '__main__':
	main()
