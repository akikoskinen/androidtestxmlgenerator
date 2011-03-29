#!/usr/bin/env python

from testresultxmlexporter import ExportXML
from testresult import TestSuite, TestCase
from xml.etree import ElementTree

import unittest

class TestTestResultXMLExporter(unittest.TestCase):
	def setUp(self):
		self._testSuites = []
	
	def _addTestSuite(self, name, package, time):
		testSuite = TestSuite(name, package, time)
		self._testSuites.append(testSuite)
		return testSuite
	
	def _generateExpectedXml(self):
		xml = '<testsuites>'
		
		for suite in self._testSuites:
			xml += '<testsuite name="%s" package="%s" time="%.3f">' % (suite.name, suite.package, suite.time)
			
			for case in suite.testCases:
				xml += '<testcase name="%s">' % case.name
				if case.isFailing():
					xml += '<failure message="%s">%s</failure>' % (case.failMessage, case.failStack)
				xml += '</testcase>'
			
			xml += '</testsuite>'
		
		xml += '</testsuites>'
		
		return xml
	
	def _runExportedXMLComparison(self):
		actualXml = ElementTree.tostring(ElementTree.fromstring(ExportXML(self._testSuites)))
		expected = ElementTree.tostring(ElementTree.fromstring(self._generateExpectedXml()))
		self.assertEqual(actualXml, expected)
	
	def testEmptyTestResults(self):
		self._addTestSuite('name', 'package', 1.0)
		
		self._runExportedXMLComparison()

	def testOnePassingTestCaseInOneTestSuite(self):
		testSuite = self._addTestSuite('name', 'package', 1.0)
		testSuite.addTestCase(TestCase('testName'))
		
		self._runExportedXMLComparison()
		
	def testTwoPassingTestCasesInOneTestSuite(self):
		testSuite = self._addTestSuite('name', 'package', 1.0)
		testSuite.addTestCase(TestCase('testName1'))
		testSuite.addTestCase(TestCase('testName2'))
		
		self._runExportedXMLComparison()
		
	def testTwoTestSuites(self):
		self._addTestSuite('name1', 'package1', 1.0)
		self._addTestSuite('name2', 'package2', 1.0)
		
		self._runExportedXMLComparison()
	
	def testFailingTestCase(self):
		testSuite = self._addTestSuite('name', 'package', 1.0)
		testCase = TestCase('testName')
		testCase.setFailing('message', 'stack')
		testSuite.addTestCase(testCase)
		
		self._runExportedXMLComparison()

def main():    
	suite = unittest.TestLoader().loadTestsFromTestCase(TestTestResultXMLExporter)
	unittest.TextTestRunner(verbosity = 2).run(suite)

if __name__ == '__main__':
	main()
