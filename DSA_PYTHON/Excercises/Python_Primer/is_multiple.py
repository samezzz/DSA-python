"""
Write a short Python function, is_multiple(n, m), that takes two integer values and returns True if n is a multiple of m, that is, n = mi for some integer i, and False otherwise
"""

def is_multiple(n, m):
  # m is not a multiple if it's equal to zero
    if m == 0:
        return False
    # Converting n and m to positive integers
    if n < 0:
        n = -n
    elif m < 0:
        m = -m
    # Returning 0 == Returning False and Returning a value == Returning True
    return n % m == 0


import unittest

class TestIsMultiple(unittest.TestCase):
  def test_is_multiple(self):
    # Test basic case where n is a multiple of n
    self.assertEqual(is_multiple(10, 5), True)
    
    # Test case where n is not a multiple of m
    self.assertEqual(is_multiple(7, 3), False)
    
    # Test case where m is zero
    self.assertEqual(is_multiple(10, 0), False)
    
    # Test case where n is smaller than m
    self.assertEqual(is_multiple(2, 4), False)
    
    # Test case where n and m are both negative
    self.assertEqual(is_multiple(-10, -5), True)

if __name__ == '__main__':
  unittest.main()