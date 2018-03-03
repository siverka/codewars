from unittest import TestCase
from SimpleNumberTriangle.simple_number_triangle import triangle


class TestTriangle(TestCase):
    def test_triangle_1(self):
        assert triangle(1) == 1

    def test_triangle_1(self):
        assert triangle(4) == 14

    def test_triangle_1(self):
        assert triangle(5) == 42

    def test_triangle_1(self):
        assert triangle(6) == 132

    def test_triangle_1(self):
        assert triangle(7) == 429

    def test_triangle_1(self):
        assert triangle(8) == 1430

    def test_triangle_1(self):
        assert triangle(20) == 6564120420
