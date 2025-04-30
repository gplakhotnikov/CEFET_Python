def count_case(input_string):
  upper_count = 0
  lower_count = 0
  for char in input_string:
    if char.isupper():
      upper_count += 1
    elif char.islower():
      lower_count += 1
  return {'UPPER CASE': upper_count, 'lower case': lower_count}

entrada = 'Hello World!'
resultado = count_case(entrada)
print(resultado)