from testresult import TestSuite, TestCase

TEST_COMPLETED_OK = 0
TEST_COMPLETED_FAIL = -2
INTERESTING_CODES = (TEST_COMPLETED_OK, TEST_COMPLETED_FAIL)

def Transform(instrumentation):
	ret = []
	
	for status in instrumentation.statuses():
		if status.statusCode in INTERESTING_CODES:
			fullClassName = status['class']
			(package, dot, className) = fullClassName.rpartition('.')
			
			suite = TestSuite(fullClassName, package, 0.0)
			ret.append(suite)
			
			case = TestCase(status['test'])
			suite.addTestCase(case)
			
		if status.statusCode == TEST_COMPLETED_FAIL:
			case.setFailing(status['stack'].partition('\n')[0], status['stack'])
	
	return ret
