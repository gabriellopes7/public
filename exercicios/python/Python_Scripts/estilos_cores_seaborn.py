import seaborn as sns
import matplotlib.pyplot as plt 

tips = sns.load_dataset('tips')



sns.set_style('ticks') # estilos de grid(grade)-> darkgrid, whitegrid, dark, white, ticks
sns.despine() #retira as bordas externas do gráfico, por padrão retira topo e direita, mas pode-se
#retirá-las, usando left=,bottom=
plt.figure(figsize=(12,8)) #altera o tamanho da figura
sns.countplot(x='sex',data=tips)
plt.show()


sns.lmplot(x='total_bill',y='tip',data=tips,size=2,aspect=4)#alterando tamanho da figura em lmplot
plt.show()

#deixa tamanho de gráfico préconfigurados
sns.set_context('poster') #poster->aumenta o plot
#font_scale -> altera o tamanho da fonte
sns.lmplot(x='total_bill',y='tip',data=tips)
plt.show()
#palette -> altera as cores dos dados
#google -> matplotlib colormap -> mostra todas as paletas de cores disponíveis para os gráficos
sns.lmplot(x='total_bill',y='tip',data=tips,hue='sex',palette='inferno') #deve ter um hue 
plt.show()