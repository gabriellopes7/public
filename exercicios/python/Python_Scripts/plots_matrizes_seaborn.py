import seaborn as sns
import matplotlib.pyplot as plt 
flights = sns.load_dataset('flights') #informações de voos de uma companhia aerea ao longo dos anos
tips=sns.load_dataset('tips') #gorjetas

print(flights.head())
print(tips.head())

print(tips.corr()) #calcula todas as relações de todas as variáveis do conjunto de dados
#valores numéricos
corr = tips.corr()

#heatmap -> mapa de calor
sns.heatmap(corr,cmap='coolwarm',annot=True) #annot -> mostra os valores, cmap-> paleta de cores
plt.show()

print(flights.pivot_table(values='passengers',index='month',columns='year'))
ptFlights = flights.pivot_table(values='passengers',index='month',columns='year')
#remodelo a matriz da tabela para usar meses como indice, ano como coluna e valores de passageiros

sns.heatmap(ptFlights,cmap='YlGnBu') #da para se retirar bastante informações
plt.show()
#linewidths e linecolor para segmentar os dados
sns.heatmap(ptFlights,cmap='YlGnBu',linecolor='white',linewidth='1')
plt.show()

#clustermap->agrupa os dados
sns.clustermap(ptFlights,cmap='YlGnBu')
plt.show()
#a ideia é conseguir ver os padrões destes dados
#colocando escala de 0 a 1, padrão de machine learning
sns.clustermap(ptFlights,cmap='YlGnBu',standard_scale=1) #fica mais fácil ver os clusters
plt.show()
