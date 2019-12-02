frase = input('Digite uma frase: ').strip().lower()
f1 = frase.split()
junto = ''.join(f1)
inverso = ''
for c in range(len(junto)-1,-1,-1):
    inverso += junto[c]
if inverso == junto:
    print('Palindromo')
else:
    print('Não é palindromo')

