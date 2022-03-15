import random

def jogo(play,comp,item):
    if play <=2 and play >= 0:
        print(" Computador jogou {}".format(item[comp]))
        print(" Jogador jogou {} ".format(item[play]))
        if comp == 0:
            if play == 0:
                print("===EMPATE ===")
            elif play ==1:
                print("=== JOGADOR VENCEU!===")
            elif play ==2:
                print("=== COMPUTADOR VENCEU! ===")
            else:
                print("=== JOGADA INVALIDA===")
        elif comp == 1:
            if play == 1:
                print("===EMPATE ===")
            elif play ==2:
                print("=== JOGADOR VENCEU!===")
            elif play ==0:
                print("=== COMPUTADOR VENCEU! ===")
            else:
                print("=== JOGADA INVALIDA===")
        elif comp == 2:
            if play == 2:
                print("===EMPATE ===")
            elif play ==0:
                print("=== JOGADOR VENCEU!===")
            elif play ==1:
                print("=== COMPUTADOR VENCEU! ===")
            else:
                print("=== JOGADA INVALIDA===")
    else:
        print(" === JOGADA INVALIDA ===")

print(" Suas opções: ")
print(" [0] Pedra \n [1] Papel \n [2] Tesoura \n")
itens = ('Pedra','Papel','Tesoura')
player = int(input("Qual é a sua jogada? "))
computer = random.randint(0,2)
jogo(player,computer,itens)

