"""Simple unittest demonstration.

Modified from https://realpython.com/python-testing/
"""
import unittest

class TestSum(unittest.TestCase):
    """Example unittest of sums."""

    def test_sum(self):
        """Check sum of a list."""
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    def test_sum_tuple(self):
        """Check sum of a tuple."""
        self.assertEqual(sum((1, 2, 3)), 6, "Should be 6")

if __name__ == '__main__':
    unittest.main()

