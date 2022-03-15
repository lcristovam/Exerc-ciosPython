
def dolar(x):
    money = x/3.27
    print(" Com R$ {} você pode comprar {:.2f} U$".format(x,money))

reais = float(input("Quantos reais você tem em sua carteira: "))
print("\n (Supondo que o dólar esteja cotado a R$3,27)")
dolar(reais)
