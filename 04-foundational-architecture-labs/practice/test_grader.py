"""This module is to test grader.py using unittest."""
import unittest
from grader import calculate_grade

class TestGrader(unittest.TestCase):
    """This class is to test grader.py using unittest."""
    def test_calculate_grade(self):
        """This method tests the calculate_grade function."""
        self.assertEqual(calculate_grade(90), 'A')
        self.assertEqual(calculate_grade(80), 'B')
        self.assertEqual(calculate_grade(0), 'F')
        self.assertEqual(calculate_grade(100), 'A')
        self.assertEqual(calculate_grade(-80), 'Invalid score')

if __name__ == "__main__":
    unittest.main()
