#!/usr/bin/env python

# Copyright (c) 2011 Aki Koskinen
# Licensed under the MIT license. See LICENSE file for details.

from instrumentation import Instrumentation, Status
from instrumentationtotestresulttransformer import Transform

import unittest

class TestInstrumentationToTestResultTransformer(unittest.TestCase):
	SUCCESS = 0
	ERROR = -1
	FAIL = -2
	
	def setUp(self):
		self._instrumentation = Instrumentation()
		
	def _addTestRun(self, className, methodName, result):
		status = Status()
		status['class'] = className
		status['test'] = methodName
		status.statusCode = 1
		self._instrumentation.addStatus(status)
		
		status = Status()
		status['class'] = className
		status['test'] = methodName
		status.statusCode = result
		self._instrumentation.addStatus(status)

	def _addSuccessfulTestRun(self, className, methodName):
		self._addTestRun(className, methodName, self.SUCCESS)
	
	def _addFailingTestRun(self, className, methodName, stack):
		self._addTestRun(className, methodName, self.FAIL)
		self._instrumentation.statuses()[-1]['stack'] = stack
	
	def _addErroringTestRun(self, className, methodName, stack):
		self._addTestRun(className, methodName, self.ERROR)
		self._instrumentation.statuses()[-1]['stack'] = stack

	def assertTestSuite(self, suite, name, package):
		self.assertEqual(suite.name, name)
		self.assertEqual(suite.package, package)
	
	def assertTestCase(self, case, method):
		self.assertEqual(case.name, method)

	PACKAGE = 'com.example'
	CLASS_NAME = 'TestClass'
	FULL_CLASS = '.'.join((PACKAGE, CLASS_NAME))
	METHOD = 'testMethod'
	
	def testOneSucceedingTestMethod(self):
		self._addSuccessfulTestRun(self.FULL_CLASS, self.METHOD)
		
		testResults = Transform(self._instrumentation)
		
		self.assertTestSuite(testResults[0], self.FULL_CLASS, self.PACKAGE)
		self.assertTestCase(testResults[0].testCases[0], self.METHOD)

	FAIL_REASON = 'frame1'
	STACK = '\n'.join((FAIL_REASON, 'frame2'))

	def testOneFailingTestMethod(self):
		self._addFailingTestRun(self.FULL_CLASS, self.METHOD, self.STACK)
		
		testResults = Transform(self._instrumentation)
		
		testSuite = testResults[0]
		testCase = testSuite.testCases[0]
		self.assertTrue(testCase.isFailing())
		self.assertEqual(testCase.failMessage, self.FAIL_REASON)
		self.assertEqual(testCase.failStack, self.STACK)

	METHOD2 = 'testMethod2'
	
	def testTwoSucceedingTestMethods(self):
		self._addSuccessfulTestRun(self.FULL_CLASS, self.METHOD)
		self._addSuccessfulTestRun(self.FULL_CLASS, self.METHOD2)
		
		testResults = Transform(self._instrumentation)
		
		self.assertTestCase(testResults[0].testCases[0], self.METHOD)
		self.assertTestCase(testResults[0].testCases[1], self.METHOD2)
	
	def testOneErroringTestMethod(self):
		self._addErroringTestRun(self.FULL_CLASS, self.METHOD, self.STACK)
		
		testResults = Transform(self._instrumentation)
		
		testSuite = testResults[0]
		testCase = testSuite.testCases[0]
		self.assertTrue(testCase.isErroring())
		self.assertEqual(testCase.errorMessage, self.FAIL_REASON)
		self.assertEqual(testCase.errorStack, self.STACK)
	
	CLASS_NAME2 = 'TestClass2'
	FULL_CLASS2 = '.'.join((PACKAGE, CLASS_NAME2))
	
	def testTwoTestSuites(self):
		self._addSuccessfulTestRun(self.FULL_CLASS, self.METHOD)
		self._addSuccessfulTestRun(self.FULL_CLASS2, self.METHOD)
		
		testResults = Transform(self._instrumentation)
		
		self.assertTestSuite(testResults[0], self.FULL_CLASS, self.PACKAGE)
		self.assertTestCase(testResults[0].testCases[0], self.METHOD)

		self.assertTestSuite(testResults[1], self.FULL_CLASS2, self.PACKAGE)
		self.assertTestCase(testResults[1].testCases[0], self.METHOD)

def main():    
	suite = unittest.TestLoader().loadTestsFromTestCase(TestInstrumentationToTestResultTransformer)
	unittest.TextTestRunner(verbosity = 2).run(suite)

if __name__ == '__main__':
	main()
