slr = 0 
mulher = 0
for i in range(1,6):
    idade = int(input("Informe a sua idade: "))
    sex = input("informe seu sexo: ")
    salario = float(input("Mnada ai teu salario: "))
    
    slr += salario
    mediaS = slr / 5
    if i == 1:
        maior = menor = idade
        if maior > idade:
            maiorIdade = maior
        elif menor < idade:
            menorIdade = menor
    if sex == "f" and salario <= 200:
        mulher += 1
print(f"A media dos salarios digitados foram {mediaS}")
print(f"A maior idade digitada foi {maiorIdade} e a menor foi {menorIdade}")
print(f"A quantidade de mulheres com salario de até 200 conto foi de {mulher}")  
    
