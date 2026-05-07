A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

result = [[sum(pair) for pair in zip(rowA, rowB)] for rowA, rowB in zip(A, B)]
