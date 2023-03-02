"""
Python allows negative integers to be used as indices into a sequence, such as a string. If string s has length n, and expression s[k] is used for index -n <= k < 0, what is the equivalent index j >= 0 such that s[j] references the same element. 
"""

"""
If s[k] is used for index -n <= k < 0, then it refers to the kth element counting from the end of the string. To find the equivalent index j >= 0 that references the same element, we can add n to k.

That is, j = k + n.
"""

def convert_negative_index(string, k):
  # Get the length of the string
  length = len(string)
  # Adding the negative index to the length of the string
  return k + length


import unittest

class TestConvertNegativeIndex(unittest.TestCase):

    def test_convert_negative_index(self):
        string = "Hello World"
        self.assertEqual(convert_negative_index(string, -1), 10)
        self.assertEqual(convert_negative_index(string, -7), 4)
        self.assertEqual(convert_negative_index(string, -11), 0)
        
if __name__ == '__main__':
  unittest.main()