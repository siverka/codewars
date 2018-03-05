from unittest import TestCase
from CreatePhoneNumber.create_phone_number import create_phone_number


class TestCreatePhoneNumber(TestCase):
    def test_create_phone_number_1(self):
        assert create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == "(123) 456-7890"

    def test_create_phone_number_2(self):
        assert create_phone_number([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == "(111) 111-1111"

    def test_create_phone_number_3(self):
        assert create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == "(123) 456-7890"

    def test_create_phone_number_4(self):
        assert create_phone_number([0, 2, 3, 0, 5, 6, 0, 8, 9, 0]) == "(023) 056-0890"

    def test_create_phone_number_5(self):
        assert create_phone_number([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == "(000) 000-0000"
