valores = []
valores.append(5)
valores.append(9)
valores.append(4)
print(valores)
for valor in valores:
    print(f'{valor}...',end='')
print('')
for p,v in enumerate(valores):
    print(f'posição {p} valor = {v}')

#inserir valores automaticamente
lista =[]
for c in range(0,10):
    lista.append(c)
print(lista)

a = [1,2,3,4,5]
b = a #quando se faz assim, as listas ficam interligadas, a alteração em uma, influi diretamente na outra
print(a)
print(b)
b[2] = 8
print(a)
print(b)
#para criar cópia
b = a[:] #criando cópia
b.append(9)
print(a)
print(b)