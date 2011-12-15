# Copyright (c) 2011 Aki Koskinen
# Licensed under the MIT license. See LICENSE file for details.

from xml.etree import ElementTree

def ExportXML(testSuites):
	root = ElementTree.Element('testsuites')
	
	for testSuite in testSuites:
		suite = ElementTree.SubElement(root, 'testsuite')
	
		suite.set('name', testSuite.name)
		suite.set('package', testSuite.package)
		suite.set('time', '%.3f' % testSuite.time)
	
		for case in testSuite.testCases:
			caseElement = ElementTree.SubElement(suite, 'testcase')
			caseElement.set('name', case.name)
			
			if case.isFailing():
				failureElement = ElementTree.SubElement(caseElement, 'failure')
				failureElement.set('message', case.failMessage)
				failureElement.text = case.failStack
			
			if case.isErroring():
				errorElement = ElementTree.SubElement(caseElement, 'error')
				errorElement.set('message', case.errorMessage)
				errorElement.text = case.errorStack
	
	return ElementTree.tostring(root)
