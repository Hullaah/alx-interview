#!/usr/bin/python3
"""
Implements the pascal_triangle function which
generates the pascal triangle sequence.
"""


def factorial(n):
    """Computes factorial of n
    """
    if n == 0:
        return 1
    return n * factorial(n-1)


def combination(n, k):
    """Computes combination of n on k
    """
    return factorial(n) // (factorial(k) * factorial(n-k))


def pascal_triangle(n):
    """Generates pascal triangle sequence
    """
    if n <= 0:
        return []

    def pascal(n):
        if n == 0:
            return [[1]]
        return pascal(n-1) + [[combination(n, k) for k in range(n+1)]]
    return pascal(n-1)
