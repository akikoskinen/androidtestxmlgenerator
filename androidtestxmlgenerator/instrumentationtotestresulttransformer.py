from testresult import TestSuite, TestCase

TEST_COMPLETED_OK = 0

def Transform(instrumentation):
	ret = []
	
	for status in instrumentation.statuses():
		if status.statusCode == TEST_COMPLETED_OK:
			fullClassName = status['class']
			(package, sep, className) = fullClassName.rpartition('.')
			
			suite = TestSuite(fullClassName, package, 0.0)
			ret.append(suite)
			
			suite.addTestCase(TestCase(status['test']))
	
	return ret
