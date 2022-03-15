def contadorletras(__cont):
    print(" A letra A aparece {} vezes na frase. ".format(__cont.count("A")))
    print(" A primeira letra A apareceu na posição {}".format(__cont.find("A")+1))
    print(" A ultima letra A apareceu na posição {}".format(__cont.rfind("A")+1))


phrase = str(input("Digite uma Frase:  ")).upper().strip()

contadorletras(phrase)