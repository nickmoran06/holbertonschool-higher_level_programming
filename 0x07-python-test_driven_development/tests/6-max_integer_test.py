#!/usr/bin/python3
import unittest


max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_max_integer(self):
        self.assertEqual(max_integer([127, 13, -6, 226]), 226)

    def test_repeated_number(self):
        self.assertEqual(max_integer([123, 123, 123]), 123)

    def test_neg_numbers(self):
        self.assertEqual(max_integer([-10, -234, -17, -7]), -7)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_number(self):
        with self.assertRaises(TypeError):
            max_integer(6)

    def test_string_number_in_a_list(self):
        with self.assertRaises(TypeError):
            max_integer([23, 'a'])

    def test_dictionary(self):
        with self.assertRaises(KeyError):
            max_integer({'a': b, 'b': c})

    def test_tuple_in_a_list(self):
        with self.assertRaises(TypeError):
            max_integer([23, (12, 45)])
