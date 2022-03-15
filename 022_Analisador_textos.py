def analise(x):
    print(" Seu nome em maíusculas é {}" .format(x.upper()).strip())
    print(" Seu nome em minusculas é {}".format(x.lower()))
    print(" Seu nome tem ao todo {} letras".format(len(x)-x.count(" ")))
    #print(" Seu primeiro nome tem {} letras".format(x.find(" ")) )
    y = x.split()
    print(" Seu primeiro nome é {} e ele tem {} letras".format(y[0],len(y[0])))

nome = str(input("Digite seu nome completo: "))
analise(nome)