#!/usr/bin/python3
import unittest


max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_max_end(self):
        self.assertEqual(max_integer([127, 13, -6, 226]), 226)

    def test_max_begin(self):
        self.assertEqual(max_integer([226, 13, -6, 127]), 226)

    def test_max_middle(self):
        self.assertEqual(max_integer([123, 124, 123]), 124)

    def test_max_middle_2(self):
        self.assertEqual(max_integer([-5, 56, 123, 567, 345, 78]), 567)

    def test_negative_int(self):
        self.assertEqual(max_integer([-10, -234, -17, -7]), -7)

    def test_negative_int(self):
        self.assertEqual(max_integer([3]), 3)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_number(self):
        with self.assertRaises(TypeError):
            max_integer(6)

    def test_string(self):
        with self.assertRaises(TypeError):
            max_integer([23, 'a'])

    def test_tuple(self):
        with self.assertRaises(TypeError):
            max_integer([23, (12, 45)])
