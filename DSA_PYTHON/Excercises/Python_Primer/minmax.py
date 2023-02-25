"""
Write a short Python function, minmax(data), that takes a sequence of one or more numbers, and returns the smallest and largest numbers, in the form of a tuple of length two. Do not use the built-in functions min or max in implementing your solution.
"""

def minmax(data):
  pass
      

import unittest

class TestMinMax(unittest.TestCase):
  def test_minmax(self):
    # Test for positive numbers
    self.assertEqual(minmax([1, 2, 3]), (1, 3))
    
    # Test for positive and negative numbers
    self.assertEqual(minmax([-10, -5, 0, 5, 10]), (-10, 10))
    
    # Test for a single number
    self.assertEqual(minmax([5]), (5, 5))
    
    # Test for repeating numbers
    self.assertEqual(minmax([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]), (1, 9))
    
if __name__ == "__main__":
  unittest.main()