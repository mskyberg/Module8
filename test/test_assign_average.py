"""
Program: test_assign_average.py
Author: Michael Skyberg, mskyberg@dmacc.edu
Last date modified: June 2020

Purpose: test a switch style statement
"""

import unittest
import unittest.mock as mock
from more_fun_with_collections import assign_average as aa


class MyTestCase(unittest.TestCase):
    def test_case_A(self):
        self.assertEqual(aa.get_switch_value('A'), 90)
        self.assertEqual(aa.get_switch_value('a'), 90)

    def test_case_B(self):
        self.assertEqual(aa.get_switch_value('B'), 80)
        self.assertEqual(aa.get_switch_value('b'), 80)

    def test_case_C(self):
        self.assertEqual(aa.get_switch_value('C'), 70)
        self.assertEqual(aa.get_switch_value('c'), 70)

    def test_case_D(self):
        self.assertEqual(aa.get_switch_value('D'), 60)
        self.assertEqual(aa.get_switch_value('d'), 60)

    def test_case_F(self):
        self.assertEqual(aa.get_switch_value('F'), 50)
        self.assertEqual(aa.get_switch_value('f'), 50)

    def test_case_not_exists(self):
        with self.assertRaises(ValueError):
            aa.get_switch_value('E')

    def test_average_grade(self):
        grade_list = ['A', 'b', 'C', 'd']
        self.assertEqual(aa.switch_average(grade_list), 75)


if __name__ == '__main__':
    unittest.TestCase()
