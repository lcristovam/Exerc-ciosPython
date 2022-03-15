import random

n1 = str(input("Digite o primeiro nome: "))
n2 = str(input("Digite o segundo nome: "))
n3 = str(input("Digite o teceiro nome: "))
n4 = str(input("Digite o quarto nome: "))

lista_alunos = [n1,n2,n3,n4]


random.shuffle(lista_alunos)

print("A ordem de apresentação será: ")
print(lista_alunos)