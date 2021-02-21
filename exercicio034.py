salario = float(input('Insira o valor do seu salário para saber o reajuste: '))
if salario > 1250.00:
    aumento_de_10 = salario + salario * 0.10
    print('Você receberá a partir de hoje R${} com o ajuste de 10 porcento.'.format(aumento_de_10))
else:
    aumento_de_15 =  salario + salario * 0.15
    print('Você receberá a partir de hoje R${} com o ajuste de 15 porcento'.format(aumento_de_15))
print('Obrigado por usar nosso serviço. Até a próxima!')