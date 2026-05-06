def digit_frequency(n)
    n_str = str(abs(n))
    freq = {}
    
    for digit in n_str:
        freq[digit] = freq.get(digit, 0) + 1
        
    return freq
