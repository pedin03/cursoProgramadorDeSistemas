'''Faça um programa que armazena valores em duas variáveis, e faça a troca desses valores.
ex:
a=10
b=20
"a="20
"b="10'''

a=int(input("Atribua um valor à a: "))
b=int(input("Atribua um valor à b: "))
aux=a

a=b
b=aux
print("a=",a)
print("b=",b)
