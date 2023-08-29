# pylint: disable=all
"""
Pattern 20:

*        *
**      **
***    ***
****  ****
**********
****  ****
***    ***
**      **
*        *
"""


def pattern(n, char='*'):
    space = ' '

    for i in range(1, n + 1):
        # stars
        for j in range(i):
            print(char, end='')

        # spaces
        for j in range(n - 1 - i):
            print(space, end='')

        # stars
        for j in range(i):
            print(char, end='')

        print()
