# pylint: disable=C0116

import pytest
from algorithm.algorithm import *


class TestAdd:
    def test_my_zip(self):
        assert my_zip([1, 2], "xy", "ab") == [(1, "x", "a"), (2, "y", "b")]
        assert my_zip([1, 2], "x") == [(1, "x")]
        assert my_zip([1], "xy") == [(1, "x")]
        assert my_zip() is None
        assert my_zip("") == []
        assert my_zip("", [1]) == []
        assert my_zip([1], "") == []

    def test_my_sum(self):
        assert my_sum([1]) == 1
        assert my_sum([1, 2]) == 3
        assert my_sum([]) == 0

    def test_qsort01(self):
        assert qsort01([3, 2, 1]) == [1, 2, 3]
        assert qsort01([2, 3, 1]) == [1, 2, 3]
        assert qsort01([1, 2, 3]) == [1, 2, 3]
        assert qsort01([3, 2, 3, 1]) == [1, 2, 3, 3]
        assert qsort01("abc") == ["a", "b", "c"]
        assert qsort01("cba") == ["a", "b", "c"]
        assert qsort01("bca") == ["a", "b", "c"]
        assert qsort01([1]) == [1]
        assert qsort01(["a"]) == ["a"]
        assert qsort01([]) == []
        assert qsort01("") == []

    def test_product(self):
        assert product([1, 2, 3]) == 6
        assert product([4, 5, 0]) == 0
        assert product([1]) == 1
        assert product([]) == 1

    def test_my_last(self):
        assert my_last([1, 2, 3]) == 3
        assert my_last([1, 2]) == 2
        assert my_last([1]) == 1
        with pytest.raises(ValueError):
            my_last([])

    def test_halve(self):
        assert ([1], [2]) == halve([1, 2])
        assert ([1, 2], [3, 4]) == halve([1, 2, 3, 4])
        with pytest.raises(ValueError):
            halve([])
        with pytest.raises(ValueError):
            halve([1])
        with pytest.raises(ValueError):
            halve([1, 2, 3])
