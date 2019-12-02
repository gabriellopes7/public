from random import randint

num = (randint(0,80),randint(0,80),randint(0,80),randint(0,80),randint(0,80))
print(num)
menor = 99
maior = 0
for item in num:
    print(item, end=' ')
    if item>maior:
        maior = item
    if item<menor:
        menor = item
print('')
print(f'O maior número da Tupla é: {maior}')
print(f'O menor número da Tupla é: {menor}')
print(f'Maior valor {max(num)}\nMenor valor {min(num)}')