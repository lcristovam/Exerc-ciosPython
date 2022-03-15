import math
def raiz(x):
        if(x>0):
            _raiz = math.sqrt(x)
            print(" A raiz quadrada de {} é {}".format(x,math.sqrt(x)))
        else:
             print(" Erro, não existe raiz de números negativos")
def dobro(x):
    try:
        _dobro = x *2
        print("O dobro de {} é {}".format(x,_dobro))
    except:
        print("Valor inválido! ")
def triplo(x):
    try:
        _triplo = x *3
        print("O triplo de {} é {}".format(x,_triplo))
    except:
        print("Valor inválido! ")
n1 = int(input(" Digite um número para saber seu dobro, seu triplo e sua raiz quadrada: "))

dobro(n1)
triplo(n1)
raiz(n1)



