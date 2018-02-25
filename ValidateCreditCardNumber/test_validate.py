from unittest import TestCase
from ValidateCreditCardNumber.validate_credit_card_number import validate


class TestValidate(TestCase):
    def test_validate_1(self):
        assert validate(891) == False

    def test_validate_2(self):
        assert validate(79927398713) == True

    def test_validate_3(self):
        assert validate(79927398710) == False

    def test_validate_4(self):
        assert validate(79927398711) == False

    def test_validate_5(self):
        assert validate(79927398712) == False

    def test_validate_6(self):
        assert validate(79927398714) == False

    def test_validate_7(self):
        assert validate(2543) == True

    def test_validate_8(self):
        assert validate(2741) == True

    def test_validate_9(self):
        assert validate(2841) == False

