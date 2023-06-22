n1 = float(input("Manda o Primeiro número: "))
n2 = float(input("Manda o Segundo número: "))

simbolo = input("Manda o Simbolo da operação que você quer fazer: ")
if simbolo == "*":
    mult = n1 * n2
    print("A multiplicação entre n1 e n2 é",mult)
elif simbolo == "+":
    soma = n1 + n2
    print("A soma entre n1 e n2 é", soma)
elif simbolo == "-":
    subt = n1 - n2
    print("A subtração entre n1 e n2 é", subt)
elif simbolo == "/":
    div = n1 / n2
    print("A divisão de n1 por n2 é de", div)