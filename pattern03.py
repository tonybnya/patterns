# pylint: disable=all
"""
1
12
123
1234
12345
"""


def pattern(n, char='*'):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end='')
        print()


n = 5
pattern(n)
