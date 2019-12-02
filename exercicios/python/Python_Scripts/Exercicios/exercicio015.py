dias = int(input('Digite a quantidade de dias alugado: '))
km = int(input('Digite a quantidade de kms rodados: '))
total = dias*60 + km*0.15
print('O total a pagar será de {:.2f} reais'.format(total))