from unittest import TestCase
from AlphabetSymmetry.alphabet_symmetry import symmetry


class TestSymmetry(TestCase):
    def test_symmetry_1(self):
        assert symmetry(["abode","ABc","xyzD"]) == [4, 3, 1]

    def test_symmetry_2(self):
        assert symmetry(["abide","ABc","xyz"]) == [4, 3, 0]

    def test_symmetry_3(self):
        assert symmetry(["IAMDEFANDJKL","thedefgh","xyzDEFghijabc"]) == [6, 5, 7]

    def test_symmetry_3(self):
        assert symmetry(["encode","abc","xyzD","ABmD"]) == [1, 3, 1, 3]
