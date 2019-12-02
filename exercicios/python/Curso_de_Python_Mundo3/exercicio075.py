
t = (int(input('Digite um número: ')),int(input('Digite um número: ')),int(input('Digite um número: ')),
     int(input('Digite um número: ')))

print(f'Valores digitados: {t}')
c9 = 0
pares = 0
for item in t:
    if item%2==0:
        pares+=1
    if item==9:
        c9+=1
print(f'O valor 9 apareceu {c9} vezes')
if 3 in t:
    print(f'O valor 3 apareceu na {t.index(3)+1}º posição')
else:
    print('O valor 3 não foi digitado')
print(f'Foram digitados {pares} valores pares')
