from collections import Counter

def find_first_unique(s):
    counts = Counter(s)
    for char in s:
        if counts[char] == 1:
            return char
    return None
