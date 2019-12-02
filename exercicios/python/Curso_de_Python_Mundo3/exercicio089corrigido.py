aluno =[]
while True:
    nome=input('Nome: ')
    nota1=float(input('Nota 1: '))
    nota2=float(input('Nota 2: '))
    media = (nota1+nota2)/2
    aluno.append([nome,[nota1,nota2],media])
    opcao = input('Deseja continuar [S/N] ? ')
    while opcao not in 'Ss' and opcao not in 'Nn':
        opcao = input('Deseja continuar [S/N] ? ')
    if opcao.lower() == 'n':
        break
print('-'*30)
print(f'{"Nº":<3}{"NOME":<10}{"MÉDIA":>8}')
for i,a in enumerate(aluno):
    print(f'{i+1:<3}{a[0]:<10}{a[2]:>8}')
print('-'*30)
while True:
    opcao = input('Deseja ver nota de aluno [S/N] ? ')
    while opcao not in 'Ss' and opcao not in 'Nn':
        opcao = input('Deseja ver nota de aluno [S/N] ? ')
    if opcao.lower() == 'n':
     break
    numero = int(input('Digite o número do aluno: '))
    if numero <= len(aluno):
        print(f'Nome: {aluno[numero-1][0]}')
        print(f'Nota 1: {aluno[numero-1][1][0]}')
        print(f'Nota 2: {aluno[numero-1][1][1]}')
    else:
        print('Numero do aluno não encontrado !')