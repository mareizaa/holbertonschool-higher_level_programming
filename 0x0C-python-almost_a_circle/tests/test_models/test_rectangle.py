#!/usr/bin/python3
"""
Unittest for Rectangle
"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """ Test class Rectangle """
    def test_rectangle(self):
        """ Test attributes """
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        r2 = Rectangle(8, 15)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r2.width, 8)
        self.assertEqual(r2.height, 15)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r2.y, 0)
        r3 = Rectangle(8, 15, 5, 4, 6)
        self.assertEqual(r3.id, 6)
        self.assertEqual(r3.width, 8)
        self.assertEqual(r3.height, 15)
        self.assertEqual(r3.x, 5)
        self.assertEqual(r3.y, 4)

    def test_ErrorType(self):
        """ Test attributes """
        r = Rectangle("x", 2)
        self.assertRaises(TypeError, r.width)

    def test_ErrorValue(self):
        """ Test attributes """
        r1 = Rectangle(-0, 2)
        self.assertRaises(ValueError, r1.width)
        r2 = Rectangle(8, 15, -5, 4, 6)
        self.assertRaises(ValueError, r2.x)

    def test_area(self):
        """ Test attributes """
        r = Rectangle(3, 2)
        self.assertEqual(r.area(), 6)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)
