valores = []
pares=[]
impares =[]
while True:
    n = int(input('Digite um número: '))
    valores.append(n)
    if n%2==0:
        pares.append(n)
    else:
        impares.append(n)
    opcao = input('Deseja continuar [S/N] ? ')
    while opcao.lower() != 's' and opcao.lower() != 'n':
        opcao = input('Deseja continuar [S/N] ? ')
    if opcao.lower() =='n':
        break

print(f'Valores: {valores}')
print(f'Pares: {pares}')
print(f'Impares: {impares}')
