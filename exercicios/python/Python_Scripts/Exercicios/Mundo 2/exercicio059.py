n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
c=0
while c!=5:
    print('[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos números\n[5] Sair do programa')
    c = int(input('Digite a opção desejada: '))
    if(c!=1 and c!= 2 and c!= 3 and c!= 4 and c!=5):
        print('Opcao inválida, tente novamente !')
    elif c==1:
        print('A soma é: {}'.format(n1+n2))
    elif c==2:
        print('A multiplicação é: {}'.format(n1*n2))
    elif c==3:
        if n1>n2:
            print('{} é o maior número'.format(n1))
        else:
            print('{} é o maior número'.format(n2))
    elif c==4:
        n1 = int(input('Digite o primeiro numero: '))
        n2 = int(input('Digite o segundo numero: '))
print('Programa encerrado !')
