"""
https://www.codewars.com/kata/mumbling
This time no story, no theory. The examples below show you how to write function accum:
Examples:
accum("abcd")    # "A-Bb-Ccc-Dddd"
accum("RqaEzty") # "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt")    # "C-Ww-Aaa-Tttt"
"""


def accum(word):
    return  '-'.join(w.upper()+ i*w.lower() for i, w in enumerate(word))
