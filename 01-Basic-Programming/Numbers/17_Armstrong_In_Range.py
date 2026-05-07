def find_armstrong_in_range(start, end):
    armstrong_list = []
    for num in range(start, end + 1):
        if 0 <= num <= 9:
            armstrong_list.append(num)
            continue
            
        temp = num
        n = len(str(num)) 
        total = 0
        while temp > 0:
            digit = temp % 10
            total += digit ** n
            temp //= 10

            if total > num:
                break
        
        if total == num:
            armstrong_list.append(num)
            
    return armstrong_list



print(f"{s} se {e} ke beech Armstrong numbers hain:")
print(*(result))
