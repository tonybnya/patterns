# pylint: disable=all
"""
E
DE
CDE
BCDE
ABCDE
"""


def pattern(n, char='*'):
    start = 69

    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(chr(start - i + j), end='')
        print()


n = 5
pattern(n)
