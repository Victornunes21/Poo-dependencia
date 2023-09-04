print("1 - Média aritmética")
print("2 – Média ponderada")
print("3 – Sair")
for i in range(1000):
    nmr = int(input("Manda ai um númro ai: "))
    if nmr == 1:
        print("Vamos fazer uma media simples!")
        n1 = int(input("Manda ai 0 1° número: "))
        n2 = int(input("Manda ai o 2º número: "))
        media = (n1 + n2) / 2
        print(f"A media simples dos 2 números digitados foram {media}")
    elif nmr == 2:
        print("Vamos fazer uma media ponderada")
        n1 = int(input("Manda ai 0 1° número: "))
        p1 = int(input("Informe o 1º peso: "))
        n2 = int(input("Manda ai o 2º número: "))
        p2 = int(input("informe o 2º peso: "))
        n3 = int(input("informe o 3º numero: "))
        p3 = int(input("informe o 3º peso: "))
        media = (n1 * p1 + n2 * p2 + n3 * p3) / n1 + n2 + n3
        print(f"A media ponderada dos números digitados foram {media}")
    elif nmr == 3:
        break