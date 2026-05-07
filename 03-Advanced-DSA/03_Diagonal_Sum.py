def both_diagonals_sum(n, matrix):
    primary = 0
    secondary = 0
    
    for i in range(n):
        primary += matrix[i][i]
        secondary += matrix[i][n - i - 1]
        
    return primary, secondary


