import math
def sen(ang):
    x = math.sin(math.radians(ang))
    print(" O Seno de {} é igual a: {:.2f}".format(ang, x))

def  cos(ang):
    x = math.cos(math.radians(ang))
    print(" O Cosseno de {} é igual a: {:.2f}".format(ang, x))

def tan(ang):
    x = math.tan(math.radians(ang))
    print(" A tangente de {} é igual a {:.2f}".format(ang, x))


print("--------- Calculando o Seno, Cosseno e Tangente de um número -------------")

ângulo = float(input("Digite um ângulo \n"))


sen(ângulo)
cos(ângulo)
tan(ângulo)

