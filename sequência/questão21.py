cont = 0
acum = 0
maiorn = 0
menorn = 500000
for i in range(1,11):
    numero = int(input("Manda ai uns numeros: "))
    acum = acum + numero
    media = acum / 10
    if numero > maiorn:
        maiorn = numero
        if numero < menorn:
            menorn = numero
        else:
            continue
    else:
        continue
    

    

print(f"A soma de todos os números é igual á {acum}")
print(f"A média dos números digitados é igual á {media}")
print(f"O maior número digitados foi {maiorn}")
print(f"O menor número digitado foi {menorn}")