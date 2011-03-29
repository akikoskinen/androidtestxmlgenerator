from xml.etree import ElementTree

def ExportXML(testSuite):
	root = ElementTree.Element('testsuites')
	
	suite = ElementTree.SubElement(root, 'testsuite')
	
	suite.set('name', testSuite.name)
	suite.set('package', testSuite.package)
	suite.set('time', '%.3f' % testSuite.time)
	
	try:
		case = testSuite.testCases[0]
		caseElement = ElementTree.SubElement(suite, 'testcase')
		caseElement.set('name', case.name)
	except:
		pass
	
	return ElementTree.tostring(root)
	