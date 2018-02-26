from unittest import TestCase
from SimpleArithmeticProgression.simple_arithmetic_progression import progressions


class TestProgressions(TestCase):
    def test_progressions_1(self):
        assert progressions([1, 2, 3, 4, 5]) == 4

    def test_progressions_1(self):
        assert progressions([1, 2, 3, 5, 7, 9]) == 5

    def test_progressions_1(self):
        assert progressions([0, 5, 8, 9, 11, 13, 14, 16, 17, 19]) == 10

    def test_progressions_1(self):
        assert progressions([0, 1, 2, 3, 5, 6, 7, 11, 13, 15, 17, 19]) == 17

    def test_progressions_1(self):
        assert progressions([0, 1, 4, 5, 7, 9, 10, 13, 15, 16, 18, 19]) == 15

    def test_progressions_1(self):
        assert progressions([0, 1, 2, 3, 5, 8, 11, 13, 14, 16, 18, 19]) == 13

