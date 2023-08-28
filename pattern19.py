# pylint: disable=all
"""
**********
****  ****
***    ***
**      **
*        *
*        *
**      **
***    ***
****  ****
**********
"""


def pattern(n, char='*'):
    space = ' '

    for i in range(n):
        # stars
        for j in range(n - i):
            print(char, end='')

        # spaces
        for j in range(i * 2):
            print(space, end='')

        # stars
        for j in range(n - i):
            print(char, end='')

        print()

    for i in range(n):
        # stars
        for j in range(i + 1):
            print(char, end='')

        # spaces
        for j in range(2 * (n - i) - 2):
            print(space, end='')

        # stars
        for j in range(i + 1):
            print(char, end='')

        print()
