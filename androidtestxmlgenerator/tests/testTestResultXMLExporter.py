#!/usr/bin/env python

from testresultxmlexporter import ExportXML
from testresult import TestSuite, TestCase
from xml.etree import ElementTree

import unittest

class TestTestResultXMLExporter(unittest.TestCase):
	def _runExportedXMLComparison(self, testResults, expectedXml):
		actualXml = ElementTree.tostring(ElementTree.fromstring(ExportXML(testResults)))
		expected = ElementTree.tostring(ElementTree.fromstring(expectedXml))
		self.assertEqual(actualXml, expected)
	
	def testEmptyTestResults(self):
		time = 1.0
		testResults = TestSuite('name', 'package', time)
		
		expectedStr = ''.join(('<testsuites>',
		                       '<testsuite name="name" package="package" time="1.000"></testsuite>',
		                       '</testsuites>'))
		
		self._runExportedXMLComparison(testResults, expectedStr)

	def testOnePassingTestCaseInOneTestSuite(self):
		time = 1.0
		testSuite = TestSuite('name', 'package', time)
		testSuite.addTestCase(TestCase('testName'))
		
		expectedStr = ''.join(('<testsuites>',
		                       '<testsuite name="name" package="package" time="1.000">',
		                       '<testcase name="testName"></testcase>',
		                       '</testsuite>',
		                       '</testsuites>'))
		self._runExportedXMLComparison(testSuite, expectedStr)

def main():    
	suite = unittest.TestLoader().loadTestsFromTestCase(TestTestResultXMLExporter)
	unittest.TextTestRunner(verbosity = 2).run(suite)

if __name__ == '__main__':
	main()
