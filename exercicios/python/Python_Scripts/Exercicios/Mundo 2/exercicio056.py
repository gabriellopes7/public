cont = 0
soma = 0
nomeMaisVelho =''
maiorId = 0
mulheres =0
for c in range(0,4):
    nome = input('Digite o nome da {}ª pessoa: '.format(c+1))
    idade = int(input('Digite a idade da {}ª pessoa: '.format(c+1)))
    sexo = input('Digite o sexo da {}ª pessoa [M/F]: '.format(c+1))
    if idade<20 and sexo.upper() == 'F':
        mulheres+=1
    soma += idade
    cont+=1
    if idade>maiorId:
        maiorId=idade
        nomeMaisVelho = nome
print('A média de idades é {}'.format(soma/cont))
print('O mais velho se chama {}'.format(nomeMaisVelho))
print('A quantidade de mulheres com menos de 20 anos é {}'.format(mulheres))