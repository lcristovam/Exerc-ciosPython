soma = 0
cont = 0
for c in range(1,11):
    num = int(input(" Digite o {} valor ".format(c)))
    if c % 2 ==0:
        soma = soma + num
        cont = cont +1
print("Você informou {} números pares e a soma foi de: {}".format(cont,soma))


