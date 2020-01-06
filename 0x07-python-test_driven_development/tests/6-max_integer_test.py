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

    def test_single_val(self):
        """Test for single value"""
        my_list = ["a"]
        self.assertEqual(max_integer(my_list), 'a')

    def test_2_str(self):
        """Test for 2 str"""
        my_list = ["Kati", "Fredlund"]
        self.assertEqual(max_integer(my_list), 'Kati')

    def test_neg_val(self):
        """Test for neg value"""
        my_list = [-1, -2, -3, -4]
        self.assertEqual(max_integer(my_list), -1)

    def test_mixed_neg_val(self):
        """Test for mixed values"""
        my_list = [-1, 2, 3, -4]
        self.assertEqual(max_integer(my_list), 3)

    def test_zero_val(self):
        """Test for zero value"""
        my_list = [0, 0, 0, 0]
        self.assertEqual(max_integer(my_list), 0)

    def test_float_val(self):
        """Test for float value"""
        my_list = [-1, -2.5, -3.7, -4]
        self.assertEqual(max_integer(my_list), -1)

    def test_neg_val(self):
        """Test for neg value"""
        my_list = [-198748937, -223423, -3234325346, 42342412]
        self.assertEqual(max_integer(my_list), 42342412)

if __name__ == '__main__':
    unittest.main()
