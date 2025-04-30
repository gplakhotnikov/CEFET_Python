def sum_of_series(a):
  str_a = str(a)
  term1 = int(str_a)
  term2 = int(str_a*2)
  term3 = int(str_a*3)
  term4 = int(str_a*4)
  total_sum = term1 + term2 + term3 + term4
  return total_sum

entrada = 7
resultado = sum_of_series(entrada)
print(resultado)