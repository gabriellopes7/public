import seaborn as sns 
import matplotlib.pyplot as plt 

sns.set_style('whitegrid')
titanic = sns.load_dataset('titanic')
print(titanic.info())

sns.jointplot(x='fare',y='age',data=titanic) #fare -> tarifa
plt.show()

sns.distplot(titanic['fare'],kde=False,bins=30,color='red')
plt.show()

sns.boxplot(x='class',y='age',data=titanic,palette='rainbow')
plt.show()

sns.swarmplot(x='class',y='age',data=titanic,palette='Set2')
plt.show()

sns.countplot(x='sex',data=titanic)
plt.show()

corr = titanic.corr()
sns.heatmap(corr,cmap='coolwarm')
plt.title('titanic correlations')
plt.show()

g = sns.FacetGrid(data=titanic, col='sex')
g.map(plt.hist, 'age')
plt.show()