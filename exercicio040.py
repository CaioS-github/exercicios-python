nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
if media >= 7.0:
    print('APROVADO')
elif media > 5.1 and media < 6.9:
    print('RECUPERAÇÃO')
elif media < 5.0:
    print('REPROVADO')