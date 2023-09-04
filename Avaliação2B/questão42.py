
cnl4 = 0
cnl5 = 0
cnl7 = 0
cnl12 = 0
ass4 = 0
ass5 = 0
ass7 = 0
ass12 = 0
for i in range(1,11):
    cnl = int(input("Informe o canal que você estar assistindo: "))
    qnt = int(input("Informe a quantidade de pessoas que estão assistindo este canal: "))
    if cnl == 4:
        cnl4 += 1
        ass4 += qnt 
    elif cnl == 5:
        ass5 += qnt
        cnl5 += 1
    elif cnl == 7:
        ass7 += qnt
        cnl7 += 1
    elif cnl == 12:
        ass12 += qnt
        cnl12 += 1
total = ass12 + ass4 + ass5 + ass7
print(f"A porcentagem de audiencia do canal 4 foi de {(cnl4/total) * 100}")
print(f"A porcentagem da audiencia do canal 5 foi de {(cnl5/total) * 100}")
print(f"A porcentagem da audiencia do canal 7 foi de {(cnl7/total) * 100}")
print(f"A porcentagem da audiencia do canal 12 foi de {(cnl12/total) * 100}")

