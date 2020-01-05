#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_empty(self):
        """Test for empty list"""
        my_list = []
        self.assertEqual(max_integer(my_list), None)

    def test_not_list(self):
        """Test for not a list type"""
        my_list = {}
        self.assertEqual(max_integer(my_list), None)

    def test_max(self):
        """Test for max int"""
        my_list = [1, 2, 3, 4, 5]
        self.assertEqual(max_integer(my_list), 5)

    def test_mixed_val(self):
        """Test for mixed types"""
        my_list = ["a", 2, "c", 4, "e"]
        self.assertRaises(TypeError, max_integer, my_list)

if __name__ == '__main__':
    unittest.main()
