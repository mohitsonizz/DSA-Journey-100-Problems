n = int(input())
arr = list(map(int, input().split()))

def count_frequency(arr):
    freq = {}
    for item in arr:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    
    return freq

print(count_frequency(arr))
