
def tabuada(x):
    i =2
    while i <= 100:
        resultado = x * i
        print(" {} x {} = {}".format(x,i,resultado))
        i = i +1

n1 = int(input("Digite um número para saber sua tabuada  "))

tabuada(n1)


