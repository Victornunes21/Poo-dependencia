contf = 0
contm = 0
hex = 0
aidade = 0
id46 = 0
cont22 = 0
for i in range(1,5):
    idade = int(input("Digite sua idade: "))
    sex = input("Digite seu sex: [F/M]")
    ex = input('Tem Experiência:[S/N]')
    if sex == "M" or sex =="m":
        contm += 1
    elif sex == "F" or sex =="f":
        contf += 1
    else:
        print("Invalido!")

    if sex == "M" and ex == "S":
        hex +=1
        aidade +=idade
        media = aidade / hex
    if sex == "M" and idade > 45:
        id46 += 1
        porcet = (id46 / 4) * 100

    if sex == "F" and idade < 21 and ex == "S":
        cont22 = cont22 + 1

        
    
    
       
print(f"A Quantidade de candidatos homens é {contm}")
print(f"A quantidade de canditadas mulheres é {contf}")
print(f"A média das idades dos condidatos masculino que já tem experiêcia é {media}")
print(f"A porcentagem dos homes com mais que 45 anos é de {porcet}%")
print(f"A quantidade de candidatas mulheres com nemos de 21 anos e com experiencia é de {cont22}")


