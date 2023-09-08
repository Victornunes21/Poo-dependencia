

mulher = 0
slr = 0
acmS = 0 
menorS = 0
maiorS = 0
for i in range(1,11):
    salario = int(input("Infome seu salario: "))
    idade = int(input("Informe sua idade: "))
    sex = input("Informe seu sexo: ")

    acmS += salario
    if i == 1:
        maior = menor = idade
    if idade > maior:
        maior = idade
    if idade < menor:
        menor = idade

    if sex == "f" and salario <= 200:
        mulher += 1

    if i == 1:
       menorS = maiorS = salario
    if salario < menorS:
        menorS = salario
        sexoM = sex
        idadeM = idade
         
print(f"O menor salario foi de {menorS} e a pessoa tem {idadeM} anos e é do sexo {sexoM}")
print(f"A media dos salarios foram de {acmS/10}")
print(f"A quantidade de mulheres com salario de ate 200R$ foi de {mulher} mulheres")
print(f"A menor idade coletada foi {menor} e a maior idade foi {maior}") 