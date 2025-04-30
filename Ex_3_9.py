def unique_sorted_words(input_string):
  words = input_string.lower().split()
  unique_words = sorted(list(set(words)))
  return ' '.join(unique_words)

entrada = 'dog cat apple cat banana dog'
resultado = unique_sorted_words(entrada)
print(resultado)