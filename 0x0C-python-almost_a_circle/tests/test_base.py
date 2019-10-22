#!/usr/bin/python3

import unittest
import json
from models import base
Base = base.Base

class TestBase(unittest.TestCase):
    """Testing functionality"""

    def TestNoid(self):
        """Testing id as None"""
        self.assertEqual(Base().id, 1)

    def TestSetid(self):
        """Testing id as not None"""
        self.assertEqual(Base(34).id, 34)

    def TestMoreArgs(self):
        """Testing too many args"""
        with self.assertRaises(TypeError):
            Base(2, 1)
