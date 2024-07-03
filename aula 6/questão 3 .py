print("Escolha o tipo de conversão que deseja fazer.")
print("Digite 1 para converter de Celsius para Fahrenheit.")
print("Digite 2 para converter de Fahrenheit para Celsius.")
tipo=int(input(""))

temp=float(input("Digite a temperatura a ser convertida: "))

if tipo==1:
    print(temp,"°C é igual a",(temp*9/5)+32,"°F")
if tipo==2:
    print(temp,"°F é igual a",(temp-32)*5/9,"°C")