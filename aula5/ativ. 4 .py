
num1=int(input("Insira um número: "))
num2=int(input("Insira outro número: "))
num3=int(input("Insira mais um número: "))

if num1>num2:
    temp=num1
    num1=num2
    num2=temp
if num2>num3:
    temp=num2
    num2=num3
    num3=temp
if num1>num2:
    temp=num1
    num1=num2
    num2=temp
print("Em ordem crescente os números ficam assim:",num1,num2,num3)