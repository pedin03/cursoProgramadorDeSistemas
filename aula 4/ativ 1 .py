'''Faça um programa que peça dois números e imprima o maior deles.'''

num1=int(input("Escolha um número: "))
num2=int(input("Escolha outro número: "))

if num1>num2:
    print(num1,"é o maior número.")
elif num1<num2:
    print(num2,"é o maior número.")
else:
    print("Os números são iguais!")