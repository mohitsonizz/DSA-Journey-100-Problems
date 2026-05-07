def rotate_array(arr, k):
    n = len(arr)
    k = k % n 
    arr = arr[-k:] + arr[:-k]
    return arr

