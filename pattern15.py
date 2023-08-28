# pylint: disable=all
"""
ABCDE
ABCD
ABC
AB
A
"""


def pattern(n, char='*'):
    asc = 65

    for i in range(n):
        for j in range(n - i):
            print(chr(asc + j), end='')
        print()
