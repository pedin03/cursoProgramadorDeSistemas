def lermatriz():
    matriz=[]
    for i in range(4):
        linha=[]
        for j in range(4):
            elemento=int(input("Digite o elemento da posição [{}][{}]: ".format(i,j)))
            linha.append(elemento)
        matriz.append(linha)
    return matriz
def maiorvalor(matriz1,matriz2):
    matrizmaior=[]
    for i in range(4):
        linhamaior=[]
        for j in range(4):
            linhamaior.append(max(matriz1[i][j], matriz2[i][j]))
        matrizmaior.append(linhamaior)
    return matrizmaior
print("Digite abaixo os elementos da primeira matriz.")
matriz1=lermatriz()
print()
print("Digite abaixo os elementos da segunda matriz.")
matriz2=lermatriz()
print()
matrizmaior=maiorvalor(matriz1,matriz2)

print("A matriz com os maiores valores de cada posição é:")
for linha in matrizmaior:
    print(linha)