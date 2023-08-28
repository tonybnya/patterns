# pylint: disable=all
"""
1
01
101
0101
10101
"""


def pattern(n, char='*'):
    for i in range(n):
        if i % 2 != 0:
            start = 0
        else:
            start = 1

        for j in range(i + 1):
            print(start, end='')

            if start == 1:
                start = 0
            else:
                start = 1

        print()
