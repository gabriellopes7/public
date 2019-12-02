contagem = ('Zero','Um','Dois','Três','Quatro',
            'Cinco','Seis','Sete','Oito','Nove','Dez')
opcao = int(input('Digite um número de 0 a 10: '))
while opcao<0 and opcao>10:
    print('Opcao inválida, tente novamente')
    opcao = int(input('Digite um número de 0 a 10: '))
print(f'Você digitou o número {contagem[opcao]}')
