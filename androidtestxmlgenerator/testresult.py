# Copyright (c) 2011 Aki Koskinen
# Licensed under the MIT license. See LICENSE file for details.

class TestSuite():
	def __init__(self, name, package, time):
		self.name = name
		self.package = package
		self.time = time
		self.testCases = []
	
	def addTestCase(self, testCase):
		self.testCases.append(testCase)

class TestCase():
	def __init__(self, name):
		self.name = name
	
	def setFailing(self, message, stack):
		self.failMessage = message
		self.failStack = stack
	
	def isFailing(self):
		return hasattr(self, 'failMessage')
		
	def setErroring(self, message, stack):
		self.errorMessage = message
		self.errorStack = stack
	
	def isErroring(self):
		return hasattr(self, 'errorMessage')
