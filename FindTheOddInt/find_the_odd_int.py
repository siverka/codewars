"""
http://www.codewars.com/kata/find-the-odd-int

Given an array, find the int that appears an odd number of times.
There will always be only one integer that appears an odd number of times.
"""


def find_it(arr: list):
    for e in set(arr):
        if arr.count(e) % 2 != 0:
            return e
    return None
