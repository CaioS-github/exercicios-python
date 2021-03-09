num = int(input('Digite o número que quer ver a tabuada: '))
for tab in range(1, 11):
    total = num * tab
    print('{} * {} = {}'.format(num, tab, total))