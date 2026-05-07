def boundary_traversal(matrix):
    if not matrix:
        return []
    
    rows = len(matrix)
    cols = len(matrix[0])
    result = []
    if rows == 1:
        return matrix[0]
    if cols == 1:
        return [matrix[i][0] for i in range(rows)]
    for j in range(cols):
        result.append(matrix[0][j])
    for i in range(1, rows):
        result.append(matrix[i][cols - 1])
    for j in range(cols - 2, -1, -1):
        result.append(matrix[rows - 1][j])
    for i in range(rows - 2, 0, -1):
        result.append(matrix[i][0])

    return result

mat = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

print(*(boundary_traversal(mat)))

