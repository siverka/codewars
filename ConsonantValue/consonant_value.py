"""
https://www.codewars.com/kata/consonant-value

A consonant is any letter of the alphabet except a, e, i ,o, u.
The consonant substrings in the word "zodiacs" are z, d, cs.
Assuming a = 1, b = 2 ... z = 26, the values of these substrings
are 26 ,4, 22 because z = 26,d = 4,cs=3+19=22. The maximum value
of these substrings is 26. Therefore, solve("zodiacs") = 26.                                                

Given a lowercase string that has alphabetic characters only and
no spaces, return the highest value of consonant substrings.
"""


from string import ascii_lowercase
letters = {w: i for i, w in enumerate(ascii_lowercase, start=1)}


def consonant_value(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    v, values = 0, []
    for w in string:
        if w not in vowels:
            v += letters[w]
        else:
            values.append(v)
            v = 0

    return max(values)

