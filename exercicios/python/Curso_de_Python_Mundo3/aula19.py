pessoas={'nome':'Gustavo','sexo':'M','idade':22}
print(pessoas)
print(pessoas['nome'])
print(pessoas['idade'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

for k in pessoas.keys():
    print(k)
for v in pessoas.values():
    print(v)
for i in pessoas.items():
    print(i)
for k,v in pessoas.items():
    print(f'{k}: {v}')
del pessoas['sexo']
for k,v in pessoas.items():
    print(f'{k}: {v}')
pessoas['nome'] = 'Leandro'
for k,v in pessoas.items():
    print(f'{k}: {v}')
pessoas['peso'] = 85.0
for k,v in pessoas.items():
    print(f'{k}: {v}')