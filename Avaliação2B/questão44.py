total = 0
lucor1000 = 0
lucro200 = 0
for i in range(1,11):
    letra = input("Informe uma letra para ser comercializada: ")
    pc = float(input("Informe o preço da compra: "))
    pv = float(input("Informe o preço da venda: "))
    lucro = pv - pc
    total += lucro
    if lucro >= 1000:
        lucor1000 += 1
    elif lucro < 200:
        lucro200 += 1
    print(f"Lucro da ação {letra} foi de {lucro}R$")
print(f"A quantidade de investimento com o lucro acima de 1000 R$ foi de {lucor1000}")
print(f"A quantidade de investimento com o lucro abaixo de 200 R$ foi de {lucro200} ")
print(f"O lucro total da empresa foi de {total}")
