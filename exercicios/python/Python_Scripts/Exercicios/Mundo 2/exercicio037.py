n = int(input('Digite um numero: '))
print('1-Binário\n2-Octal\n3-Hexadecimal')
opcao = int(input('Digite a base de conversão: '))
if opcao == 1:
    print('Numero em binario {}'.format(bin(n)[2:]))
elif opcao ==2:
    print('Numero em octal {}'.format(oct(n)[2:]))
else:
    print('Numero em hexadecimal {}'.format(hex(n)[2:]))
