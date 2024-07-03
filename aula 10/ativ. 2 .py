contador=0
linha=0
coluna=0
matriz=[[0,0,0],
        [0,0,0],
        [0,0,0],
       ]
for i in range(len(matriz)):
    for j in range(len(matriz)):
     matriz[i][j]= int(input("Insira os números da matriz: "))
     if matriz[i][j]>10:
        contador+=1
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        print(matriz[i][j])
print("Há",contador,"números maiores que 10 nessa matriz.")


