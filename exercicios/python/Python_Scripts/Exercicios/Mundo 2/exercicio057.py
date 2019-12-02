s = '0'
while s != 'M' and s!='F':
    f = input("Digite o sexo [M/F]: ")
    s=f.upper()
    if s!='M' and s!='F':
        print('Sexo inválido, digite novamente !')
if s == 'M':
    print('O sexo digitado foi Masculino')
else:
    print('O sexo digitado foi Feminino')

