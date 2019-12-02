n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
n3 = int(input('Terceiro número: '))
if n1>n2 and n1>n3:
    print('{} é o maior número'.format(n1))
    print('{} é o menor número'.format(n3) if n2>n3 else '{} é o menor número'.format(n2))
else:
    if n2>n3:
        print('{} é o maior número'.format(n2))
        print('{} é o menor número'.format(n3) if n1>n3 else '{} é o menor número'.format(n1))
    else:
        print('{} é o maior número'.format(n3))
        print('{} é o menor número'.format(n2) if n1>n2 else '{} é o menor número'.format(n1))