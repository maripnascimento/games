import game_advinhacao
import game_forca

def escolhe_jogo():
    print("*********************************")
    print("ESCOLHA O SEU JOGO!")
    print("*********************************")

    print("(1) Forca (2) Advinhação")

    jogo = int(input("Qual jogo? "))

    if(jogo ==1):
        print("Jogando FORCA")
        game_forca.jogar()

    elif(jogo ==2):
        print("Jogando ADVINHAÇÃO")  
        game_advinhacao.jogar()

if (__name__ == "__main__"):
    escolhe_jogo()        


