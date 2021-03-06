frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes na frase'.format(frase.count('A')))
print('O primeiro A aparece na posição {}'.format(frase.find('A')+1))
print('O último A apareceu na posição {}'.format(frase.rfind('A')+1))