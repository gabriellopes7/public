from datetime import date
s=0
for c in range(0,7):
    ano = int(input('Digite o ano de nascimento da {} ª pessoa: '.format(c+1)))
    if date.today().year - ano >=18:
        s+=1
print('Há {} pessoas maiores de idade'.format(s))