n = int(input('Digite um numero: '))
cont =0
for c in range(n,0,-1):
    if n%c ==0:
        cont+=1
if cont == 2:
    print('O numero é primo')
else:
    print('O numero não é primo')

