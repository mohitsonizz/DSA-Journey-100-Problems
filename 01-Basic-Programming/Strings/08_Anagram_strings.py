from collections import Counter

def is_anagram_optimized(s1, s2):
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()
    
    if len(s1) != len(s2):
        return False
        
    return Counter(s1) == Counter(s2)
