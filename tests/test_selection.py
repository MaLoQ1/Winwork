import unittest
from calc.selection import statistic

class StatisticTests(unittest.TestCase):
    def test_basic(self):
        values = [12, 71, 35, 80, 61, 50, 87, 11, 20]
        self.assertEqual(statistic(values[:], 1, seed=1), 11)
        self.assertEqual(statistic(values[:], 4, seed=1), 35)
        self.assertEqual(statistic(values[:], 9, seed=1), 87)

    def test_duplicates(self):
        values = [5, 2, 2, 9]
        self.assertEqual(statistic(values[:], 2, seed=1), 2)

    def test_invalid_rank(self):
        with self.assertRaises(ValueError):
            statistic([1, 2, 3], 0)
        with self.assertRaises(ValueError):
            statistic([1, 2, 3], 4)
        with self.assertRaises(ValueError):
            statistic([], 1)
        with self.assertRaises(ValueError):
            statistic([1, 2, 3], 1.5)
        with self.assertRaises(ValueError):
            statistic([1, 2, 3], True)

    def test_all_ranks(self):
        original = [5, -1, 2, 2]
        expected = sorted(original)
        for k in range(1, len(original) + 1):
            with self.subTest(k=k):
                values = original[:]
                result = statistic(values, k, seed=1)
                self.assertEqual(result, expected[k - 1])
                self.assertEqual(sorted(values), expected)