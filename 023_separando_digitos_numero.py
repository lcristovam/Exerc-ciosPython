from math import trunc

def separa(x):
    print(" Analisando o número {}".format(x))

    t = x // 1%10
    print(" Unidade = {} ".format(t))
    u = x // 10%10
    print(" Dezena = {} ".format(u))
    y = x // 100%10
    print(" Centena = {} ".format(y))
    z = x // 1000%10
    print(" Milhar = {} ".format(z))


num = int(input(" Informe um número inteiro: "))

separa(num)
