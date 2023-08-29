# pylint: disable=all
"""
Pattern 06:

12345
1234
123
12
1
"""


def pattern(n, char='*'):
    for i in range(n):
        for j in range(1, n - i + 1):
            print(j, end='')
        print()
