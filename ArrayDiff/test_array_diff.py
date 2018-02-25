from unittest import TestCase
from ArrayDiff.array_diff import array_diff


class TestArrayDiff(TestCase):
    def test_array_diff(self):
        assert array_diff([1,2], [1]) == [2]

    def test_array_diff(self):
        assert array_diff([1,2,2], [1]) == [2,2]

    def test_array_diff(self):
        assert array_diff([1,2,2], [2]) == [1]

    def test_array_diff(self):
        assert array_diff([1,2,2], []) == [1,2,2]

    def test_array_diff(self):
        assert array_diff([], [1,2]) == []
