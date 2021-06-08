#!/usr/bin/python3
"""
Unittest for base
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """ Test class Base """
    def test_id_base(self):
        """ Test id """
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base(8)
        self.assertEqual(b3.id, 8)
