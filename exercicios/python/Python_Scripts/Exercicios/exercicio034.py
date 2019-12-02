salario = float(input('Digite seu salário: R$'))
print('Seu novo salário é R${:.2f}'.format(salario*1.1) if salario>1250 else 'Seu novo salário é R$ {:.2f}'.format(salario*1.15))