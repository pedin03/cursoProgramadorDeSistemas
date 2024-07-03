num1=int(input("Informe o 1° número: "))
num2=int(input("Informe o 2° número: "))

print("Qual operação aritmética você deseja realizar?")
print("1. +")
print("2. -")
print("3. *")
print("4. /")
operação=int(input(""))

match operação:
    case 1:
        print("O resultado é",num1+num2)
    case 2:
        print("O resultado é",num1-num2)
    case 3:
        print("O resultado é",num1*num2)
    case 4:
        print("O resultado é",num1/num2)