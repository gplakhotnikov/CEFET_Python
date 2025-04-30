from functools import reduce

sequencia = [54, 10, 29, 87, 7, 64]
maior = reduce(lambda a, b: a if a > b else b, sequencia)
menor = reduce(lambda a, b: a if a < b else b, sequencia)
print(f"Sequência: {sequencia}")
print(f"Maior valor: {maior}")
print(f"Menor valor: {menor}")