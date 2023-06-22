print("Vamos calcular seu peso ideal")
sexo = input("Digite se sexo: ")
altura = float(input("Digite sua altura: "))
if sexo == "masculino":
    peso = (72.7 * altura)- 58
    print("Seu peso ideal é {:.2f}".format (peso))
elif sexo == "feminino":
    peso =(62.1 * altura) - 44.7
    print("Seu peso ideal é ", peso)
else:
    print("sexo invalido!")
