print("Brathe! Eu vou descobrir o mamífero que você tá pesando, duvida? ")
dica = input("Esse mamífero é um quadúpedes:")
if dica == "sim":
    print("Ok! vamos continuar...")
    dica01 = input("Esse quadrúpedes é carnivoro ou herbívoro: ")
    if dica01 == "carnivoro":
        print("Então só pode ser o Rei Leão!")
    elif dica01 == "herbívoro":
        print("Então é o Cavalo!")
elif dica == "não":
    print("humm!")
    dica02 = input("Esse animal é um bípedes: ")
    if dica02 == "sim":
        print("ok! vamos continuar...")
        dica03 = input("Esse bípedes é onívoro ou frutívoro: ")
        if dica03 == "onívoro":
            print("Esse animal é o Homem!")
        elif dica03 == "frutívoro":
            print("Então, esse animal é o Macaco!")
    elif dica02 == "não":
        print("humm...")
        dica04 = input("Esse mamífero voa ou é aquatico: ")
        if dica04 == "voa":
            print("O unico mamífero que voa é o Morcego!")
        elif dica04 == "aquatico":
            print("Então brathe, só restou a Baleia!")