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
