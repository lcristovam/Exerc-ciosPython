from time import sleep
from random import randint
def jogo(__number):
   if __number <=5 and __number >=0:
            computer = randint(0, 5)
            if computer == __number:
                print("Parabéns! Você conseguiu me vencer!")
            else:
                print(" GANHEI! Eu pensei no número {} e não no {}".format(computer,__number))
   else:
        print("Número inválido.")

print("-=-" *20)
print("\033[1:34mVou pensar em um número entre 0 e 5. Tente adivinhar...)\033[m")
print("-=-" * 20)
numero = int(input("Em que número eu pensei ? "))
print("\033[1:32mPROCESSANDO....\033[m")
sleep(3)

jogo(numero)

