n = int(input())
arr = list(map(int, input().split()))

unique_arr = list(dict.fromkeys(arr))

print(*(unique_arr))
