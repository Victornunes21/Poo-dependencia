nascimento = int(input("Qual o seu ano de nascimento? "))
idade = 2023 -nascimento
if idade == 16 or idade == 17 :
    print("Você já tem idade para votar!")
elif idade >= 18:
    print("Você já tem idade para consegui a Carteira de Habilitação!")
else:
    print("boy tu não tem idade nem para votar quanto mais para dirigir!")