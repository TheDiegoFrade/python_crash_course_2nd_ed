import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
	"""Tests for name_function.py"""

	def test_first_middle_last_name(self):
		"""Do names like Odin Elperro work?"""
		formatted_name = get_formatted_name('odin','elperro','perro')
		self.assertEqual(formatted_name,'Odin Perro Elperro')
#If this file is run as the main program __name__ will change
#to __main__
#When a testing framework imports this file __name__ wont change
#and this block won't be executed
if __name__ == '__main__':
	unittest.main()

 
#unittest.main([module[, defaultTest[, argv[, testRunner[, testLoader]]]]])
#A command-line program that runs a set of tests; this is primarily 
#for making test modules conveniently executable. The simplest use for this 
#function is to include the following line at the end of a test script

#What to do when a test fails.

# assertEqual(a, b)

# Verify that a == b

# assertNotEqual(a, b)

# Verify that a != b

# assertTrue(x)

# Verify that x is True

# assertFalse(x)

# Verify that x is False

# assertIn(item, list)

# Verify that item is in list

# assertNotIn(item, list)

# Verify that item is not in list