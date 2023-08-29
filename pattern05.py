# pylint: disable=all
"""
Pattern 05:

*****
****
***
**
*
"""


def pattern(n, char='*'):
    for i in range(n):
        for j in range(n - i):
            print(char, end='')
        print()
