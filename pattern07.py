# pylint: disable=all
"""
Pattern 07:

    *
   ***
  *****
 *******
*********
"""


def pattern(n, char='*'):
    space = ' '

    for i in range(n):
        # spaces
        for j in range(n - i - 1):
            print(space, end='')

        # chars
        for j in range(2 * i + 1):
            print(char, end='')

        # spaces
        for j in range(n - i - 1):
            print(space, end='')

        print()


pattern(5)
