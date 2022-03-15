
def area(x,y):
    a = x * y
    print ( " Seu cômodo possui {:.2f} M²".format(a))
def qnttinta(x,y):
    a = (x*y)/2
    print(" Para pintá-lo, irá precisar de {} L de tinta".format(a))

ladoa = float(input("Qual a distância tem o primeiro lado de seu cômodo? "))
ladob = float(input("Qual a distância em metros do segundo lado de seu cômodo? "))

area(ladoa,ladob)
qnttinta(ladoa,ladob)
