#!/usr/bin/env python

from testresultxmlexporter import ExportXML
from testresult import TestSuite
from xml.etree import ElementTree

import unittest

class TestTestResultXMLExporter(unittest.TestCase):
	def testEmptyTestResults(self):
		time = 1.0
		testResults = TestSuite('name', 'package', time)
		actualXml = ElementTree.tostring(ElementTree.fromstring(ExportXML(testResults)))
		
		expectedStr = '<testsuites><testsuite name="name" package="package" time="1.000"></testsuite></testsuites>'
		expected = ElementTree.tostring(ElementTree.fromstring(expectedStr))
		self.assertEqual(actualXml, expected)

def main():    
	suite = unittest.TestLoader().loadTestsFromTestCase(TestTestResultXMLExporter)
	unittest.TextTestRunner(verbosity = 2).run(suite)

if __name__ == '__main__':
	main()
