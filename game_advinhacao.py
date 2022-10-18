import random

def play():

    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    secret_number = random.randrange(1,101) 
    total_attempt = 0
    round = 1

    print("Qual o nível de dificuldade")
    print("(1) Fácil (2) Médio (3) Difícil")

    level = int(input("Define o nível: "))

    if(level == 1):
        total_attempt = 20
    elif(level == 2):
        total_attempt = 10
    else:
        total_attempt = 5   

    for round in range (1, total_attempt +1):
        print("Tentativa {} de {}".format(round, total_attempt))
        bet_str = input("Digite o seu número: ")
        print("Você digitou " , bet_str)
        bet = int(bet_str)

        right = bet == secret_number
        larger = bet > secret_number
        smaller = bet < secret_number

        if(bet < 1 or bet > 100):
            print("Você deve digitar um número entre 1 e 100")
            continue

        if right:
            print("Parabéns! Você acertou!")
            break
        else:
            if larger:
                print("O seu chute foi maior do que o número secreto!")
            elif smaller:
                print("O seu chute foi menor do que o número secreto!")

        round = round + 1


    print("Fim do jogo")
    print("O número secreto era", secret_number)

if (__name__ == "__main__"):
    play()

