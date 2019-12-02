a18 = h = m = 0
while True:
    idade = int(input('Digite a idade: '))
    if idade>18:
        a18+=1
    sexo = input('Digite o sexo [M/F]: ')
    while sexo.lower()!='m' and sexo.lower()!='f':
        print('Sexo inválido, tente novamente')
        sexo = input('Digite o sexo [M/F]: ')
    if sexo=='m':
        h+=1
    if sexo=='f' and idade<20:
        m+=1
    opcao=input('Deseja continuar [S/N]?')
    while opcao.lower()!='s' and opcao.lower()!='n':
        print('Opção inválida')
        opcao = input('Deseja continuar [S/N]?')
    if opcao=='n':
        break
print(f'Tiveram {a18} pessoas acima de 18 anos')
print(f'{h} homens cadastrados')
print(f'e {m} mulheres com menos de 20 anos')