preco = float(input("brothe, quanto foi esse produto: "))
pagam = int(input("broth, qual vai ser a forma de pagamento de compra: "))
if pagam == 1:
    npreco = preco - (preco * 10 / 100)
    print("O novo valor do produto é de", npreco)
elif pagam == 2:
    precon = preco - (preco * 5/ 100)
    print("O novo preço é de ", precon)
elif pagam == 3:
    print("Brothe, dessa forma o preço continua o mesmo!")
elif pagam == 4:
    novop = preco + (preco * 10/100)
    print("Brthe, o preço deu uma aumentada, agora custa", novop)
else:
    print("Número invalido!")