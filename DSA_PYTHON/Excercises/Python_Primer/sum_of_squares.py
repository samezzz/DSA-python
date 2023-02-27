"""
Write a short Python function that takes a positive integer n and returns the sum of the squares of all the positive integers smaller than n.
"""

def sumOfSquares(pos_num):
  # Get a list of all the numbers smaller than the positive number
  below_num = list(range(pos_num))
  # Before iteration sum == 0
  init_sum = 0
  # Loop through the list and add the square of each number to init_sum
  for i in below_num:
    init_sum += below_num[i] ** 2
  return init_sum

"""
A more efficient way of doing this
def sumOfSquares(pos_num):
  return (pos_num * (pos_num + 1) * (2 * pos_num + 1)) // 6

OR

def sumOfSquares(pos_num):
return sum(i ** 2 for i in range(pos_num))

"""

import unittest

class TestSumOfSquares(unittest.TestCase):
  def test_sumOfSquares(self):
    # Testing a random positive number
    self.assertEqual(sumOfSquares(4), 14)
    # Test for 1 as input
    self.assertEqual(sumOfSquares(1), 0)
    
if __name__ == "__main__":
  unittest.main()