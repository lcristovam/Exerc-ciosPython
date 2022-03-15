from math import trunc
def quebra_numero(x):
    print(" O valor digitado foi {} e sua parte inteira é {} ".format(x, trunc(x)))


numero = float(input(" Digite um número decimal  "))

quebra_numero(numero)