"""
Write a short python function that receives a list of n integers, so that the numbers are listed in the opposite order than they were before, and compare this method to an equivalent python function for doing the same thing
"""

def reverse_list(data):
    my_list = []
    for index, value in enumerate(data):
        return my_list.append(data[len(data) - index - 1])

reverse_list([23, 24, 25, 26])

import unittest

class TestReverseList(unittest.TestCase):
    def test_reverse_list(self):
        # Test with a list of even length
        self.assertEqual(reverse_list([1, 2, 3, 4]), [4, 3, 2, 1])
        
        # Test with a list of odd length
        self.assertEqual(reverse_list([1, 2, 3, 4, 5]), [5, 4, 3, 2, 1])
        
        # Test with an empty list
        self.assertEqual(reverse_list([]), [])
        
        # Test with a list of one element
        self.assertEqual(reverse_list([1]), [1])
        
        # Test with a list of duplicate values
        self.assertEqual(reverse_list([1, 2, 2, 3, 3, 3]), [3, 3, 3, 2, 2, 1])
        
        # Test with a list of negative numbers
        self.assertEqual(reverse_list([-1, -2, -3, -4]), [-4, -3, -2, -1])
    
if __name__ == "__main__":
    unittest.main()