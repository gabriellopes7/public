galera =[]
dado =[]
for c in range(0,3):
    dado.append(input('Nome: '))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
print(galera)

for pessoa in galera:
    if pessoa[1] > 18:
        print(f'{pessoa[0]} é maior de idade')
    else:
        print(f'{pessoa[0]} é menor de idade')
