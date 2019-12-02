#montagem de matriz
matriz = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(0,3):
    for c in range (0,3):
        matriz[i][c] = int(input('Digite um número: '))
for i in range (0,3):
    for c in range(0,3):
        print(f'{matriz[i][c]:2}',end='')
    print('')

