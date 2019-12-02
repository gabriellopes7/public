#Tuplas são imutáveis
lanche = ('Hamburguer','Suco','Pizza','Pudim')
print(lanche)
print(lanche[-1])
print(lanche[-3:])
for c in lanche:
    print(c, end=' ')

print('')
for pos,comida in enumerate(lanche):
    print(pos,'-',comida)

print(sorted(lanche)) #organiza em ordem alfabética