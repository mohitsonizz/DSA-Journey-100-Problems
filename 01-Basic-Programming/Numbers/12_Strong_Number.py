def check_strong_number(n):
  
    fact = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
    
    original_n = n
    sum_of_facts = 0
    
    if n == 0:
        return False
        
    temp = n
    while temp > 0:
        digit = temp % 10       
        sum_of_facts += fact[digit] 
        temp //= 10               
        
    return sum_of_facts == original_n
