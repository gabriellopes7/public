n = int(input('Quantos elementos da sequencia de Fibonacci que deseja ver ? '))
c = 0
n1 = 1
n2 = 1
aux =0
print(aux)
print(n1)
print(n2)
while c<n-3:
    aux=n1+n2
    print(aux)
    n1 = n2
    n2 = aux
    c+=1
print('Encerrado')
