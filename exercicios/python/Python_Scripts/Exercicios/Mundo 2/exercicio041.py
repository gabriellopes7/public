from datetime import date
atual = date.today().year
ano = int(input('Digite o ano de nascimento do atleta: '))
idade = atual-ano
if idade <=9:
    print('MIRIM')
elif idade <=14:
    print('INFANTIL')
elif idade <= 19:
    print('JUNIOR')
elif idade <= 20:
    print('SENIOR')
else:
    print('MASTER')