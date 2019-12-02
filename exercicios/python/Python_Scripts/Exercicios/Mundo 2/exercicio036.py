valor = float(input('Digite o valor da casa: R$'))
salario = float(input('Digite o salario do comprador: R$'))
anos = int(input('Em quantos anos deseja pagar: '))
prest = anos*12
valorPrest = valor/prest
if valorPrest > 0.3*salario:
    print('Empréstimo negado')
else:
    print('Empréstimo aprovado')