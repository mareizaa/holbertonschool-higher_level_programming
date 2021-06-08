#!/usr/bin/python3
"""
Unittest for Square
"""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """ Test class Square """
    def test_square(self):
        """ Test attributes """
        r1 = Square(10, 2)
        self.assertEqual(r1.size, 10)
        self.assertEqual(r1.area(), 100)
