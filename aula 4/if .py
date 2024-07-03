n1=float(input("Informe a nota 1: "))
n2=float(input("Informe a nota 2: "))

med=(n1+n2)/2

if med>=7:
    print("Aluno aprovado!")
elif med>=5:
     print("Aluno de recuperação!")
else:
       print("Aluno reprovado!")