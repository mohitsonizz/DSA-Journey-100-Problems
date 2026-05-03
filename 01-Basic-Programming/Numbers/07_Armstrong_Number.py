def is_armstrong(n):
    if n < 0:
        return False

    power = len(str(num_str))
    total_sum = 0
    temp = n
    
    while temp_n > 0:
        digit = temp % 10
        total_sum += digit ** power
        temp //= 10
        
    return total_sum == n
