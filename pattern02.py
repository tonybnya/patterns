# pylint: disable=all
"""
*
**
***
****
*****
"""


def pattern(n, char='*'):
    for i in range(1, n + 1):
        for j in range(i):
            print(char, end='')
        print()


n = 5
pattern(n)
