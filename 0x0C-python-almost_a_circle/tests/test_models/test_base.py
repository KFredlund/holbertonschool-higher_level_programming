#!/usr/bin/python3
"""tests for base"""
import unittest
from models.base import Base
import os


class test_base(unittest.TestCase):
    """test base class"""

    def setUp(self):
        """setup method"""
        Base._Base__nb_objects = 0

    def test_None(self):
        """testing for None"""
        test = Base(None)
        self.assertEqual(test.id, 1)

    def test_string(self):
        """testing for type string"""
        test = Base("Kati")
        self.assertIsInstance(test.id, str)

    def test_auto(self):
        """testing for assigning automatically an id exists"""
        test = Base()
        self.assertEqual(test.id, 1)

    def test_auto_plus1(self):
        """testing for auto plus 1"""
        test = Base(+ 1)
        self.assertEqual(test.id, 1)

    def test_id_passed(self):
        """testing for saving an id passed in"""
        test = Base(89)
        self.assertEqual(test.id, 89)

if __name__ == "__main__":
    unittest.main()
