from datetime import date
atual = date.today().year
for p in range(1, 7):
    nome = str(input('Nome da primeira pessoa: ').strip(' '))
    nascimento = int(input('Agora digite o ano que nasceu: '))
    idade = atual - nascimento
    print('{}, você tem {} anos'.format(nome, idade))
    if idade < 21:
        print('{} é menor de idade'.format(nome).upper())
    else:
        print('{} é de maior de idade.'.format(nome).upper())
print('FIM')