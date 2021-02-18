nome = str(input('Digite seu nome: ')).strip()
aluno = nome.split()
print('****************************************************')
print('A média para passar na escola São José de Deus é 7.0')
print('****************************************************')
n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
m = (n1 + n2)/2
print('A sua média foi {}'.format(m))
if m >= 7.0:
    print('Sua média foi muito boa, meu caro. Continue assim, {}'.format(aluno[0]))
else:
    print('Sua média não foi boa, cara... Você tem que melhorar isso aí, {}.'.format(aluno[0]))