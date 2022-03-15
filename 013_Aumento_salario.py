
def aumento(x):
    a = x *1.15
    print("O colaborador que recebia o valor de R$ {} , vai passar a receber R$ {:.2f} ".format(x,a))

print(" -------- Programa para calcular 15 % de aumento no salário---------")
salarioatual = float(input(" Digite o salário do colaborador  "))

aumento(salarioatual)