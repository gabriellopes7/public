teste = list()
teste.append('Gustavo')
teste.append(40)
galera =[]
galera.append(teste)
print(teste)
print(galera)
teste[0] = 'Maria'
teste[1] = 32
print(galera) #a lista galera fica vinculada a lista teste, qualquer alteração em teste causa uma alteração em galera
galera.append(teste)
print(galera)

pessoas = [['Joao',19],['Maria',15],['Pedro',32],['Ana',22]]
print(pessoas)
print(pessoas[3][0])