from unittest import TestCase
from FindTheOddInt.find_the_odd_int import find_it


class TestFindIt(TestCase):
    def test_find_it(self):
        assert find_it([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]) == 5
