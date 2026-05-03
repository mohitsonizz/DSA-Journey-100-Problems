def is_palindrome(n):
    # Basic Checks
    if n < 0 or (n % 10 == 0 and n != 0):
        return False

    rev = 0
    while n > rev:
        last_digit = n % 10
        rev = (rev * 10) + last_digit
        n = n // 10  # Number ko chhota karte jao

    return n == rev or n == rev // 10 
