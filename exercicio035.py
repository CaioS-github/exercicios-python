print('=-='*10)
print('Analise os segmentos do triângulo')
print('=-='*10)
a = float(input('Digite o segmento do triângulo lado(a): '))
b = float(input('Digite o segmento do triângulo lado(b): '))
c = float(input('Digite o segmento do triângulo lado(c): '))
if a < b + c and b < a + c and c < b + a:
    print('Esses segmentos fazem um triângulo.')
else:
    print('O triângulo não é possível neste caso.')