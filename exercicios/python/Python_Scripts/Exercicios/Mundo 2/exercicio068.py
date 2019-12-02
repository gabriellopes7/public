from random import randint
c=0
while True:
    opcao = input('Deseja par ou ímpar ? [P/I]')
    while opcao.lower() != 'p' and opcao.lower() != 'i':
        print('Opcao inválida, tente novamente')
        opcao = input('Deseja par ou ímpar ? [P/I]')
    n = int(input('Diga um valor de 0 a 10: '))
    while n>10 and n<0:
        print('Valor inválido, digite um novo valor')
        n = int(input('Diga um valor de 0 a 10: '))
    pc = randint(0,10)
    print(f'Você jogou {n} e o computador jogou {pc}. ',end='')
    if opcao.lower() == 'p':
        if (n+pc)%2 == 0:
            print('Deu par')
            print('Você ganhou')
            c+=1
        else:
            print('Deu ímpar')
            print('Você perdeu')
            break
    elif opcao.lower() == 'i':
        if (n+pc)%2 != 0:
            print('Deu ímpar')
            print('Você ganhou')
            c+=1
        else:
            print('Deu par')
            print('Você perdeu')
            break
print(f'Você ganhou {c} vezes seguidas !')
