def desconto_5(x):
    desc = x *0.95
    print(" Com desconto de 5% sobre R$ {} , o preço do produto será = R$ {:.1f} ".format(x, desc))

preco = float(input(" Quanto custa o produto? "))

desconto_5(preco)

