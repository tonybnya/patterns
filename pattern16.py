# pylint: disable=all
"""
Pattern 16:

A
BB
CCC
DDDD
EEEEE
"""


def pattern(n, char='*'):
    asc = 65

    for i in range(n):
        for j in range(i + 1):
            print(chr(asc + i), end='')
        print()
