def even_digit_numbers(start, end):
  even_numbers = []
  for num in range(start, end + 1):
    s_num = str(num)
    is_even_digits = True
    for digit in s_num:
      if int(digit) % 2 != 0:
        is_even_digits = False
        break
    if is_even_digits:
      even_numbers.append(s_num)
  return ','.join(even_numbers)

resultado = even_digit_numbers(1200, 2100)
print(resultado)