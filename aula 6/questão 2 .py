print("Insira 3 números a seguir.")
num1=int(input("número 1: "))
num2=int(input("número 2: "))
num3=int(input("número 3: "))

if num1>num2 and num1>num3:
    print(num1,"É o maior número")
if num2>num1 and num2>num3:
    print(num2,"É o maior número")
if num3>num2 and num3>num1:
    print(num3,"É o maior número")
if num1<num2 and num1<num3:
    print(num1,"É o menor número")
if num2<num1 and num2<num3:
    print(num2,"É o menor número")
if num3<num2 and num3<num1:
    print(num3,"É o menor número")