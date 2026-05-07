arr = [10, 20, 30, 20, 40, 20]
target = 20
positions = [i for i, x in enumerate(arr) if x == target]
print(f"Element found at indices: {positions}")

