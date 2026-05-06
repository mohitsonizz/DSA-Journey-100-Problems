    def linear_search():
 
        n = int(input())
        arr = list(map(int, input().split()))
        target = int(input())

        found_index = -1
        
        for i in range(n):
            if arr[i] == target:
                found_index = i
                break 

        print(found_index)
