from unittest import TestCase
from ConsonantValue.consonant_value import consonant_value


class TestConsonantValue(TestCase):
    def test_consonant_value_1(self):
        assert consonant_value("zodiac") == 26

    def test_consonant_value_2(self):
        assert consonant_value("chruschtschov") == 80

    def test_consonant_value_3(self):
        assert consonant_value("khrushchev") == 38

    def test_consonant_value_4(self):
        assert consonant_value("strength") == 57

    def test_consonant_value_5(self):
        assert consonant_value("catchphrase") == 73

    def test_consonant_value_6(self):
        assert consonant_value("twelfthstreet") == 103

    def test_consonant_value_7(self):
        assert consonant_value("mischtschenkoana") == 80
