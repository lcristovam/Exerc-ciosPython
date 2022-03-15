# Regra de negócio:
# A vista no dinheiro 20 % de desconto
# A vista no cartão 15 % de desconto
# 2x no cartão 5 % de Juros sobre o valor total
# 3x ou mais no cartão 15 % de juros sobre o valor total
def calculocompra(price,form,times):
    if form == 1:
        price = price *0.8
        print(" \033[1:32mPagando á vista no dinheiro ou cheque, você obterá 20 % de desconto. O valor da sua compra será de R$: {} \033[m".format(price))
    elif form ==2:
        price = price * 0.85
        print("\033[1:32m Pagando á vista no cartão, você obterá 15 % de desconto. O valor da sua compra será de R$: {} \033[m".format(price))
    elif form ==3:
        price = price * 1.05
        valuetimes =  price / times
        print("\033[1:32m Pagando em {} x no cartão, o compra terá 5% de juros sob o valor total ficando  {} parcelas de R$ {} , somando o valor total da compra de R$: {} \033[m".format(times,times,valuetimes,price))
    elif form ==4:
        price = price * 1.15
        valuetimes = price / times
        print(" \033[1:32mPagando em {} x no cartão, o compra terá 15% de juros sob o valor total ficando  {} parcelas de R$ {} , somando o valor total da compra de R$: {} \033[m".format(times,times,valuetimes,price))
    else:
        print("\033[1:31m Opção inválida !\033[m")
print("================ Lojas Cristovam =================")
preco = float(input(" Qual o valor da compra?  "))
print(''' \033[1:32mFORMAS DE PAGAMENTO\033[m \n 
\033[1:32m[ 1 ] - À vista no dinheiro/cheque\033[m \n
\033[1:31m[ 2 ] - À vista no cartão\033[m \n
\033[1:34m[ 3 ] - 2x no cartão\033[m \n
\033[1:36m[ 4 ] - 3x ou mais no cartão\033[m \n''')
formapgto = int(input(" Qual a forma de pagamento?  "))
parcelas = None
if   formapgto == 3:
        parcelas = 2
elif formapgto == 4:
        parcelas = int(input(" Quantas parcelas ?  "))

calculocompra(preco,formapgto,parcelas)


