from datetime import date
def categorias(_nasc,_anoatual,__idade):
    if idade <= 9:
        print(" O Atleta tem  {} anos".format(idade))
        print(" Sua categoria é MIRIM")
    elif idade > 9 and idade<=14:
        print(" O Atleta tem  {} anos".format(idade))
        print("Sua categoria é INFANTIL")
    elif idade > 14 and idade <=19:
        print(" O Atleta tem  {} anos".format(idade))
        print("Sua categoria é JUNIOR")
    elif idade > 19 and idade <=25:
        print(" O Atleta tem  {} anos".format(idade))
        print("Sua categoria é SÊNIOR")
    elif idade >25:
        print(" O Atleta tem  {} anos".format(idade))
        print(" Sua categoria é MASTER")
    else:
        print(" Idade inválida")
nasc = int(input(" Digite o ano de nascimento: "))
anoatual = date.today().year
idade = 2020 - nasc
categorias(nasc,anoatual,idade)

