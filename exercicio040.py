nome = str(input('Qual o nome do aluno? '))
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
if media >= 7.0:
    print('{}, você está APROVADO com a média de {:.1f}.'.format(nome, media))
elif media > 5.1 and media < 6.9:
    print('{}, você está de RECUPERAÇÃO, pois sua média foi de {}.'.format(nome, media))
elif media < 5.0:
    print('{}, você está REPROVADO e sua média foi de {}.'.format(nome, media))