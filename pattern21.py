# pylint: disable=all
"""
Pattern 21:

*****
*   *
*   *
*   *
*****
"""


def pattern(n, char='*'):
    space = ' '

    for i in range(n):
        if i == 0 or i == n - 1:
            for j in range(n):
                print(char, end='')
        else:
            # stars
            print(char, end='')

            # spaces
            for j in range(n - 2):
                print(space, end='')

            # stars
            print(char, end='')

        print()


pattern(9)
