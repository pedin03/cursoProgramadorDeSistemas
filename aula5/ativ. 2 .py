print("Escolha uma das opções abaixo:")
print("1. Fazer check-in.")
print("2. Chamar serviço de quarto.")
print("3. Fazer pedido.")
print("4. Fazer check-out.")
opção=int(input(""))

match opção:
    case 1:
        print("Check-in realizado com suceso, aproveite!")
    case 2:
        print("Serviço de quarto acionado, espere um momento.")
    case 3:
        print("Faça seu pedido.")
    case 4:
        print("Check-out realizado, volte sempre!")