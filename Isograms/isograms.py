"""
https://www.codewars.com/kata/54ba84be607a92aa900000f1
An isogram is a word that has no repeating letters, consecutive or non-consecutive.
Implement a function that determines whether a string that contains only letters is an isogram.
Assume the empty string is an isogram. Ignore letter case.
"""

from unittest import TestCase


def is_isogram(word: str):
    word = word.lower()
    if not word:
        return True
    else:
        return len(set(word)) == len(word)


class Test_Is_isogram(TestCase):
    def test_is_isogram_1(self):
        assert is_isogram('')

    def test_is_isogram_2(self):
        assert is_isogram("Dermatoglyphics")

    def test_is_isogram_3(self):
        assert not is_isogram('aba')

    def test_is_isogram_4(self):
        assert not is_isogram('moOse')
