b = float(input('Digite a largura da parede que você quer pintar: '))
h = float(input('Agora digite a altura: '))
area = b * h
litros = area / 2
print('A quantidade necessária para pintar {:.1f} metros quadrados é de {:.1f}l.'.format(area, litros))