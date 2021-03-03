num = int(input('Insira um número aqui: '))
print('Opções para converter: '
      '\n [ 1 ] - BINÁRIO'
      '\n [ 2 ] - OCTAL'
      '\n [ 3 ] - HEXADECIMAL')
escolhido = int(input('Digite a opção para converter o número digitado: '))
if escolhido == 1:
    print('{} convertido para BINÁRIO é {}'.format(num, bin(num)[2:]))
elif escolhido == 2:
    print('{} convertido para OCTAL é {}'.format(num, oct(num)[2:]))
elif escolhido == 3:
    print('{} convertido para HEXADECIMAL é {}'.format(num, hex(num)[2:]))
else:
    print('Essa opção não existe. Tente novamente.')