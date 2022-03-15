
def analisenome(__name):
    print(" Seu primeiro nome é {} ".format(__name[0]))
    print(" Seu ultimo nome é {} ".format(__name[len(__name)-1]))


nome = str(input("Digite seu nome: ")).strip()

n = nome.split()

analisenome(n)




