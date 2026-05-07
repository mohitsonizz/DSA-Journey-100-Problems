def matrix_multiplication(a,b):
  result = [[sum(a*b for a, b in zip(row_a, col_b)) for col_b in zip(*B)] for row_a in A]
  return result 


