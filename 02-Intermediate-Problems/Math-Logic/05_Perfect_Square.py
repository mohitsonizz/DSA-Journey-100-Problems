import math

def is_perfect_square_fast(n):
    if n < 0:
        return False
    root = math.isqrt(n)
    return root * root == n
