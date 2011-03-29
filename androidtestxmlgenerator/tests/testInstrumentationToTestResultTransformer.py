#!/usr/bin/env python

from instrumentation import Instrumentation, Status
from instrumentationtotestresulttransformer import Transform

import unittest

class TestInstrumentationToTestResultTransformer(unittest.TestCase):
	def testOneSucceedingTestMethod(self):
		instrumentation = Instrumentation()
		
		status = Status()
		status.values['class'] = 'com.example.TestClass'
		status.values['test'] = 'testMethod'
		status.statusCode = 1
		instrumentation.addStatus(status)
		
		status = Status()
		status.values['class'] = 'com.example.TestClass'
		status.values['test'] = 'testMethod'
		status.statusCode = 0
		instrumentation.addStatus(status)
		
		testResults = Transform(instrumentation)
		
		testSuite = testResults[0]
		self.assertEqual(testSuite.name, 'com.example.TestClass')
		self.assertEqual(testSuite.package, 'com.example')

		testCase = testSuite.testCases[0]
		self.assertEqual(testCase.name, 'testMethod')

def main():    
	suite = unittest.TestLoader().loadTestsFromTestCase(TestInstrumentationToTestResultTransformer)
	unittest.TextTestRunner(verbosity = 2).run(suite)

if __name__ == '__main__':
	main()
