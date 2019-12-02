ficha = {}
ficha['nome']=input('Nome: ')
ficha['média']=float(input('Média: '))
if ficha['média']>7.0:
    ficha['situação'] = 'Aprovado'
elif ficha['média']<5.0:
    ficha['situação'] = 'Reprovado'
else:
    ficha['situação'] = 'Recuperação'
for k,i in ficha.items():
    print(f'{k.capitalize()}: {i}')
