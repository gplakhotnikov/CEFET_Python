def verificar_par_impar(numero):
  if numero % 2 == 0:
    return "par"
  else:
    return "ímpar"

numero_teste = 15
resultado = verificar_par_impar(numero_teste)
print(f"O número {numero_teste} é {resultado}")