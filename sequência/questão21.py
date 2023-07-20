cont = 0
acum = 0
qnt = 0
contp = 0
conti = 0
acup = 0
mediap = 0
for i in range(1,11):
    numero = int(input("Manda ai uns numeros: "))
    acum = acum + numero
    qnt = qnt + 1
    media = acum / 10
    if  qnt == 1:
        maior = numero
        menor = numero
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero


    if numero % 2 == 0:
        acup += numero
        contp += 1
        mediap = acup / contp
    else:
        conti += 1
        porcentagem = (conti / 10) * 100

print(f"A soma de todos os números é igual á {acum}")
print(f"A quantidade de numeros digitados foi de {qnt}")
print(f"A média dos números digitados é igual á {media}")
print(f"O maior número digitado foi {maior}")
print(f"O menor número digitado foi {menor}")
print(f"A média dos números pares é de {mediap}")
print(f"A porcentagem dos numeros inmpares foi de {porcentagem}% ")