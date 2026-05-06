def sum_of_even(n):
     if n < 0: return 0
    k = n // 2
    return k * (k + 1)

def sum_of_odd(n):
    k = (n + 1) // 2
    return k * k

def sum_even_range(L, R):
    return sum_of_even(R) - sum_of_even(L - 1)


def sum_odd_range(L, R):
    return sum_of_odd(R) - sum_of_odd(L - 1)



