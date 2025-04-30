def catch_zero_division():
  try:
    result = 10 / 0
    return result 
  except ZeroDivisionError:
    return "division by zero"

resultado = catch_zero_division()
print(resultado)