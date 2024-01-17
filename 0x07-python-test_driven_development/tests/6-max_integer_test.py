#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """ Tests 6-max_integer """

    def test_max_isatEND(self):
        """ Max number is at end """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_isbeginning(self):
        """ Max number is at beginning """
        self.assertEqual(max_integer([6, 1, 2, 3, 4]), 6)

    def test_max_inthemiddle(self):
        """Max in the middle """

        self.assertEqual(max_integer([1, 2, 9, 3, 4]), 9)

    def test_onenegative(self):
        """ A negative """

        self.assertEqual(max_integer([1, 4, 0, -6, 8]), 8)

    def test_allnegative(self):
        """All negative """

        self.assertEqual(max_integer([-4, -6, -1, -5, -2]), -1)

    def test_listofone(self):
        """One ELEMENT """

        self.assertEqual(max_integer([7]), 7)

    def test_emptylist(self):
        """ Empty List """

        self.assertEqual(max_integer([]), None)


if __name__ == '__main__':
    unittest.main()
