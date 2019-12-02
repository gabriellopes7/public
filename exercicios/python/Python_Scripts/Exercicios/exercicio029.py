v = int(input('Velocidade do carro: '))
if v>80:
    print('Multado !')
    m = (v-80)*7
    print('Sua multa vai custar: {:.2f} reais'.format(m))

