#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Function to find and return the max integer in a list of integers
        If the list is empty, the function returns None
    """
    def test_integer(self):
        self.assertEqual(max_integer([3, 8, 2, 6]), 8)
        self.assertEqual(max_integer([3, -8, 2, 6]), 6)
        self.assertEqual(max_integer([15, -8, 2, 6]), 15)
        self.assertEqual(max_integer([6]), 6)

    def string(self):
        self.assertRaises(TypeError, max_integer["hello", "world", 6, "h"])
        self.assertRaises(TypeError, max_integer[6, "h"])

    def list_is_empty(self):
        self.assertEqual(max_integer(()), None)
        self.assertEqual(max_integer([]), None)

    def num_float(self):
        self.assertEqual(max_integer(float('-inf')), 8)
        self.assertEqual(max_integer(float('-inf')), float('-inf'))
        self.assertEqual(max_integer(float('inf')), 8)
        self.assertEqual(max_integer(float('inf'), 6, 10), float('inf'))
