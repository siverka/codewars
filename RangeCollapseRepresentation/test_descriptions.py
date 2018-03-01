from unittest import TestCase
from RangeCollapseRepresentation.range_collapse_representation import descriptions


class TestDescriptions(TestCase):
    def test_descriptions_1(self):
        assert descriptions([1, 3, 4, 5, 6, 8]) == 8

    def test_descriptions_2(self):
        assert descriptions([1, 2, 3]) == 4

    def test_descriptions_3(self):
        assert descriptions([11, 43, 66, 123]) == 1

    def test_descriptions_4(self):
        assert descriptions([3, 4, 5, 8, 9, 10, 11, 23, 43, 66, 67]) == 64
