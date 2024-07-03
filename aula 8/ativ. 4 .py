tabuada=int(input("Escolha o número de tabuada que você deseja entre 1 e 10: "))
while tabuada<1 or tabuada >10:
    tabuada=int(input("Insira um número entre 1 e 10: "))
print("Número validado.")

for i in range(11):
    print(tabuada,"x",i,"=",tabuada,"=",tabuada*i)
