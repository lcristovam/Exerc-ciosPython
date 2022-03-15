def conversao(__option,__number):
    if __option == 1:
        print("{} convertido em binário é igual a: {}".format(__number, bin(__number)[2:]))
    elif __option ==2:
        print(" {} convertido em ocal é igual a: {} ".format(__number, oct(__number)[2:]))
    elif __option ==3:
        print("{} convertido em Hexadecimal é igual a: {}".format(__number, hex(__number)[:2]))
    else:
        print(" \033[1:31mValor inválido\033[m")

num = int(input("Digite um número inteiro: "))
print(''' Escolha uma das bases para conversão:
[ 1 ] Converter para BINARIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL''')
base = int(input(" \033[1:36mSua opção:   \033[m"))
conversao(base, num)


import random
from time import sleep

def sorteio(comp,n1,n2,n3,n4,n5,n6):
  try:
    if n1 == comp or n2 == comp or n3 == comp or n4 == comp or n5 == comp or n6 == comp:
      print("Parabéns! Bom trabalho! Você ganhou! Praticamente parente da mãe Diná! O número que pensei foi: {}".format(comp))
    else:
      print("Que pena… Você errou… O número era {} ".format(comp))
  except:
    print("ERRO!")


computador = random.randint(1,20)
print("Olá Amigo(a)! Vou pensar em um número de 1 a 20  e você terá 6 chances para adivinhar")
sleep(3.5)
print("Vamos lá, vou escolher um agora!")
sleep(2)
print("\033[1:32m PROCESSANDO\033[m")
sleep(1)
print("..")
sleep(1)
print("..")
sleep(1)
print("..")
sleep(1)
print("PRONTO, escolhi um!")
numero1 = int(input(" Digite o 1º número: "))
numero2 = int(input(" Digite o 2º número: "))
numero3 = int(input(" Digite o 3º número: "))
numero4 = int(input(" Digite o 4º número: "))
numero5 = int(input(" Digite o 5º número: "))









sorteio(computador,numero1,numero2,numero3,numero4,numero5,numero6)