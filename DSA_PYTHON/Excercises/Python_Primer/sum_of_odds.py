"""
Write a short python function that takes a positive integer n and returns the sum of the squares of all the odd positive integers smaller than n
"""

def sum_of_odds(pos_int):
  # Get a list of all the numbers smaller than the positive number
  below_int = list(range(pos_int))
  # Before iteration sum == 0
  init_sum = 0
  # Loop through the List and add the square of the odd numbers
  for num in below_int:
    if num % 2 == 1:
      init_sum += num ** 2
  return init_sum 

"""
def sum_of_odds(pos_int):
  return sum(i ** 2 for i in range(pos_int) if i % 2 == 1)
"""

import unittest

class TestSumOfOdds(unittest.TestCase):
  def test_sumOfOdds(self):
    # Testing a random positive integer
    self.assertEqual(sum_of_odds(14), 455)
    # Test for 1 as input
    self.assertEqual(sum_of_odds(1), 0)
    
if __name__ == "__main__":
  unittest.main()