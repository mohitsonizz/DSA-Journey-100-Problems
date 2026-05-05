def get_product_of_digits(n: int) -> int:
    n = abs(n)
    
    if n == 0:
        return 0
    
    product = 1
    
    while n > 0:
        digit = n % 10
        # Update product
        product *= digit
        if product == 0:
            return 0
        n //= 10
        
    return product
