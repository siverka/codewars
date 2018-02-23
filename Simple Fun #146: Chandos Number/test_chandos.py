from unittest import TestCase
from chandos_number import chandos


class TestChandos(TestCase):
    def test_chandos_1(self):
        assert chandos(1) == 5

    def test_chandos_2(self):
        assert chandos(2) == 25

    def test_chandos_3(self):
        assert chandos(3) == 30

    def test_chandos_4(self):
        assert chandos(4) == 125

    def test_chandos_5(self):
        assert chandos(5) == 130

    def test_chandos_6(self):
        assert chandos(9) == 630

    def test_chandos_6(self):
        assert chandos(19) == 3155

    def test_chandos_6(self):
        assert chandos(23) == 3280

    def test_chandos_6(self):
        assert chandos(123) == 97530
