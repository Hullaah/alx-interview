import math


def pascal_triangle(n):
    if n <= 0:
        return []

    def pascal(n):
        if n == 0:
            return [[1]]
        return pascal(n-1) + [[math.comb(n, k) for k in range(n+1)]]
    return pascal(n-1)
