num1=int(input("Insira o 1° número: "))
num2=int(input("Insira o 2° número: "))
num3=int(input("Insira o 3° número: "))

if num1>num2 and num1>num3:
    print(num1,"é o maior.")
if num2>num1 and num2>num3:
    print(num2,"é o maior.")
if num3>num1 and num3>num2:
    print(num3,"é o maior.")