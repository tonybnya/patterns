# pylint: disable=all
"""
Pattern 01:

*****
*****
*****
*****
*****
"""


def pattern(n, char='*'):
    for i in range(n):
        for j in range(n):
            print(char, end='')
        print()
