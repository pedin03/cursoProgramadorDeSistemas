print("ALISTAMENTO DO EXÉRCITO.")
print()
print("Digite M caso seja do gênero masculino ou F para gênero feminino.")
sex=input("")

altura=float(input("Informe sua altura: "))


if altura>=1.70 and sex=="M":
    print("Apto para o alistamento.")
if altura<1.70 and sex=="M":
    print("Não está apto para o alistamento.")

if altura>=1.60 and sex=="F":
    print("Apta para o alistamento.")
if altura<1.60 and sex=="F":
    print("Não está apta para o alistamento.")