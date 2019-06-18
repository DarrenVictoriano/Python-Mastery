"""
Primitive Types basic
Bitwise Operators
"""


def count_bits(x: int) -> int:
    num_bits = 0

    while x:
        # bitwise &, comapres binary of each int
        # ex: imgs/and_example.png
        num_bits += x & 1

        # >>= (bitwise right shift and assignment)
        x >>= 1
    return num_bits


print(count_bits(5))
