"""
Python's random module includes a function choice(data) that returns a random element from a non-empty sequence. The random module includes a more basic function randrange, with parameterization similar to the built-in range function, that return a random choice from the given range. Using only the randrange function, implement your own version of the choice function.
"""

import random

def random_choice(sequence):
    index = random.randrange(len(sequence))
    return sequence[index]
  
import unittest

class TestRandomChoice(unittest.TestCase):
  def test_random_choice(self):
    sequence = [1, 2, 3, 4, 5]
    choice = random_choice(sequence)
    self.assertIn(choice, sequence)

    sequence = "Hello, World!"
    choice = random_choice(sequence)
    self.assertIn(choice, sequence)


if __name__ == "__main__":
  unittest.main()