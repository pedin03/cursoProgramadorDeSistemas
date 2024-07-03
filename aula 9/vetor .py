marcas=["Porsche","Lamborghinni","Jaguar","Ferrari","Ford","Chevrolet","Land Rover","Rolls Royce"]
#print(marcas[3])
marcas[0]
#print(marcas[0])

#marcas.append("Range Rover") #Adicionar valor no final da lista
marcas.insert(5,"Range Rover")
marcas.remove("Range Rover")
valor_removido=marcas.pop(7)


for i in marcas:
    print(i)

print("elemento removido:",valor_removido)
ocorrencias=marcas.count("Land Rover")
print("Quantas vezes apareceu o nome Land Rover?",ocorrencias,"vez(es).")
print("O vetor marcas possui",len(marcas),"marcas.")
