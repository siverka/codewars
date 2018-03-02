from unittest import TestCase
from ReOcurringSequence.sequence_re_occuring import is_reoccuring


class TestIsReoccuring(TestCase):
    def test_is_reoccuring_1(self):
        assert is_reoccuring([0, 0, 1, 1, 0, 0])

    def test_is_reoccuring_2(self):
        assert is_reoccuring([0, 0, 'a', 0])

    def test_is_reoccuring_3(self):
        assert is_reoccuring([0, 0, 1, 1, 2, 2, 1, 1])

    def test_is_reoccuring_4(self):
        assert not is_reoccuring([0, 0, 0])

    def test_is_reoccuring_5(self):
        assert not is_reoccuring([0, 0, 1, 1, 2, 2])
