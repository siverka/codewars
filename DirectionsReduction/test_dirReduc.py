from unittest import TestCase
from DirectionsReduction.directions_reduction import dirReduc


class TestDirReduc(TestCase):
    def test_dirReduc_1(self):
        assert dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]) == ["WEST"]

    def test_dirReduc_2(self):
        assert dirReduc(["NORTH", "SOUTH", "EAST", "WEST"]) == []

    def test_dirReduc_3(self):
        assert dirReduc(["NORTH", "EAST", "WEST", "SOUTH", "WEST", "WEST"]) == ["WEST", "WEST"]

    def test_dirReduc_4(self):
        assert dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]) == ["WEST"]

    def test_dirReduc_5(self):
        assert dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH"]) == []

    def test_dirReduc_6(self):
        assert dirReduc(["NORTH", "WEST", "SOUTH", "EAST"]) == ["NORTH", "WEST", "SOUTH", "EAST"]

    def test_dirReduc_7(self):
        assert dirReduc(["NORTH", "WEST", "SOUTH", "EAST"]) == ["NORTH", "WEST", "SOUTH", "EAST"]

