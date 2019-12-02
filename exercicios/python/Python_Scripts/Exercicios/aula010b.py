n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1+n2)/2
print('A sua média foi {:.1f}'.format(m))
if m>=6:
    print('Sua média foi boa, parabéns')
else:
    print('Sua média foi ruim ! Estude mais')

print('Parabéns' if m>=6 else 'Estude mais') #condição simplificada