print('Compra de dólar')
real = float(input('Quanto você tem na carteira em reais? R$'))
dol = real / (5.36)
print('Com R${} você pode comprar U${:.2f}'.format(real, dol))