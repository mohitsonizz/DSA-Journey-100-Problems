def move_zeros_fast(arr):
    non_zeros = [x for x in arr if x != 0]
    zeros_count = arr.count(0)
    return non_zeros + [0] * zeros_count


