"""
https://www.codewars.com/kata/simple-number-triangle

Consider the number triangle below, in which each number is equal to
the number above plus the number to the left. If there is no number above,
assume the number above is a 0.

1
1 1
1 2 2
1 3 5 5
1 4 9 14 14
The triangle has 5 rows and the sum of the last row is sum([1,4,9,14,14]) = 42.
You will given an integer n and your task will be to return the sum of the last row of a triangle of n-rows.
In the example above:
solve(5) = 42.
"""


def triangle(n):
    if n == 1:
        return 1

    res = []
    for i in range(n):
        res.append([0 for _ in range(n)])
        for j in range(n):
            if j == 0:
                res[i][j] = 1
            if j <= i:
                res[i][j] = res[i][j-1] + res[i-1][j]
    #
    # for e in res:
    #     print(*e)

    return sum(res[-1])
