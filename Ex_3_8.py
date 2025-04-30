def capitalize_lines(input_list):
  capitalized_list = [line.upper() for line in input_list]
  return capitalized_list

entrada = ['Sundays are Fun', 'Monday is Done']
resultado = capitalize_lines(entrada)
print(resultado)