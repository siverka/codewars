from unittest import TestCase
from PeakArrayIndex.peak_array_index import peak


class TestPeak(TestCase):
    def test_peak_1(self):
        assert peak([1, 2, 3, 5, 3, 2, 1]) == 3

    def test_peak_2(self):
        assert peak([1, 12, 3, 3, 6, 3, 1]) == 2

    def test_peak_3(self):
        assert peak([10, 20, 30, 40]) == -1

