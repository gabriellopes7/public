valores =[]
while True:
    n = int(input('Digite um número: '))
    if valores.__contains__(n) == False:
        valores.append(n)
    opcao = input('Deseja continuar [S/N]? ')
    while opcao.lower()!='s' and opcao.lower()!='n':
        opcao = input('Deseja continuar [S/N]? ')
    if opcao.lower() == 'n':
        break
valores.sort()
for c in valores:
    print(f'{c}...',end='')