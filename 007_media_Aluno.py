
def  media(x,y):

        media = (x+y)/2
        if media <7.0:
            print(" Aluno está abaixo da média > {} > Em recuperação! ".format(media))
        elif media <4.0:
            print(" Aluno está abaixo de 4 pontos > {} > Reprovado! ".format(media))
        else:
            print(" Aluno está acima da média > {} > Aprovado !".format(media))

n1 = float(input(" Digite a primeira nota do aluno: "))
n2 = float(input(" Digite a segunda nota do aluno: "))

media(n1,n2)


