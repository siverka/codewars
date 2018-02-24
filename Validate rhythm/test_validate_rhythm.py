from unittest import TestCase
from validate_rhythm import validate_rhythm


class TestValidate_rhythm(TestCase):
    def test_validate_rhythm_01(self):
        assert validate_rhythm([4, 4], '4444|88888888|22|2488|1') == 'Valid rhythm'

    def test_validate_rhythm_02(self):
        assert validate_rhythm([5, 2], '22222|2244244|8888244888844|112') == 'Valid rhythm'

    def test_validate_rhythm_03(self):
        assert validate_rhythm([3, 8], '888|48|84') == 'Valid rhythm'

    def test_validate_rhythm_04(self):
        assert validate_rhythm([4, 4], '4444') == 'Valid rhythm'

    def test_validate_rhythm_05(self):
        assert validate_rhythm([5, 2], '22222') == 'Valid rhythm'

    def test_validate_rhythm_06(self):
        assert validate_rhythm([1, 4], '4') == 'Valid rhythm'

    def test_validate_rhythm_07(self):
        assert validate_rhythm([3, 8], '888') == 'Valid rhythm'

    def test_validate_rhythm_08(self):
        assert validate_rhythm([4, 4], '44|4444|884884|22|1|44') == 'Valid rhythm with anacrusis'

    def test_validate_rhythm_09(self):
        assert validate_rhythm([5, 2], '222|1144|41188|22') == 'Valid rhythm with anacrusis'

    def test_validate_rhythm_10(self):
        assert validate_rhythm([3, 8], '88|48|84|8') == 'Valid rhythm with anacrusis'

    def test_validate_rhythm_11(self):
        assert validate_rhythm([4, 4], '44|11|224|44') == 'Invalid rhythm'

    def test_validate_rhythm_12(self):
        assert validate_rhythm([5, 2], '222|111|222222|22') == 'Invalid rhythm'

    def test_validate_rhythm_13(self):
        assert validate_rhythm([3, 8], '8|8888|448|88') == 'Invalid rhythm'

    def test_validate_rhythm_14(self):
        assert validate_rhythm([4, 4], '|11|224|4444') == 'Invalid rhythm'

    def test_validate_rhythm_15(self):
        assert validate_rhythm([5, 2], '2288888244|111|222222|') == 'Invalid rhythm'

    def test_validate_rhythm_16(self):
        assert validate_rhythm([3, 8], '|884|888|') == 'Invalid rhythm'

    def test_validate_rhythm_17(self):
        assert validate_rhythm([4, 4], '444|22|1|244') == 'Invalid rhythm'

    def test_validate_rhythm_18(self):
        assert validate_rhythm([5, 2], '111|222222|888') == 'Invalid rhythm'

    def test_validate_rhythm_19(self):
        assert validate_rhythm([3, 8], '444|888|1') == 'Invalid rhythm'

    def test_validate_rhythm_20(self):
        assert validate_rhythm([7, 3], '222|111|2222222|1112|2222') == 'Invalid rhythm'

    def test_validate_rhythm_21(self):
        assert validate_rhythm([1, 3], '2|44|22') == 'Invalid rhythm'

    def test_validate_rhythm_22(self):
        assert validate_rhythm([9, 9], '444448|2288') == 'Invalid rhythm'

    def test_validate_rhythm_23(self):
        assert validate_rhythm([3, 3], '333|333|333') == 'Invalid rhythm'

    def test_validate_rhythm_24(self):
        assert validate_rhythm([5, 7], '777|77777|77') == 'Invalid rhythm'

    def test_validate_rhythm_25(self):
        assert validate_rhythm([2, 6], '66|66|66|66|66') == 'Invalid rhythm'
