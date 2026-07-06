"""This module is for testing mymodule.py."""
import unittest
from mymodule import *

class TestMyModule(unittest.TestCase):
    """This class is for testing mymodule.py."""
    def test_square(self):
        """This method tests the square function."""
        self.assertEqual(square(2), 4)
        self.assertEqual(square(3.0), 9.0)
        self.assertNotEqual(square(-3), -9)

    def test_double(self):
        """This method tests the double function."""
        self.assertEqual(double(2), 4)
        self.assertEqual(double(3.1), 6.2)
        self.assertEqual(double(0), 0)

    def test_add(self):
        """This method tests the add function."""
        self.assertEqual(add(2, 4), 6)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(2.3, 3.6), 5.9)
        self.assertEqual(add('hello', 'world'), 'helloworld')
        self.assertEqual(add(2.3000, 4.3000), 6.6)
        self.assertNotEqual(add(-2, -2), 0)

if __name__ == "__main__":
    unittest.main()
