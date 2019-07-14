# the parity of a binary work is 1 if the number
# of 1s in the word is odd; otherwise, it is 0.


def parity_me(x: int) -> int:
    count = 0
    while x:
        if x & 1:
            count += 1
        x >>= 1
    print(count)
    if count % 2:
        return 1
    else:
        return 0


def parity_book(x):
    result = 0
    while x:
        print(f'res: {result} ^= {"{0:b}".format(x)} & 1')
        print(f'res: {result} ^= {x & 1}')
        result ^= x & 1
        print(f'res: {result}')
        x >>= 1
    return result


print("{0:b}".format(35))
# print(f'res: {parity_me(39)}')
print(f'res2: {parity_book(35)}')
