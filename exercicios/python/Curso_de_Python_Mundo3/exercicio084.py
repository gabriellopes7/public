pessoa = []
galera=[]
while True:
    pessoa.append(input('Nome: '))
    pessoa.append(float(input('Peso: ')))
    galera.append(pessoa[:])
    pessoa.clear()
    opcao=input('Deseja continuar [S/N] ? ')
    while opcao.lower()!='s' and opcao.lower()!='n':
        opcao = input('Deseja continuar [S/N] ? ')
    if opcao.lower() =='n':
        break
print(f'Foram cadastradas {len(galera)} pessoas')
soma=0
for p in galera:
    soma+=p[1]
media = soma/len(galera)
leves =[]
pesadas=[]
for p in galera:
    if p[1]<media:
        leves.append(p)
    else:
        pesadas.append(p)
print('Mais leves:')
for p in leves:
    print(f'{p[0]} com {p[1]:.2f}kg')
print('Mais pesadas: ')
for p in pesadas:
    print(f'{p[0]} com {p[1]:.2f}kg')