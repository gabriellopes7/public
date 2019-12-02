a = float(input('Digite a altura da parede: '))
l = float(input('Digite a largura da parede: '))
area = a*l
print('A área da parede é de {:.2f} m² e são necessários {:.2f} litros de tinta para pintá-la'.format(area,area/2))