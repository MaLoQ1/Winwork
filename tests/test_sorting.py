import unittest
from calc.sorting import METHODS

class SortingTests(unittest.TestCase):
    def test_all_methods(self):
        original = [5, -1, 2, 2, 0]
        for method_name, method_func in METHODS.items():
            for descending in [False, True]:
                with self.subTest(method=method_name, desc=descending):
                    values = original[:]
                    result = method_func(values, descending)
                    self.assertIsNone(result)
                    self.assertEqual(values, sorted(original, reverse=descending))