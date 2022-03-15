def calc(__year, __actualyear):
    anocorte = 2002
    alistamento =  __actualyear - anocorte
    idade = __actualyear - __year
    if idade < 18 and alistamento > 0:
        print(" Quem nasceu em {} tem {} anos em {}".format(__year, idade, __actualyear))
        print(" Ainda faltam {} anos para seu alistamento".format(alistamento-idade))
    elif idade == 18:
        print(" Você precisa se alistar imediatamente!")
    else:
        print(" Quem nasceu em {} tem {} anos em {}".format(__year, idade, __actualyear))
        print(" Você já deveria ter se alistado há {} anos".format(idade-alistamento))
        print(" Seu alistamento foi em {}".format(__year+alistamento))
ano = int(input(" Ano de nascimento: "))
anoatual= 2020
calc(ano,anoatual)