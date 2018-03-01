"""
http://www.codewars.com/kata/simple-fun-number-120-range-collapse-representation

A range-collapse representation of an array of integers looks like this: "1,3-6,8",
where 3-6 denotes the range from 3-6, i.e. [3,4,5,6].

Hence "1,3-6,8" = [1,3,4,5,6,8]. Some other range-collapse representations of [1,3,4,5,6,8]
include "1,3-5,6,8", "1,3,4,5,6,8", etc.

Each range is written in the following format "a-b", where a < b, and the whole range
must belong to the array in an increasing order.
You are given an array arr. Your task is to find the number of different
range-collapse representations of the given array.

Example
For arr = [1,3,4,5,6,8], the result should be 8.

 "1,3-4,5,6,8"
 "1,3-4,5-6,8"
 "1,3-5,6,8"
 "1,3-6,8"
 "1,3,4-5,6,8"
 "1,3,4-6,8"
 "1,3,4,5-6,8"
 "1,3,4,5,6,8"

Input/OutPut
[input] integer array arr - sorted array of different positive integers.
[output] an integer - the number of different range-collapse representations of the given array.
"""

from math import factorial
from functools import reduce


def num_of_comb(k, n):
    return int(factorial(n) / factorial(k) / factorial(n-k))


def num_of_repr(lst: list):
    n = len(lst)
    return 1 if n == 1 else sum(num_of_comb(i, n-1) for i in range(n))


def descriptions(arr):
    stack, result = [], []
    for i in range(len(arr)):
        stack.append(i)
        if i == len(arr) - 1 or arr[i+1] != arr[i] + 1:
            result.append(stack)
            stack = []
    combs = [num_of_repr(e) for e in result]
    return reduce(lambda x, y: x*y, combs)
