estado1 = {'uf': 'Rio de Janeiro','sigla':'RJ'}
estado2 = {'uf':'São Paulo','sigla':'SP'}
brasil = []
brasil.append(estado1)
brasil.append(estado2)
print(estado1)
print(estado2)
print(brasil)
print(brasil[0])
print(brasil[1])
print(brasil[0]['uf'])
print(brasil[1]['sigla'])

#printando cada elemento da lista
for v,c in enumerate(brasil):
    print(f'{c["uf"]}-{c["sigla"]}')