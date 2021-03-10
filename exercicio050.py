soma = 0        #Nesta variável o programa vai acumular a soma
contador = 0    #Nesta variável o programa vai contadar
for c in range(1, 7):
    #Aqui pedirei para que o usuário digite 6 valores
    numero = int(input('Digite o {}º valor: '.format(c)))
    # No código abaixo toda vez que o programa pedir um valor novo, ele irá agregar com o valor anterior
    if numero % 2 == 0:
        soma = soma + numero # ou soma += numero
        # No código abaixo o contador vai contar quantos números foram digitados a partir de 1 e agregará no acumulador.
        contador = contador + 1 # ou contador += 1
print('A soma dos {} valores  PARES que você digitou foi {}'.format(contador, soma))