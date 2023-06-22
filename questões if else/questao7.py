codigo = int(input("Manda o codigo desse produto: "))
if codigo == 1:
    print("Esse produto é não perecivel!")
if codigo == 2 or codigo == 3 or codigo == 4:
    print("Alimento perecivel!")
if codigo == 5 or codigo == 6:
    print("Vestuario!")
if codigo == 7:
    print("Higiene Pessoal!")
if codigo  >= 8 or codigo == 15:
    print("Limpeza e utensílios domesticos!")
elif codigo > 15:
    print("Ivalido!")