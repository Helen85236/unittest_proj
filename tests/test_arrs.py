import unittest
from utils import arrs


class SquareEqSolverTestCase(unittest.TestCase):

    def test_get(self):
        res = arrs.get([1, 2, 3], 1, "test")
        self.assertEqual(res, 2)
        res = arrs.get([], 0, "test")
        self.assertEqual(res, "test")
        res = arrs.get([], -1, "test-1")
        self.assertEqual(res, "test-1")

    def test_slice(self):
        res = arrs.my_slice([1, 2, 3, 4], 1, 3)
        self.assertEqual(res, [2, 3])
        res = arrs.my_slice([1, 2, 3], 1)
        self.assertEqual(res, [2, 3])
        res = arrs.my_slice([], 1)
        self.assertEqual(res, [])
        res = arrs.my_slice([1, 2, 3], -1)
        self.assertEqual(res, [3])
        res = arrs.my_slice([1, 2, 3], -5)
        self.assertEqual(res, [1, 2, 3])