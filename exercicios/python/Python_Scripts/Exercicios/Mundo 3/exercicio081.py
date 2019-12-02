valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    opcao = input('Deseja continuar [S/N] ? ')
    while opcao.lower()!='s' and opcao.lower()!='n':
        opcao = input('Deseja continuar [S/N] ? ')
    if opcao.lower()=='n':
        break
print(valores)
print(f'Foram digitados {len(valores)} números')
valores.sort(reverse=True)
print(valores)
if 5 in valores:
    print('O valor 5 foi digitado')
else:
    print('O valor 5 não está na lista')