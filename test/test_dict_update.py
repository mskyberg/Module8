"""
Program: test_dict_update.py
Author: Michael Skyberg, mskyberg@dmacc.edu
Last date modified: June 2020

Purpose: test the use of dictionaries
"""

import unittest
import unittest.mock as mock
from more_fun_with_collections import dict_update


class MyTestCase(unittest.TestCase):
    def test_average_scores(self):
        # create a dictionary
        test_dict = {'Test 0': 81, 'Test 1': 92, 'Test 2': 88}
        # test to see if the dictionary contains a key
        self.assertAlmostEqual(dict_update.average_scores(test_dict), 87, 10)

    def test_get_scores_dict(self):
        # mock input from a user
        with mock.patch('builtins.input', side_effect=[2, 90, 95]):
            assert dict_update.get_test_scores() == {'Test 0': 90, 'Test 1': 95}


if __name__ == '__main__':
    unittest.TestCase()
