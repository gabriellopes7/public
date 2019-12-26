import seaborn as sns
import matplotlib.pyplot as plt 


tips = sns.load_dataset('tips')
print(tips.head())

#plot de regressão
#regressao entre total da conta e tip
sns.lmplot(x='total_bill',y='tip',data=tips)
plt.show()
#area sombreada mostra onde a variação de dados é maior

#pode-se utilizar o hue, separando os dados por sexo
#alterando o tipo de marcador para melhorar a visualização de dados
#markers
sns.lmplot(x='total_bill',y='tip',data=tips,hue='sex',markers=['o','v']) #o -> bolinha, v -> triangulo
plt.show()

#parametro que permite alterar o gráfico, através de dicionario do scatter plot
sns.lmplot(x='total_bill',y='tip',data=tips,hue='sex',markers=['o','v'],scatter_kws={'s':100}) 
#s -> size, aumenta o tamanho dos marcadoress
plt.show()

#para dividir o filtro sexo em 2 gráficos -> col='sex'
sns.lmplot(x='total_bill',y='tip',data=tips,hue='sex',col='sex')
plt.show()
#segregando em mais informações -> row=''
sns.lmplot(x='total_bill',y='tip',data=tips,hue='sex',col='sex',row='time')
plt.show()

#aspect e size -> alteram os formatos dos gráficos em dimensões



