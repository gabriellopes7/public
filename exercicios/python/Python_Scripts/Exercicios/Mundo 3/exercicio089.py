aluno =[]
listaAluno=[]
while True:
    aluno.append(input('Nome: '))
    aluno.append(int(input('Nota 1: ')))
    aluno.append(int(input('Nota 2: ')))
    listaAluno.append(aluno[:])
    opcao = input('Deseja continuar [S/N] ? ')
    while opcao.lower()!='s' and opcao.lower()!='n':
        opcao = input('Deseja continuar [S/N] ? ')
    if opcao.lower()=='n':
        break
print(f'{"Boletim":^20}')
print('='*20)
for pos, a in enumerate(listaAluno):
    print(f'Nome: {a[pos,0]}')
    print(f'Média: {(a[pos,1]+a[pos,2])/2:.2f}')
    print('-'*20)
notas = input('Deseja ver a nota de algum aluno [S/N]? ')
while notas.lower()!='s' and notas.lower()!='n':
    notas = input('Deseja ver a nota de algum aluno [S/N]? ')
if notas.lower()=='s':
    escolha = input('Digite o nome do aluno: ')
else:
    print('Finalizado')
if escolha in listaAluno:
    for a in listaAluno:
        if a[0]==escolha:
            print(f'Nota 1: {a[1]:.2f}')
            print(f'Nota 2: {a[2]:.2f}')
else:
    print('Aluno não encontrado !')
