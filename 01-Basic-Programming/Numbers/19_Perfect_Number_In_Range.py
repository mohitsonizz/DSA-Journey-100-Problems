import math

def is_perfect(num):
    if num < 2:
        return False
    div_sum = 1
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            div_sum += i
           
            if i * i != num:
                div_sum += num // i         
    return div_sum == num

def find_perfect_in_range(start, end):
    result = []
    for i in range(start, end + 1):
        if is_perfect(i):
            result.append(i)
    return result

