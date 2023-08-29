# pylint: disable=all
"""
Pattern 13:

1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
"""


def pattern(n, char='*'):
    start = 1

    for i in range(1, n + 1):
        for j in range(i):
            print(f'{start} ', end='')
            start += 1
        print()
