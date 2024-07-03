contador=0
print("Insira V ou F para as perguntas a seguir.")
print("Telefonou para a vítima?")
a=input("")
print("Esteve no local do crime?")
b=input("")
print("Mora perto da vítima?")
c=input("")
print("Devia para a vítima?")
d=input("")
print("Já trabalhou com a vítima?")
e=input("")

if a=="V":
    contador+=1
if b=="V":
    contador+=1
if c=="V":
    contador+=1
if d=="V":
    contador+=1
if e=="V":
    contador+=1

if contador==2:
    print("Você é um suspeito.")
if contador==3 or contador==4:
    print("Você é cúmplice.")
if contador==5:
    print("Você é o assasino!")