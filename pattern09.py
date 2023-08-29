# pylint: disable=all
"""
Pattern 09:

    *
   ***
  *****
 *******
*********
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
        for j in range(n - i - 1):
            print(space, end='')

        # chars
        for j in range(i * 2 + 1):
            print(char, end='')

        # spaces
        for j in range(n - i - 1):
            print(space, end='')

        print()

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
