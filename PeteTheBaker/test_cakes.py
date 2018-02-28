from unittest import TestCase
from PeteTheBaker.pete_the_baker import cakes


class TestCakes(TestCase):
    def test_cakes_1(self):
        recipe = {"flour": 500, "sugar": 200, "eggs": 1}
        available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
        assert cakes(recipe, available) == 2

    def test_cakes_2(self):
        recipe = {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}
        available = {"sugar": 500, "flour": 2000, "milk": 2000}
        assert cakes(recipe, available) == 0

