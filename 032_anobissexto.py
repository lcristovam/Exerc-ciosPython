
def bissexto(__ano):
    if __ano % 4 ==0 and __ano %100 !=0 or __ano %400==0:
        print("\033[1:34m O ano {} é BISSEXTO \033[m".format(__ano))
    else:
        print("\033[1:34m O ano {} NÃO É BISSEXTO\033[m".format(__ano))


ano = int(input("\033[1:32m Digite um anos para saber se ele é bissexto: \n"))

bissexto(ano)