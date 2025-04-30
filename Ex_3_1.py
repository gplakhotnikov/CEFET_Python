def find_numbers(inicio, fim):
  numeros_encontrados = []
  for numero in range(inicio, fim + 1):
    if numero % 7 == 0 and numero % 5 != 0:
      numeros_encontrados.append(str(numero))
  return ", ".join(numeros_encontrados)

resultado = find_numbers(100, 200)
print(resultado)