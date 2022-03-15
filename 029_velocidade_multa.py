
def mult(__vel):
    if __vel > 80:
        print("\033[1;31mMULTADO! Está acima da velocidade permitida de 80 KM/H")
        print(" Você deverá pagar a multa no valor de R$ {} ".format((__vel-80)*7))
    else:
        print("\033[1;32m Tenha uma boa viagem. Dirija com segurança!")
velocidade = int(input("Qual a velocidade do carro??  "))


mult(velocidade)