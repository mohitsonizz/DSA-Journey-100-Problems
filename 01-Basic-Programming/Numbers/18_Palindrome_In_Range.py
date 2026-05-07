def find_palindromes_fast(start, end):
    palindromes = []
    for num in range(start, end + 1):
        if str(num) == str(num)[::-1]:
            palindromes.append(num)
    return palindromes

