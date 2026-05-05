s = input().strip()
clean_s = "".join(char for char in s if char.isalnum())
print(clean_s)
