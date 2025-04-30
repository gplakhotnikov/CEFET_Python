def sort_words(input_string):
  words = input_string.split(',')
  sorted_words = sorted(words)
  return ','.join(sorted_words)

entrada = 'banana,apple,grape,orange'
resultado = sort_words(entrada)
print(resultado)