def find_missing_number():
    n = int(input())
    arr = list(map(int, input().split()))
    
    expected_sum = n * (n + 1) // 2
    
    actual_sum = sum(arr)
    
    missing = expected_sum - actual_sum
    print(missing)
