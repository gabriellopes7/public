estado = {}
brasil = []
for c in range(0,3):
    estado['uf'] = input('Digite o estado: ')
    estado['sigla'] = input('Digite a sigla: ')
    brasil.append(estado.copy())
    estado.clear()
print(brasil)
for e in brasil:
    print(e)
for e in brasil:
    for s in e.values():
        print(s)