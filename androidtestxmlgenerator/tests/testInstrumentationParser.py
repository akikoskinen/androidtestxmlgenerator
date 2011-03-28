#!/usr/bin/env python

from instrumentationparser import ParseInstrumentation

import unittest

class TestInstrumentationParser(unittest.TestCase):
	# Can be overriden if initialization code is needed
	#def setUp(self):
		#pass

	# Can be overriden if deinitialization code is needed
	#def tearDown(self):
		#pass
        
	def testEmptyInstrumentation(self):
		result = ParseInstrumentation('')
		self.assertEqual(len(result.statuses()), 0)

def main():    
	suite = unittest.TestLoader().loadTestsFromTestCase(TestInstrumentationParser)
	unittest.TextTestRunner(verbosity = 2).run(suite)

if __name__ == '__main__':
	main()
