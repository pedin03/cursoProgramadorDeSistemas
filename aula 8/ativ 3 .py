nome=input("Insira seu nome: ")
while len(nome)<2:
    nome=input("Nome inválido, insira outro nome:")
print("Bem-vindo,",nome)
print()


idade=int(input("Insira sua idade: "))
while idade<0 or idade>120:
    idade=int(input("insira uma idade válida: "))
print("Você tem",idade,"anos de idade.")
print()

salário=float(input("Insira seu salário: "))
while salário<=0:
    salário=float(input("insira um número válido: "))
print("Seu salário é de",salário,"R$.")
print()

print("Insira M para masculino ou F para feminino.")
sex=input("")
while sex!="M" and sex!="F":
    sex=input("Insira um caractere válido: ")
print("Seu gênero é",sex)
print()

print("Estado civil:")
print("Digite S para solteiro(a).")
print("Digite C para casado(a).")
print("Digite V para viúvo(a).")
print("Digite D para divorciado(a).")
ec=input("")

while ec!="S" and ec!="C" and ec!="V" and ec!="D":
    ec=input("Insira um caractere válido para seu estado civil: ")
print("Seu estado civil é",ec)

