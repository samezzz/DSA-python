"""
Write a short python function that takes a positive integer n and returns the sum of the squares of all the odd positive integers smaller than n
"""

def sum_of_odds(pos_int):
  below_int = list(range(pos_int))
  init_sum = 0
  for num in below_int:
    if num % 2 == 1:
      init_sum += num ** 2
  return init_sum 

import unittest

class TestSumOfOdds(unittest.TestCase):
  def test_sumOfOdds(self):
    # Testing a random positive integer
    self.assertEqual(sum_of_odds(14), 455)
    # Test for 1 as input
    self.assertEqual(sum_of_odds(1), 0)
    
if __name__ == "__main__":
  unittest.main()