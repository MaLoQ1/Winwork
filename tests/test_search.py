import unittest
from calc.arrays import binary_search

class SearchTests(unittest.TestCase):
    def test_binary_search(self):
        values = [1, 3, 5, 7, 9]
        self.assertEqual(binary_search(values, 5), 2)
        self.assertIsNone(binary_search(values, 4))
        self.assertEqual(binary_search(values, 1), 0)