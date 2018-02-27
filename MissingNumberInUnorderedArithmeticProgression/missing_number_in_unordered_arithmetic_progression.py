"""
https://www.codewars.com/kata/missing-number-in-unordered-arithmetic-progression

You are provided with consecutive elements of an Arithmetic Progression.
There is however one hitch: exactly one term from the original series is missing
from the set of numbers which have been given to you. The rest of the given
series is the same as the original AP. Find the missing term.
And here is an unordered version. Try if you can survive lists of MASSIVE numbers
(which means time limit should be considered).

Note: Don't be afraid that the minimum or the maximum element in the list is missing, e.g. [4, 6, 3, 5, 2] is missing 1 or 7, but this case is excluded from the kata.
find([3, 9, 1, 11, 13, 5]) # => 7
"""


def find(arr: list):
    arr.sort()
    d = arr[1] - arr[0]
    for i in range(len(arr)):
        t = arr[i + 1] - arr[i]
        if t == d:
            continue
        elif t > d:
            return arr[0] + d * (i + 1)
        else:
            return arr[0] + t * i
