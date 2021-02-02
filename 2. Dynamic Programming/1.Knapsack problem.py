"""
Knapsack Problem
Now that you know the dynamic programming, it's time to implement it. Assume you are given two things:

1. The items, each having its associated weight (kg) and value ( $ ).
2. A knapsack that can hold a maximum weight of knapsack_max_weight (kg).

Use dynamic programming to implement the function knapsack_max_value() to return the maximum total value of items
that can be accommodated into the given knapsack.

Note - The items variable is the type Item, which is a named tuple.
"""

import collections

Item = collections.namedtuple('Item', ['weight', 'value'])


# DP Solution
def knapsack_max_value(knapsack_max_weight, items):
    lookup_table = [0] * (knapsack_max_weight + 1)

    for item in items:

        for capacity in reversed(range(knapsack_max_weight + 1)):
            if item.weight > capacity:
                break
            else:
                lookup_table[capacity] = max(lookup_table[capacity], lookup_table[capacity - item.weight] + item.value)

    return lookup_table[-1]


tests = [
    {
        'correct_output': 14,
        'input':
            {
                'knapsack_max_weight': 15,
                'items': [Item(10, 7), Item(9, 8), Item(5, 6)]}},
    {
        'correct_output': 13,
        'input':
            {
                'knapsack_max_weight': 25,
                'items': [Item(10, 2), Item(29, 10), Item(5, 7), Item(5, 3), Item(5, 1), Item(24, 12)]}}]
for test in tests:
    assert test['correct_output'] == knapsack_max_value(**test['input'])
