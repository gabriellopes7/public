import seaborn as sns 
import matplotlib.pyplot as plt 

iris = sns.load_dataset('iris') #dataset de iris de flores
print(iris.head())

#pairgrid -> permite criar gráficos mais customizados, mas precisa de maior conhecimento
#de criação

g = sns.PairGrid(iris)
plt.show()
#popula cada região com funções

#sintaxes
g = sns.PairGrid(iris) #-> cria o grid de gráficos baseado no cruzamento de informações do dataset
g.map_diag(plt.hist) #cria um histograma na diagonal do grid
g.map_upper(plt.scatter) #criar um scatter para os gráficos de cima
g.map_lower(sns.kdeplot) #criar um kdeplot nos gráficos inferiores do grid
plt.show()

#o pairplot é um pairgrid criado de maneira padronizada
sns.pairplot(iris, hue='species')
plt.show()

#sns.FacetGrid() -> maneira geral de criar plots que trabalham com dados categóricos
tips = sns.load_dataset('tips')
g=sns.FacetGrid(tips, col='time',row='smoker') #está para os outros métodos de plot assim como pair plot está para pairgrid
#tem que passar dados categóricos
g.map(plt.hist,'total_bill') #seleciona o tipo de gráfico que vc quer gerar e o dado numérico referente
plt.show()
