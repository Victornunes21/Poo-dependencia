a = float(input('Valor de A: '))
b = float(input('Valor de B: '))
c = float(input('Valor de C: '))
delta = (b**2) - (4*a*c)
import math
if delta < 0:
    print('Não possui raízes reais.')
elif delta == 0:
    raiz = -b / (2*a)
    print('Possui uma raiz real = {}'.format(raiz))
else:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    print('Possui duas raízes reais: Raiz 1 = {}, Raiz 2 = {}'.format(x1, x2))