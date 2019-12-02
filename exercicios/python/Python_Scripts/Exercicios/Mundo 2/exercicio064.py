n = 0
soma = 0
c=0
while n!= 999:
    n = int(input('Digite um numero inteiro: '))
    if n!=999:
        soma += n
        c+=1
print('Foram digitados {} numeros'.format(c))
print('A soma dos numeros digitados é {}'.format(soma))