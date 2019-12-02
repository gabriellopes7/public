c = 0
menor = 99999999999
mNome = ''
s=0
while True:
    nome = input('Digite o nome do produto: ')
    preco = float(input('Digite o preço do produto: R$'))
    if preco<menor:
        menor = preco
        mNome = nome
    if preco>1000:
        c+=1
    s+=preco
    opcao = input('Deseja continuar [S/N]? ')
    while opcao.lower()!='s' and opcao.lower()!='n':
        print('Opcao inválida')
        opcao = input('Deseja continuar [S/N]?')
    if opcao.lower() =='n':
        break
print(f'O total gasto foi de R${s:.2f}')
print(f'Há {c} produtos que custam mais de R$ 1000,00')
print(f'O produto mais barato é {mNome} no valor de R${menor:.2f}')
