"""This module contains test cases for the Math and Stats Functions package."""

import unittest
from mymath import basic, stats

class TestMathFunctions(unittest.TestCase):
    """This class contains test cases for the Math Functions package."""
    def test_square(self):
        """This method tests the square function."""
        self.assertEqual(basic.square(2), 4)
        self.assertEqual(basic.square(3.0), 9.0)
        self.assertNotEqual(basic.square(-3), -9)

    def test_double(self):
        """This method tests the double function."""
        self.assertEqual(basic.double(2), 4)
        self.assertEqual(basic.double(3.1), 6.2)
        self.assertEqual(basic.double(0), 0)

    def test_add(self):
        """This method tests the add function."""
        self.assertEqual(basic.add(2, 4), 6)
        self.assertEqual(basic.add(0, 0), 0)
        self.assertEqual(basic.add(2.3, 3.6), 5.9)
        self.assertEqual(basic.add('hello', 'world'), 'helloworld')
        self.assertEqual(basic.add(2.3000, 4.3000), 6.6)
        self.assertNotEqual(basic.add(-2, -2), 0)

class TestStatsFunctions(unittest.TestCase):
    """This class contains test cases for the Stats Functions package."""
    def test_mean(self):
        """This method tests the mean function."""
        self.assertEqual(stats.mean([1, 2, 3, 4, 5]), 3.0)
        self.assertEqual(stats.mean([2.5, 3.5, 4.5]), 3.5)
        self.assertEqual(stats.mean([-1, 0, 1]), 0.0)

    def test_median(self):
        """This method tests the median function."""
        self.assertEqual(stats.median([1, 2, 3, 4, 5]), 3.0)
        self.assertEqual(stats.median([2.5, 3.5, 4.5]), 3.5)
        self.assertEqual(stats.median([-1, 0, 1]), 0.0)
        self.assertEqual(stats.median([1, 3, 2, 5, 4]), 3.0)

if __name__ == '__main__':
    unittest.main()
