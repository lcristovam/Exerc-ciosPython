def tabuada(x):
    for i  in range(1,11):
        result = x * i
        print(" {} X {} = {}".format(x,i,result))
num = int(input("Digite um número para ver sua tabuada"))
tabuada(num)

