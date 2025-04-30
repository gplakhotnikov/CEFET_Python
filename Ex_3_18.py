def f(n):
  if n == 0:
    return 1
  else:
    return f(n - 1) + 100 * n

resultado = f(0)
print(resultado)