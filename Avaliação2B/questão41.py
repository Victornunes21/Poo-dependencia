
"""acm = 0
for i in range(1,11):
    idade = int(input("Manda ai 10 idade: "))
    acm += idade
    meida = acm/10
print(f"A media das idade digitadas foram de {meida}")"""
acm = 0
cont = 0
idade = int(input("digite uma idade: "))
while idade != 0:
    acm += idade
    cont += 1
    idade = int(input("Manda ai as idade: "))

media = acm / cont
print(f"A media das idades digitadas foram de {media}")
    
