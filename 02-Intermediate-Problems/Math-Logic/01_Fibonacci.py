n = int(input())
if n <= 0:
    pass 
elif n == 1:
    print(0)
else:
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        temp = a + b
        a = b
        b = temp
