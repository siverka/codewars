from unittest import TestCase
from MissingNumberInUnorderedArithmeticProgression.missing_number_in_unordered_arithmetic_progression import find


class TestFind(TestCase):
    def test_find_1(self):
        assert find([3, 9, 1, 11, 13, 5]) == 7

    def test_find_2(self):
        assert find([7, 9, 1, 11, 13, 5]) == 3

    def test_find_3(self):
        assert find([5, -1, 0, 3, 4, -3, 2, -2]) == 1
