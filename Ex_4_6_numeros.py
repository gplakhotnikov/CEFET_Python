numero = int(input("Digite um número inteiro: "))
antecessor = numero-1
sucessor = numero+1
print(f"Número informado: {numero}")
print(f"Antecessor: {antecessor}")
print(f"Sucessor: {sucessor}")

numero_decimal = float(input("Digite um número: "))
print(f"Número com duas casas decimais: {numero_decimal:.2f}")

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))
media = (nota1 + nota2 + nota3 + nota4)/4
print(f"A média final é: {media:.2f}")

numero = int(input("Digite um número inteiro: "))
if numero % 2 == 0:
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é ímpar.")