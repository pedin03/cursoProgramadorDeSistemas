num=int(input("Insira um número para fazer a fatoração: "))
fatorial=num

for i in range(num-1,1,-1):
    #print(i)
    fatorial=fatorial*i
print(fatorial)