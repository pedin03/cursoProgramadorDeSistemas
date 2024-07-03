vetor1=[]
vetor2=[]
print("Digite os 5 elementos do primeiro vetor:")
for i in range(5):
    elemento=int(input())
    vetor1.append(elemento)
print("Digite os 5 elementos do segundo vetor:")
for i in range(5):
    elemento=int(input())
    vetor2.append(elemento)
interseçao=[]
for elemento in vetor1:
    if elemento in vetor2 and elemento not in interseçao:
        interseçao.append(elemento)

print("A interseção entre os dois vetores é:",interseçao)