# pylint: disable=all
"""
*********
 *******
  *****
   ***
    *
"""


def pattern(n, char='*'):
    space = ' '

    for i in range(n):
        # spaces
        for j in range(i):
            print(space, end='')

        # chars
        for j in range(2 * (n - i) - 1):
            print(char, end='')

        # spaces
        for j in range(i):
            print(space, end='')

        print()
