print('{:=^40}'.format(' Lojas Caio '))
preco = float(input('Qual o valor total? R$').strip())
print('''DIGITE UMA OPÇÃO:
    1 - Dinheiro/cheque: 10% desconto;
    2 - Débito: 5% de desconto;
    3 - Cartão até 2x: preço normal;
    4 - Cartão 3x ou mais no Cartão com 20% de juros.''')
opcao = int(input('Qual a forma de pagamento? ').strip())
pg1 = preco * 0.1
pg2 = preco * 0.05
pg3 = preco / 2
if opcao == 1:
    print('Total: {:.2f}'.format(preco - pg1))
elif opcao == 2:
    print('Total: {:.2f}'.format(preco - pg2))
elif opcao == 3:
    print('O total sairá por {:.2f} em duas parcelas de {:.2f}'.format(preco, (pg3)))
elif opcao == 4:
    parcelas = int(input('Quantas parcelas? ').strip())
    pg4 = preco + (preco * 0.20)
    print('Ficará por R${} de {} vezes somado a 20% de juros.'.format(pg4, parcelas))
print('Sua compra de {} vai custar {} no final.'.format(preco, pg4))