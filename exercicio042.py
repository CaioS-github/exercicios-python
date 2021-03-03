print('=-='*10)
print('Analise os segmentos do triângulo')
print('=-='*10)
a = float(input('Digite o segmento do triângulo lado(a): '))
b = float(input('Digite o segmento do triângulo lado(b): '))
c = float(input('Digite o segmento do triângulo lado(c): '))
triangulo = a < b + c and b < a + c and c < b + a
if triangulo:
    print('Esses segmentos fazem um triângulo.')
else:
    print('O triângulo não é possível neste caso.')
if a == b == c:
    print('O triângulo é EQUILÁTERO.')
elif a != b !=c:
    print('O triângulo é ESCALENO.')
elif a==b!=c and a==c!=b and b==c!=a:
    print('O triângulo é ISÓCELES.')