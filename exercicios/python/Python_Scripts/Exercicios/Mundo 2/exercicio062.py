n = int(input('Digite o numero: '))
r = int(input('Digite a razão: '))
res = n
c = 0
termos = int(input('Digite a quantidade de termos que deseja ver: '))
print(res,end='')
while c<termos-1:
    res +=r
    print(' -> ',res,  end='')
    c+=1
    if c == termos-1:
        print('')
        novos = int(input('Quantos termos deseja ver mais: '))
        if novos != 0:
            print(res, end='')
        termos += novos
print('Programa encerrado !')
