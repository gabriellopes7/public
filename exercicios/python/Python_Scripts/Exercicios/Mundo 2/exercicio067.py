c=0
while True:
    n = int(input('Digite um número: '))
    if n<0:
        break
    for c in range (0,11):
        print(f'{c} x {n} = {c*n}')
        c+=1
print('Programa encerrado')
