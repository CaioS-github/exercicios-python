import math
b = float(input('Digite o valor do cateto oposto: '))
c = float(input('Digite o valor do cateto adjacente: '))
a = b**2 + c**2
print('O valor da hipotenusa é {:.2f}.'.format(math.sqrt(a)))