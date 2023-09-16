# pylint: disable=all
"""
Pattern 22:

555555555
544444445
543333345
543222345
543212345
543222345
543333345
544444445
555555555
"""


def pattern(n, char='*'):
    for i in range(1, n * 2):
        for j in range(1, n * 2):
            pass


pattern(5)
