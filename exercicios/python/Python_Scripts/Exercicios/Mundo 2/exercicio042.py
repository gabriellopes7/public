a = int(input('Lado A: '))
b = int(input('Lado B: '))
c = int(input('Lado C: '))
if a+b>c and b+c>a and c+a>b:
    print('Formam um triângulo')
    if a==b and b==c:
        print('Equilatero')
    elif a==b or a==c or b==c:
        print('Isosceles')
    else:
        print('Escaleno')
else:
    print('Não formam um triângulo')