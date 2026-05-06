n = int(input())
arr = list(map(int, input().split()))

unique_list = sorted(list(set(arr)))
print(unique_list[-2])
