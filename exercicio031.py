print('=-=' * 10)
print('CAIO TRANSPORTE LTDA')
print('=-=' * 10)
nome = input('Qual o seu nome? ')
numero = float(input('Qual a distância que você percorrirá? R$'))
if numero < 200:
    opcao1 = numero * 0.50
    print('O valor pago será R${}.'.format(opcao1))
else:
    opcao2 = numero * 0.45
    print('Na promoção você pagará R${}'.format(opcao2))
print('Agradecemos pela preferência, {}. Volte sempre.')