"""
Write a short Python function, is_even(k), that takes an integer value and returns True if k is even, and False otherwise. However, your function cannot use the multiplication, modulo, or division operators
"""

# It's even if the last digit is [0, 2, 4, 6, 8] and odd if [1, 3, 5, 7, 9]
even = [0, 2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

def is_even(number):
  # Converts the number to a string
  string = str(number)
  # Get the length to find the last char in the string
  length = len(string)
  last_char = string[length - 1]
  # Convert the last character to an integer
  last_digit = int(last_char)
  # Check the condition
  if last_digit in even:
    return True
  elif last_digit in odd:
    return False

# more efficient solution
"""
def is_even(n):
  return (n & 1) == 0
"""


import unittest

class TestIsEven(unittest.TestCase):
  def test_is_even(self):
    # Test if a number is even
    self.assertEqual(is_even(26), True)
    
    # Test if a number is odd
    self.assertEqual(is_even(31), False)
    
    # Testing negative even number
    self.assertEqual(is_even(-52), True)
    
    # Testing negative odd number
    self.assertEqual(is_even(-31), False)
    
if __name__ == '__main__':
  unittest.main()
    