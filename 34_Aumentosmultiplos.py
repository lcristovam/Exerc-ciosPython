
def aumento(x):
    if x <= 1250:
        novosalario = x + x * 0.15
        print(" Quem ganhava  R$ {} , vai passar a ganhar: R$ {}".format(x,novosalario))
    else:
        novosalario = x + x * 0.10
        print(" \033[1:32m Quem ganhava R$ {} vai passar a ganhar: R$ {} ".format(x,novosalario))

salario = float(input("Qual o valor do salário atual? "))


aumento(salario)