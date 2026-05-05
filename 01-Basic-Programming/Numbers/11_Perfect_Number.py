def check_perfect_number(n):
    if n <= 1:
        return False
    
    div_sum = 1
    
    i = 2
    while i * i <= n:
        if n % i == 0:
            div_sum += i
            if i * i != n:
                div_sum += n // i
        i += 1
        
    return div_sum == n
