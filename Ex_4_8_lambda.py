nome_completo = input("Digite seu nome completo: ")
nomes = nome_completo.split()
primeiro_nome = nomes[0]
ultimo_nome = nomes[-1]
print(f"Primeiro nome: {primeiro_nome}")
print(f"Último nome: {ultimo_nome}")

numero = int(input("Digite um número inteiro: "))
verificar = lambda n: "par" if n % 2 == 0 else "ímpar"
resultado = verificar(numero)
print(f"O número {numero} é {resultado}")

def calculadora():
    operacao = input("Digite a operação (+, -, *, /): ")
    num1 = float(input("Digite o primeiro valor: "))
    num2 = float(input("Digite o segundo valor: "))

    if operacao == '+':
        resultado = num1 + num2
    elif operacao == '-':
        resultado = num1 - num2
    elif operacao == '*':
        resultado = num1 * num2
    elif operacao == '/':
        if num2 != 0:
            resultado = num1 / num2
        else:
            resultado = "Erro: Divisão por zero!"
    else:
        resultado = "Operação inválida!"

    print(f"O resultado da operação é: {resultado}")

calculadora()