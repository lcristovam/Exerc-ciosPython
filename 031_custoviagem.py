
def custoviagem(__number):
    if __number < 200 and __number >0:
        print("\033[1:34m O Custo da sua passagem será de: R$ {:.2f} \033[m".format(__number*0.5))

    elif __number >= 200:
        print("\033[1:34m O Custo da sua passagem será de: R$ {:.2f} \033[m ".format(__number*0.45))
    else:
        print("\033[1:31mNúmero inválido\033[m")

distancia = float(input("\033[1:31mQual é a distância de sua viagem:?\033[m  "))

custoviagem(distancia)

