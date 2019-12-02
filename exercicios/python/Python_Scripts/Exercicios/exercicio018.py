import math
angulo = float(input('Digite o ângulo: '))
radianos = math.radians(angulo)
print('Seno do ângulo = {:.2f}\nCosseno do ângulo = {:.2f}\nTangente do ângulo = {:.2f}'.format(math.sin(radianos),math.cos(radianos),math.tan(radianos)))