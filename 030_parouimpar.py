
def parouimpar(__number):
    if  (__number%2 == 1):
        print("\n O número {} é ímpar " .format(__number))
    else:
        print("\n O número {} é par " .format(__number))
        exit()

numero = int(input("Digite um número: \n"))

parouimpar(numero)
