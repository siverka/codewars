"""
https://www.codewars.com/kata/simple-arithmetic-progression/

In this Kata, you will be given an array of integers and your task is
to return the number of arithmetic progressions of size 3 that are possible from that list.
In each progression, the differences between the elements must be the same.
solve([1,2,3,5,7,9]) = 5, as follows: [1,2,3], [1,3,5],[1,5,9],[3,5,7], and [5,7,9].
All inputs will be sorted.
"""


def n_progressions(e, arr):
    diffs = [obj - e for obj in arr]
    return sum(2 * d in diffs for d in diffs)


def progressions(arr):
    return sum(n_progressions(e, arr[i + 1:]) for i, e in enumerate(arr[:-2]))
