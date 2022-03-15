def maiormenor(aa,bb,cc):
    menor = aa
    if bb < aa and bb < cc:
        menor = b
    if cc < aa and cc < bb:
        menor = c
    print("O menor número digitado foi o:  {}".format(menor))
    if bb > aa and bb > cc:
        maior = b
    if cc > aa and cc > bb:
        maior = c
    print("O Maior número digitado foi: {} ".format(maior))
a = int(input("Digite o primeiro valor"))
b = int(input("Digite o segundo valor"))
c = int(input(" Digite o terceiro valor"))
maiormenor(a,b,c)