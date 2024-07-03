vetor=[]
compactado=[]

for i in range(10):
    valor=int(input("Digite 10 números para o vetor: "))
    vetor.append(valor)

for valor in vetor:
    if valor != 0:
        compactado.append(valor)
print("Compactado(sem 0) fica assim:")
for valor in compactado:
    print(valor, end=" ")