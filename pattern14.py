# pylint: disable=all
"""
Pattern 14:

A
AB
ABC
ABCD
ABCDE
"""


def pattern(n, char='*'):
    asc = 65

    for i in range(1, n + 1):
        for j in range(i):
            print(chr(asc + j), end='')
        print()
