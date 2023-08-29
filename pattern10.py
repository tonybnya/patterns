# pylint: disable=all
"""
Pattern 10:

*
**
***
****
*****
****
***
**
*
"""


def pattern(n, char='*'):
    for i in range(n):
        for j in range(i + 1):
            print(char, end='')
        print()

    for i in range(n - 1):
        for j in range(n - 1 - i):
            print(char, end='')
        print()
