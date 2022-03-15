
def cm(x):
    d = x *100
    print(" {} metros é equivalente a {:.0f} centímetros".format(x,d))

def mm(x):
    d = x *1000
    print(" {} metros é equivalente a {:.0f} milímetros".format(x,d))

medida = float(input("Digite um valor em metros: "))

cm(medida)
mm(medida)

