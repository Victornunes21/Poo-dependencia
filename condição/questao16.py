idade = 51
if idade <= 15:
    print("Não votante!")
if idade == 16 or idade == 17 or idade > 65:
    print("Voto facultativo!")
elif idade > 18 or idade == 65:
    print("Eleitor obrigatorio!")