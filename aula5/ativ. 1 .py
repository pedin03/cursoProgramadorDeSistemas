print("Informe M para masculino ou F para feminino.")
sex=input("")
match sex:
    case "M":
        print("Sexo masculino.")
    case "F":
        print("Sexo feminino.")
    case _:
        print("Caractere inválido.")