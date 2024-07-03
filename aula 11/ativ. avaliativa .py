valores=[]
for i in range(5):
    valor=int(input("Digite 5 valores: "))
    valores.append(valor)

maior_numero=valores[0]
menor_numero=valores[0]

maiorposiçao=0
menorposiçao=0

for i in range(1,5):
    if valores[i]>maior_numero:
        maior_numero=valores[i]
        maiorposiçao=i
    if valores[i]<menor_numero:
        menor_numero=valores[i]
        menorposiçao=i

print("O maior valor é",maior_numero,"e está na posição",maiorposiçao)
print()
print("O menor valor é",menor_numero,"e está na posição",menorposiçao)