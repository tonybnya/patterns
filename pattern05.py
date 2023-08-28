# pylint: disable=all
"""
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


n = 5
pattern(n)
