def binary_divisible_by_5(binary_sequence):
  binary_numbers = binary_sequence.split(',')
  divisible_by_5 = []
  for binary_num in binary_numbers:
    decimal_num = int(binary_num, 2)
    if decimal_num % 5 == 0:
      divisible_by_5.append(binary_num.strip())
  return ','.join(divisible_by_5)

entrada = '1101,1010,1111,1001'
resultado = binary_divisible_by_5(entrada)
print(resultado)