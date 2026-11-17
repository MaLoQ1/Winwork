import unittest
from calc.arrays import shuffle

class ShuffleTests(unittest.TestCase):
    def test_composition(self):
        original = [2, 2, -1, 5]
        values = original[:]
        result = shuffle(values, seed=1)
        self.assertIsNone(result)
        self.assertEqual(sorted(values), sorted(original))

    def test_empty_and_single(self):
        values = []
        shuffle(values)
        self.assertEqual(values, [])
        
        values = [1]
        shuffle(values)
        self.assertEqual(values, [1])

    def test_reproducibility(self):
        original = [1, 2, 3, 4, 5]
        v1 = original[:]
        v2 = original[:]
        shuffle(v1, seed=42)
        shuffle(v2, seed=42)
        self.assertEqual(v1, v2)