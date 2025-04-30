def count_letters_digits(input_string):
  letter_count = 0
  digit_count = 0
  for char in input_string:
    if char.isalpha():
      letter_count += 1
    elif char.isdigit():
      digit_count += 1
  return {'LETTERS': letter_count, 'DIGITS': digit_count}

entrada = 'Data123 Science 2024'
resultado = count_letters_digits(entrada)
print(resultado)