print('=-=' * 16)
print(' *---Empréstimo para compra da casa própria---* ')
print('=-=' * 16)

nome = str(input('Qual o seu nome? '))
valor_casa = float(input('Qual o valor da casa que você quer adquirir? '))
sal = float(input('Quanto você recebe mensalmente? '))
anos = int(input("Por quantos anos pretende pagar? "))
cal_parcelas = 12 * anos #aqui multiplico a cada 1 ano digitado. Exemplo: para 2 anos serão 24 parcelas.
parcelas = valor_casa / cal_parcelas
print('As parcelas ficarão por {:.2f}'.format(parcelas))
if parcelas > sal * 0.3: #Se "parcelas" for maior que 30% do salário será negado o benefício.
    print('Sua solicitação foi NEGADA, {}'.format(nome))
else:
    print('Parabéns, {}! Você foi aprovado. Fale com o consultor para usufruir de seu benefício.'.format(nome))
print('Tenha um ótimo dia, {}'.format(nome))