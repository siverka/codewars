"""
https://www.codewars.com/kata/simple-string-reversal-ii
In this Kata, you will be given a string and two indexes.
Your task is to reverse the portion of that string between those two indexes inclusive.
solve("codewars",1,5) = "cawedors" -- elements at index 1 to 5 inclusive are "odewa". So we reverse them.
solve("cODEWArs", 1,5) = "cAWEDOrs" -- to help visualize.
Input will be lowercase and uppercase letters only.
"""


def reverse(word, i, j):
    return word[:i] + word[i:j+1][::-1] + word[j+1:]
