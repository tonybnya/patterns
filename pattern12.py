# pylint: disable=all
"""
1        1
12      21
123    321
1234  4321
1234554321
"""


def pattern(n, char='*'):
    space = ' '

    for i in range(1, n + 1):
        # numbers
        start = 1
        for j in range(i):
            print(start, end='')
            start += 1

        # spaces
        for j in range(n * 2 - i * 2):
            print(space, end='')

        # numbers
        start = i
        for j in range(i):
            print(start, end='')
            start -= 1

        print()


n = 5
pattern(n)
