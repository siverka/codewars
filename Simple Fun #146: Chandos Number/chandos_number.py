"""
https://www.codewars.com/kata/simple-fun-number-146-chandos-number
The sequence of Chando is an infinite sequence of all Chando's numbers in ascending order.
A number is called Chando's if it is an integer that can be represented as a sum
of different positive integer powers of 5.
The first Chando's numbers is 5 (5^1). And the following nth Chando's numbers are:
 25  (5^2)
 30  (5^1 + 5^2)
 125 (5^3)
 130 (5^1 + 5^3)
 150 (5^2 + 5^3)
Your task is to find the Chando's nth number for a given n.
"""


def chandos(n):
    powers = [int(p) for p in bin(n)[2:]]
    return sum(i * 5 ** p for p, i in enumerate(powers[::-1], start=1))


