import math
def triang(x,y):
    hip = math.sqrt(x**2 + y**2)
    print(" O valor da hipotenusa é {}".format(hip))
catop = float(input("Digite o valor do cateto oposto: "))
catad = float(input("Digite o valor do cateto adjacente: "))
triang(catop,catad)


