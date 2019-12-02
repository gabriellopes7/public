lista = []
maior = 0
menor = 999999
for item in range (0,5):
    lista.append(int(input('Digite um número: ')))
    if lista[item] > maior:
        maior = lista[item]
    if lista[item] < menor:
        menor = lista[item]
print(f'O maior elemento é {maior} na posição ',end='')
for i,c in enumerate(lista):
    if lista[i] == maior:
        print(f'{i}...',end='')
print('')
print(f'O menor elemento é {menor} na posição ',end='')
for i,c in enumerate(lista):
    if lista[i]==menor:
        print(f'{i}...',end='')