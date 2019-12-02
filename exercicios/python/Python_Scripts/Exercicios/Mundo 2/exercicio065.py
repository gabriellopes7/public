c = 0
continuar = 's'
soma = 0
maior =0
menor = 99999
while continuar.lower() == 's':
    n = int(input('Digite um valor inteiro: '))
    soma+=n
    c+=1
    if n>maior:
        maior = n
    if n<menor:
        menor = n
    continuar = input('Deseja continuar ? [S/N]')
    while continuar.lower() != 's' and continuar.lower() != 'n':
        print('Opcao inválida, tente novamente. ')
        continuar = input('Deseja continuar ? [S/N]')
print('Maior valor: {}'.format(maior))
print('Menor valor: {}'.format(menor))
print('Média: {:.2f}'.format(soma/c))

