print('-=-CONFEDERAÇÃO NACIONAL-=-')
from datetime import date
atual = date.today().year
nascimento = int(input('Qual o ano que você nasceu? '.strip()))
idade = atual - nascimento
if idade <= 9:
    print('Você está na categoria MIRIM.')
elif idade > 9 and idade <= 14:
    print('Você está na categoria INFANTIL.')
elif idade > 14 and idade <=19:
    print('Você está na categoria JUNIOR.')
elif idade > 19 and idade == 20:
    print('Você está na categoria SÊNIOR.')
elif idade > 20:
    print('Você está na categoria MASTER.')