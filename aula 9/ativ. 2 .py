num=[1,2,3,4,5]

num.reverse()
for i in num:
    print(i)

num=[0]*5
for i in range(len(num)):
    #num.append(int(input("Informe um valor: ")))
    num[i]=int(input("Informe um valor: "))
num.reverse()
for i in num:
    print(i)