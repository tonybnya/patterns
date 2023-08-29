# pylint: disable=all
"""
    A
   ABA
  ABCBA
 ABCDCBA
ABCDEDCBA
"""


def pattern(n, char='*'):
    space = ' '

    for i in range(n):
        # spaces
        for j in range(n - i - 1):
            print(space, end='')

        # letters
        for j in range(i * 2 + 1):
            asc = 65

            if j <= i:
                code = asc + j
                print(chr(code), end='')
            else:
                code -= 1
                print(chr(code), end='')

        # spaces
        for j in range(n - i - 1):
            print(space, end='')

        print()
