print('{:^30}'.format('CAIXA ELETRÔNICO'))
print('='*30)
valor = float(input('Digite o valor a ser sacado: R$'))
c =0
v =0
d=0
u=0
while valor>0:
    if valor//50!=0:
        c+=1
        valor-=50
    elif valor//20!=0:
        v+=1
        valor-=20
    elif valor//10!=0:
        d+=1
        valor-=10
    else:
        u+=1
        valor-=1
print(f'Total de {c} notas de R$50')
print(f'Total de {v} notas de R$20')
print(f'Total de {d} notas de R$10')
print(f'Total de {u} notas de R$1')
print('='*30)
print('{:^30}'.format('VOLTE SEMPRE !'))

