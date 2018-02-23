"""
https://www.codewars.com/kata/simple-frequency-sort
In this Kata, you will sort elements in an array by decreasing frequency of elements.
If two elements have the same frequency, sort them by increasing value.

solve([2,3,5,3,7,9,5,3,7]) = [3,3,3,5,5,7,7,2,9]
--we sort by highest frequency to lowest frequency.
"""


def frequency_sort(elements: list):
    return sorted(elements, key=lambda e: (elements.count(e), -e), reverse=True)
