valor = float(input('Valor do produto: R$'))
opcao = int(input('1-A vista dinheiro ou cheque\n2-A vista cartao\n3-até 2x no crédito\n4-3x ou mais no crédito\nDigite opcao desejada: '))
if opcao == 1:
    print('Valor com desconto R$ {:.2f}'.format(valor*0.9))
elif opcao == 2:
    print('Valor com desconto R$ {:.2f}'.format(valor*0.95))
elif opcao == 3:
    print('Valor normal R$ {:.2f}'.format(valor))
else:
    print('Valor com juros R$ {:.2f}'.format(valor*1.2))