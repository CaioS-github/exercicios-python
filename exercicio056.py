soma_idade = 0
media_idade = 0
maior_idade_homem = 0
nome_velho = ''
total_mulheres20 = 0
for p in range(1, 5):
    print('----- {}º PESSOA -----'.format(p))
    nome = str(input('Nome: ')).upper()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper()
    soma_idade += idade #Aqui a SOMA_IDADE recebe a idade de cada pergunta feita no questionário.
    if p == 1 and sexo == 'M':
        maior_idade_homem = idade
        nome_velho = nome
    if sexo == 'M' and idade > maior_idade_homem: #Quando for HOMEM e a IDADE for maior que a idade do grupo dos homens
        maior_idade_homem = idade #A idade maior que valerá
        nome_velho = nome       #Neste caso o nome do mais velho está atrelado a idade
    if sexo == 'F' and idade < 20: #Quando SEXO for FEMININO e a IDADE dela for menor que 20 anos de idade
        total_mulheres20 += 1       #Aqui soma quantas mulheres existem na lista
media_idade = soma_idade / 4 #Aqui o código vai mostrar a soma da idade e dividir por 4 e armazenar o resultado na VAR media_idade
print('A de idade do grupo é de {} anos.'.format(media_idade))
print('{} é o homem mais velho do grupo e tem {} anos.'.format(nome_velho, maior_idade_homem))
print('Ao todo há {} mulheres.'.format(total_mulheres20))