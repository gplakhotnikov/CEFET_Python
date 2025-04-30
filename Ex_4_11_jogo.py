import random

def jogo_adivinhacao():
    numero_secreto = random.randint(0, 10)
    tentativas_restantes = 5
    pontuacao = 0

    print("Tente adivinhar o número secreto entre 0 e 10")

    while tentativas_restantes > 0:
        try:
            palpite = int(input(f"Tentativa {6 - tentativas_restantes}: Digite seu palpite: "))

            if not 0 <= palpite <= 10:
                print("Erro: Por favor, digite um número entre 0 e 10.")
                continue

            tentativas_restantes -= 1

            if palpite == numero_secreto:
                if tentativas_restantes == 4:
                    pontuacao = 100
                elif tentativas_restantes == 0:
                    pontuacao = 10
                else:
                    pontuacao = 10 + tentativas_restantes * 20
                print(f"Parabéns! Você adivinhou o número secreto ({numero_secreto})!")
                print(f"Sua pontuação: {pontuacao}")
                break
            elif palpite < numero_secreto:
                print("O número secreto é maior.")
            else:
                print("O número secreto é menor.")

            if tentativas_restantes > 0:
                print(f"Você tem {tentativas_restantes} tentativas restantes.")
            else:
                print(f"Você não conseguiu adivinhar o número. O número secreto era {numero_secreto}.")

        except ValueError:
            print("Erro: Por favor, digite um número inteiro.")

jogo_adivinhacao()