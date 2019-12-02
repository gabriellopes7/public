d = int(input('Digite a distância da sua viagem em KM: '))
if d <= 200:
    p = 0.5*d
else:
    p = 0.45*d
print('O preço da sua viagem de {} kms é : {:.2f}'.format(d,p))