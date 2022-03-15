import random

n1 = str(input(" Digite um nome: "))
n2 = str(input(" Digite um nome: "))
n3 = str(input(" Digite um nome: "))
n4 = str(input(" Digite um nome\n\n"))

lista_nomes = [n1,n2,n3,n4]

escolhido = random.choice(lista_nomes)

print(" O aluno escolhido foi o:  {}", escolhido)