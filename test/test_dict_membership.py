"""
Program: test_dict_membership.py
Author: Michael Skyberg, mskyberg@dmacc.edu
Last date modified: June 2020

Purpose: test the use of dictionaries
"""

import unittest
from more_fun_with_collections import dict_membership as dict_mem


class MyTestCase(unittest.TestCase):
    def test_in_set_true(self):
        # create a dictionary
        test_dict = {'cat': 'Larry', 'dog': 'Cooper', 'fish': 'Gills'}
        # test to see if the dictionary contains a key
        self.assertTrue(dict_mem.in_dict(test_dict, 'fish'))

    def test_in_set_false(self):
        # create a dictionary
        test_dict = {'cat': 'Larry', 'dog': 'Cooper', 'fish': 'Gills'}
        # test to see if the dictionary contains a key
        self.assertFalse(dict_mem.in_dict(test_dict, 'goat'))


if __name__ == '__main__':
    unittest.TestCase()
