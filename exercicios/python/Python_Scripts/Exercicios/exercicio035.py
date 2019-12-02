a = int(input('Lado A: '))
b = int(input('Lado B: '))
c = int(input('Lado C: '))
if a+b>c and b+c>a and c+a>b:
    print('Formam um triângulo')
else:
    print('Não formam um triângulo')