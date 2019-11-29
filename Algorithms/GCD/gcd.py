"""
Greatest Common Divisor or GCD
To solve this we use The Euclidean Algorithm
"""


def gcd_recursive(a: int, b: int) -> int:
    """ Recuriosn """
    if b == 0:
        return a
    else:
        return gcd_recursive(b, a % b)


def gcd_euclidean(a: int, b: int) -> int:
    """ Euclidean Algorithm"""
    while b:
        a, b = b, a % b

    return a


x = gcd_euclidean(270, 192)
print(x)
