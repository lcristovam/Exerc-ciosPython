def triangulo(x,y,z):
    if x < y + z and y < x + z and z < x + y:
        print(" Os seguimentos podem formar um triângulo", end=" ")
        if x == y == z:
            print("Equilátero")
        elif x != y != z != x:
            print("Escaleno")
        else:
            print("Isósceles")
    else:
        print(" Os seguimentos não podem formar um triângulo")
r1 = int(input(" Digite o primeiro segmento "))
r2 = int(input(" Digite o segundo segmento "))
r3 = int(input(" Digite o terceiro segmento "))

triangulo(r1,r2,r3)







