def comparation (x,y):
    if x > y:
        print(" O número {} é maior que {}".format(x,y))
    elif x < y:
        print(" O número {} é maior que  {}".format(y,x))
    else:
        print(" {} e {} são iguais".format(x,y))
num = float(input(" Digite o primeiro número: "))
num2 = float(input(" Digite o segundo número: "))
comparation(num,num2)