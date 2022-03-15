
#Faça o programa que leia algo na tela e diga que tipo primitivo ele é e outras informações possíveis sobre ela

a = (input(" Digite algo: "))

print(" O tipo primitivo desse valor é: ", type(a))
print(" É um numero ?" , a.isnumeric())
print("Só tem espaços? ", a.isspace())
print("É  alfabético? ", a.isalpha())
print("É  alfanumérico? ", a.isalnum())
print(" Só tem letras maíusculas? ", a.isupper())
print(" Só tem letras minúsculas?", a.islower())

