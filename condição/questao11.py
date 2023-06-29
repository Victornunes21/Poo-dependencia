print("Vamos calcular o seu IMC")
peso = float(input("manda ai o teu peso: "))
altura = float(input("manda também a tua altura: "))
IMC = peso / (altura **2)
print("O seu imc é {:.2f}".format(IMC))
if IMC < 18.5:
    print("Bixu, tu tá abaixo do peso!")
elif IMC == 18.5 or IMC < 25.5:
    print("Você esta com o peso normal!")
elif IMC == 25.5 or IMC <= 30:
    print("Bixu, toma cuidado! você esta acima do peso!")
elif IMC > 30:
    print("Boy! vamos fazer umas caminhadas ai pq você já ta obeso!")
