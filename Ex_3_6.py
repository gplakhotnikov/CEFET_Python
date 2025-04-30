def create_matrix(m, n):
  matrix = []
  for i in range(m):
    row = []
    for j in range(n):
      value = i * j
      row.append(value)
    matrix.append(row)
  return matrix

resultado = create_matrix(4, 3)
print(resultado)