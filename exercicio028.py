from random import randint
print('Tente advinhar um número entre 0 e 5')
num_dig = int(input('Digite aqui seu palpite: '))
valor = randint(0, 5)
print('O valor escolhido pelo computador foi {}.'.format(valor))
if valor == num_dig:
    print('Acertou! Tá colando, é? Meus parabéns!')
else:
    print('HAHA! Erooooooouuuu! kkkkkkkkkkkkkkkk')