from unittest import TestCase
from isograms import is_isogram


class Test_Is_isogram(TestCase):
    def test_is_isogram_1(self):
        assert is_isogram('')

    def test_is_isogram_2(self):
        assert is_isogram("Dermatoglyphics")

    def test_is_isogram_3(self):
        assert not is_isogram('aba')

    def test_is_isogram_4(self):
        assert not is_isogram('moOse')
