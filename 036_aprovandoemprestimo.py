from time import sleep
def calculoemprestimo(__house, __handmoney, __time, __times):
    minimum = __house / __times
    if minimum >  (__handmoney *0.3):
        print("\033[1:36mPROCESSANDO....\033[m")
        sleep(3)
        print(" Para pagar a casa de R$ {} em  {} anos, a prestação será de R$ {:.2f}".format(__house,__time,minimum))
        print(" Pelo fato das parcelas serem maiores que 30 % do seu salário, o empréstimo foi \033[1:31mNegado!\033[m")
    else:
        print("\033[1:36mPROCESSANDO.....\033[m")
        sleep(3)
        print(" Para pagar a casa de R$ {} em {} anos, a prestação será de R$ {:.2f}".format(__house,__time,minimum))
        print(" \033[1:32m Empréstimo aprovado!\033[m")

valorcasa = float(input("Qual o valor da casa ?  "))
salario = float(input(" Qual o valor do seu salário?  "))
tempo = int(input("Em quantos anos você pretende pagar  ?"))
prestacao = tempo *12
calculoemprestimo(valorcasa,salario,tempo,prestacao)