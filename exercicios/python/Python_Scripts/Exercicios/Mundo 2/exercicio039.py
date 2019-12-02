from datetime import date
hoje = date.today().year
ano = int(input('Digite o ano de nascimento: '))
if hoje-ano<18:
    print('Ainda vai se alistar, em {} ano(s)'.format(18-(hoje-ano)))
elif hoje-ano==18:
    print('Esta na hora de se alistar')
else:
    print('Passou {} ano(s) do tempo de alistamento'.format(hoje-ano-18))

