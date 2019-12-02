matriz = [[0,0,0],[0,0,0],[0,0,0]]
spares = terceira = segunda= 0

for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input('Digite um número: '))
        if matriz[l][c]%2==0:
            spares += matriz[l][c]
        if c==2:
            terceira+=matriz[l][c]
        if l==1:
            segunda+=matriz[l][c]
for l in range(0,3):
    for c in range(0,3):
        print(f'{matriz[l][c]:3} ',end='')
    print('')
print(f'A soma dos valores pares é {spares}')
print(f'A soma da terceira coluna é {terceira}')
print(f'A soma da segunda linha é {segunda}')
