def procuranome(x):
    print(" Seu nome tem Silva? {} ".format("SILVA" in x.upper()))


nome = str(input("Digite seu nome completo: ")).strip()

procuranome(nome)