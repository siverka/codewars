"""
https://www.codewars.com/kata/multiples-of-3-or-5
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.
Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.
Note: If the number is a multiple of both 3 and 5, only count it once.
"""
from unittest import TestCase
from multiples_of_3_or_5 import multiples

class Test_Multiples(TestCase):
    def test_multiples_1(self):
        assert multiples(10) == 23

    def test_multiples_2(self):
        assert multiples(20) == 78
