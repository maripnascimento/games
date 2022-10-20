from os import access
import random

def play():
    print_first_message()
    secret_word = load_secret_word()
    correct_letters = start_correct_letters(secret_word)
    print(correct_letters)

    hang = False
    hit = False
    mistakes = 0

    while(not hang and not hit):

        bet = ask_bet()

        if(bet in secret_word):
            mark_correct_bet(bet, correct_letters, secret_word)
        else:
            mistakes += 1
            draw_hang(mistakes)

        hang = mistakes == 6
        hit = "_" not in correct_letters

        print(correct_letters)

    if(hit):
        print_message_winner()
    else:
        print_message_loser(secret_word)




def print_first_message():
    print("*********************************")
    print("**Bem vindo ao jogo de FORCA!**")
    print("*********************************")

def load_secret_word():
    file = open("palavras.txt", "r")
    words = []

    for line in file:
        line = line.strip()
        words.append(line)

    file.close()

    number = random.randrange(0, len(words))
    secret_word = words[number].upper()

    return secret_word

def start_correct_letters(word):
    return ["_" for letter in word]

def ask_bet():
    bet = input("Qual letra? ")
    bet = bet.strip().upper()

    return bet

def mark_correct_bet(bet, correct_letters, secret_word):
    index = 0
    for letter in secret_word:
        if (bet == letter):
            correct_letters[index] = letter
        index += 1

def print_message_winner():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def print_message_loser(secret_word): 
    print("Você foi enforcado!")
    print("A palavra era {}".format(secret_word))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")   

def draw_hang(mistakes):
    print("  _______     ")
    print(" |/      |    ")

    if(mistakes == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(mistakes == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(mistakes == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(mistakes == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(mistakes == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(mistakes == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (mistakes == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()           

if (__name__ == "__main__"):
    play()    

