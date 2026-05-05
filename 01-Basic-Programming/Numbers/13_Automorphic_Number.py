def is_automorphic(n):
    n = abs(n)
    square = n * n
    
    temp = n
    num_of_digits = 0
    if n == 0: 
        num_of_digits = 1
    else:
        while temp > 0:
            num_of_digits += 1
            temp //= 10
            
    divisor = 10 ** num_of_digits
    last_digits = square % divisor
    
    return last_digits == n
