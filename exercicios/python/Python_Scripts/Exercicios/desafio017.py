import math
catop = float(input('Digite o cateto oposto: '))
catadj = float(input('Digite o cateto adjacente: '))
h = math.sqrt((catop**2)+(catadj**2))
hip = math.hypot(catop,catadj)
print('A hipotenusa vale : {:.2f}'.format(h))
print('A hipotenusa vale : {:.2f}'.format(hip))