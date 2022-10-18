import game_advinhacao
import game_forca

def choose_game():
    print("*********************************")
    print("ESCOLHA O SEU JOGO!")
    print("*********************************")

    print("(1) Forca (2) Advinhação")

    jogo = int(input("Qual jogo? "))

    if(jogo ==1):
        print("Jogando FORCA")
        game_forca.play()

    elif(jogo ==2):
        print("Jogando ADVINHAÇÃO")  
        game_advinhacao.play()

if (__name__ == "__main__"):
    choose_game()        


