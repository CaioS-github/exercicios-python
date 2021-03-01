print('Alistamento - veja se já passou do tempo.'.upper())
print('Digite a sua data de nascimento na sequência: dia, mês e ano.')
dia = int(input('Dia: '))
mes = int(input('Mês: '))
ano = int(input('Ano: '))
idade = 2021 - ano
print(idade)
if idade > 18:
    print('****SITUAÇÃO****')
    print('Você passou da idade de alistar-se.')
elif idade == 18:
    print('****SITUAÇÃO****')
    print('Está no período de alistar-se, meu caro.')
elif idade < 18:
    print('****SITUAÇÃO****')
    print('Ainda não está no período.')
print('Obrigado por usar nosso sistema. Até mais!')