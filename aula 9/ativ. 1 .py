alunos=["Luiz Carlos","Luiz Gustavo","Luiz Felipe","Maynara","Arthur","Anderson","Gabriel","Luana","Higor","Pedro","Felipe"]
letra="A"
contador=0
for i in alunos:
    print(i)
alunos.insert(11,"Adrian")
for i in alunos:
    if i.startswith(letra):
        contador+=1
print()
print(contador,"Nomes que começam com A")
alunos.insert(11,"Adrian")







