#!/usr/bin/python3
"""Unittest for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """provides test cases for max_integer func"""

    def test_ordered_list(self):
        """tests an ordered list"""
        ordered_list = [13, 14, 15, 16, 17, 18, 19]
        result = max_integer(ordered_list)
        self.assertEqual(result, 19)

    def test_unordered_list(self):
        """tests an unordered list"""
        unordered_list = [19, 15, 13, 14, 17, 16, 18]
        result = max_integer(unordered_list)
        self.assertEqual(result, 19)

    def test_empty_list(self):
        """tests an empty list"""
        empty_list = []
        result = max_integer(empty_list)
        self.assertEqual(result, None)

    def test_one_item_list(self):
        """tests a list with one item"""
        one_item_list = [67]
        result = max_integer(one_item_list)
        self.assertEqual(result, 67)

    def test_floating_numbers(self):
        """tests a list with floats"""
        float_list = [4.76, 5.34, 16.4, 5.89, 7.12]
        result = max_integer(float_list)
        self.assertEqual(result, 16.4)

    def test_char_list(self):
        """tests a list of characters"""
        char_list = ["m", "o", "n", "e", "y"]
        result = max_integer(char_list)
        self.assertEqual(result, "y")

    def test_ints_and_floats(self):
        """tests a list of float and integer"""
        int_float_list = [-5, -4.5, -7, -8.13, -6.89]
        result = max_integer(int_float_list)
        self.assertEqual(result, -4.5)

    def test_string(self):
        """test a string"""
        string = "zidane"
        result = max_integer(string)
        self.assertEqual(result, "z")
