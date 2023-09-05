print("1 – Novo salário")
print("2 – Férias")
print("3 – Décimo terceiro")
print("4 – Sair")
for i in range(1,11):
    opcao = int(input("Digite uma das opções acima: "))
    if opcao == 1:
        salario = float(input("Manda ai teu salario: "))
        if salario <= 210:
            nvsalario = salario +(salario * 15 / 100) 
            print(f"O seu novo salario sera de {nvsalario:.2f}")
        elif salario > 210 and salario <= 600:
            nvsalario = salario + (salario * 10 / 100) 
            print(f"O seu novo salario sera de {nvsalario:.2f}")
        elif salario > 600:
            nvsalario = (salario * 5 /100) 
            print(f"O seu novo salario sera de {nvsalario:.2f}")
    elif opcao == 2:
        salario = float(input("Digite seu salario: "))
        ferias = salario + (salario / 3)
        print(f"O valor das férias do funcionário é: R$ {ferias:.2f}")
    elif opcao == 3:
        salario = float(input("Manda ai seu salario: "))
        meses = int(input("Quantos meses você trabalhou: "))
        decimo_terceiro = (salario * meses) / 12
        print(f"O valor do seu decimo terceiro é de {decimo_terceiro:.2f}")
        
    else:
        break
