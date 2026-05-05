def is_harshad_number(n):
    if n <= 0:
        return False
    
    original_num = n
    sum_of_digits = 0
    
    temp = n
    while temp > 0:
        digit = temp % 10
        sum_of_digits += digit
        temp //= 10
        
    return original_num % sum_of_digits == 0
