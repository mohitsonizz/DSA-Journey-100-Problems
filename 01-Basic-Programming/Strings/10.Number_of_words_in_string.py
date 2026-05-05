s = input().strip()

if not s:
    print(0)
else:
    words = s.split()
    print(len(words))
