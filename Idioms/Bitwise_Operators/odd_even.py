"""
Check whether a number is even or odd.
"""


def odd_even(x: int) -> str:
    if x & 1:
        return "odd"
    else:
        return "even"


print(odd_even(3.4))
