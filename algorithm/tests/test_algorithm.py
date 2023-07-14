# pylint: disable=C0116

import unittest
from algorithm.algorithm import *


class TestAdd(unittest.TestCase):
    def test_my_zip(self):
        self.assertEqual(my_zip([1, 2], "xy", "ab"), [
                         (1, "x", "a"), (2, "y", "b")])
        self.assertEqual(my_zip([1, 2], "x"), [(1, "x")])
        self.assertEqual(my_zip([1], "xy"), [(1, "x")])
        self.assertEqual(my_zip(), None)
        self.assertEqual(my_zip(""), [])
        self.assertEqual(my_zip("", [1]), [])
        self.assertEqual(my_zip([1], ""), [])

    def test_my_sum(self):
        self.assertEqual(my_sum([1]), 1)
        self.assertEqual(my_sum([1, 2]), 3)
        self.assertEqual(my_sum([]), 0)

    def test_qsort01(self):
        self.assertEqual(qsort01([3, 2, 1]), [1, 2, 3])
        self.assertEqual(qsort01([2, 3, 1]), [1, 2, 3])
        self.assertEqual(qsort01([1, 2, 3]), [1, 2, 3])
        self.assertEqual(qsort01([3, 2, 3, 1]), [1, 2, 3, 3])
        self.assertEqual(qsort01("abc"), ["a", "b", "c"])
        self.assertEqual(qsort01("cba"), ["a", "b", "c"])
        self.assertEqual(qsort01("bca"), ["a", "b", "c"])
        self.assertEqual(qsort01([1]), [1])
        self.assertEqual(qsort01(["a"]), ["a"])
        self.assertEqual(qsort01([]), [])
        self.assertEqual(qsort01(""), [])


if __name__ == '__main__':
    unittest.main()
