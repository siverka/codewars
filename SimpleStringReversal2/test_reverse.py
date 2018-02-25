from unittest import TestCase
from SimpleStringReversal2.simple_string_reversal_ii import reverse


class TestReverse(TestCase):
    def test_reverse_1(self):
        assert reverse("codewars", 1, 5) == "cawedors"

    def test_reverse_2(self):
        assert reverse("codingIsFun", 2, 100) == "conuFsIgnid"

    def test_reverse_3(self):
        assert reverse("FunctionalProgramming", 2, 15) == "FuargorPlanoitcnmming"

    def test_reverse_4(self):
        assert reverse("abcefghijklmnopqrstuvwxyz", 0, 20) == "vutsrqponmlkjihgfecbawxyz"

    def test_reverse_5(self):
        assert reverse("abcefghijklmnopqrstuvwxyz", 5, 20) == "abcefvutsrqponmlkjihgwxyz"
