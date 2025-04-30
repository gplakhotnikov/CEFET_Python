temperaturas_celsius = [22.5, 40, 13, 29, 34]
converter_para_fahrenheit = lambda c: (c * 9/5) + 32
temperaturas_fahrenheit = list(map(converter_para_fahrenheit, temperaturas_celsius))
print(f"Temperaturas em Celsius: {temperaturas_celsius}")
print(f"Temperaturas em Fahrenheit: {temperaturas_fahrenheit}")

sequencia = [21, 5, 34, 8, 16, 7, 3]
pares = [num for num in sequencia if num % 2 == 0]
impares = [num for num in sequencia if num % 2 != 0]
soma_pares = sum(pares)
soma_impares = sum(impares)
print(f"Sequência: {sequencia}")
print(f"Números pares: {pares}")
print(f"Soma dos pares: {soma_pares}")
print(f"Números ímpares: {impares}")
print(f"Soma dos ímpares: {soma_impares}")