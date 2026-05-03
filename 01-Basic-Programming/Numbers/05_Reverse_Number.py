def reverse_number(n):
    is_negative = n < 0
    num = abs(n)
    
    reversed_num = 0
    while num > 0:
        
        last_digit = num % 10
        reversed_num = (reversed_num * 10) + last_digit
        num //= 10
        
    return -reversed_num if is_negative else reversed_num

''' 500 --> 005  
def reverse_string_way(n):
    s = str(n)
    if s[0] == '-':
        return int('-' + s[1:][::-1])
    return int(s[::-1
'''    
    
