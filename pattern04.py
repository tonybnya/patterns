# pylint: disable=all
"""
1
22
333
4444
55555
"""


def pattern(n, char='*'):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(i, end='')
        print()


n = 5
pattern(n)
