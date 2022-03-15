def custo(k,dd):
        km = k *0.15
        d = dd *60
        s = km + d
        print(" O Valor total a ser pago é de R$ {:.2f} ".format(s))

print("-------------Custo de aluguel de automóveis-----------------\n")
print(" Custo por dia = R$ 60,00 \n Custo por Km rodado = R$ 0,15 \n\n")
days = float(input("Por quantos dias o carro foi alugado? "))
dist = float(input("Quantos Kilômetros você percorreu? " ))


custo(dist,days)

