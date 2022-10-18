import random

def jogar():

    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1,101) 
    total_de_tentativas = 0
    rodada = 1

    print("Qual o nível de dificuldade")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Define o nível: "))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5   

    for rodada in range (1, total_de_tentativas +1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute_str = input("Digite o seu número: ")
        print("Você digitou " , chute_str)
        chute = int(chute_str)

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100")
            continue

        if acertou:
            print("Parabéns! Você acertou!")
            break
        else:
            if maior:
                print("O seu chute foi maior do que o número secreto!")
            elif menor:
                print("O seu chute foi menor do que o número secreto!")

        rodada = rodada + 1


    print("Fim do jogo")
    print("O número secreto era", numero_secreto)

if (__name__ == "__main__"):
    jogar()

