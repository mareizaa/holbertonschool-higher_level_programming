#!/usr/bin/python3
"""
Unittest for Rectangle inherits from Base
"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """ Test class Rectangle inherits from Base"""
    def test_rectangle(self):
        """ Test attributes """
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 7)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        r2 = Rectangle(8, 15)
        self.assertEqual(r2.id, 8)
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
        with self.assertRaises(TypeError) as error:
            r = Rectangle("x", 2)
        self.assertEqual("width must be an integer", str(error.exception))

    def test_ErrorValue(self):
        """ Test attributes """
        with self.assertRaises(ValueError):
            r1 = Rectangle(-0, 2)
        with self.assertRaises(ValueError):
            r2 = Rectangle(8, 15, -5, 4, 6)
        

    def test_area(self):
        """ Test attributes """
        r = Rectangle(3, 2)
        self.assertEqual(r.area(), 6)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)
