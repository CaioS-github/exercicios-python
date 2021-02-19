print('-!-' * 15)
print('Detran')
print('-!-' * 15)
velocidade = float(input('Qual a velocidade que o carro estava? '))
if velocidade > 80:
    print('Você foi multado!')
    multa = (velocidade - 80) * 7.0
    print('O valor da multa é {}'.format(multa))
print('Ah, okay... Tenha um ótimo dia!')