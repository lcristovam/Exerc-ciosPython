""""
def soma(x,y):
    somatoria = x + y
    print(" A soma de ", x, "+", y, " É igual a ", somatoria)

n1 = float(input(" Digite um número para soma "))
n2 = float(input("Digite o próximo numero "))

print(soma(n1,n2)"""


def soma(x,y):
    somatoria = x + y
    print(" A soma de {} + {} é igual a {}".format(x, y, somatoria))

n1 = float(input(" Digite um número para soma "))
n2 = float(input("Digite o próximo numero "))

soma(n1,n2)

