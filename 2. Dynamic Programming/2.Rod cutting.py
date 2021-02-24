"""
The rod-cutting problem is the following. Given a rod of length n inches and a table of prices pi for i = 1, 2, 3, ..., n.
determine the maximum revenue rn obtain- able by cutting up the rod and selling the pieces.
Note that if the price pn for a rod of length n is large enough, an optimal solution may require no cutting at all.
Consider the case when n = 4. Figure 15.2 shows all the ways to cut up a rod of 4 inches in length,
including the way with no cuts at all.
"""
import collections
import math

Item = collections.namedtuple('Item', ['length', 'price'])


def cuttingRod(p, n):
    print("Hii")
    r = [0] * (n + 1)
    r[0] = 0

    for j in range(1, n + 1):
        for i in range(1, j + 1):
            value = p[i - 1] + r[j - i]
            r[j] = max(r[j],  value)
    return r[n]


tests = [
    {
        'correct_output': 10,
        'input':
            {
                'rod_length': 4,
                'items': [Item(1, 1), Item(2, 5), Item(3, 8), Item(4, 9), Item(5, 10), Item(6, 17),
                          Item(7, 17), Item(8, 20), Item(9, 24), Item(10, 30)]
            }
    }
]

prices = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]

for test in tests:
    assert test['correct_output'] == cuttingRod(prices, 4)
