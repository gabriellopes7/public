#Livro basico, Introduction to Statistical Learning
#Livro gratuito e online
#Statistical learning refere-se a uma gama de ferramentaas para
#entender dados
#Essas ferramentas são classificadas como supervisionadas e não supervisionadas
#Aprendizagem estatística supervisionada -> criar um modelo estatístico
#para prever, ou estimar, um output baseado em um ou mais inputs
#Aprendizagem não supervisionada -> há inputs mas não há um output supervisionado
#mesmo assim podemos aprender as relações e estruturas destes dados
#n representa o numero de pontos de dadas, ou observações.
#p representará o número de variáveis disponíveis para usar em fazer predições
#exemplo -> temos 12 variáveis caracterizando 3000 pessoas
#n=3000
#p=12
#i representará n, j representará p
#exemplo anterior: i: 1,2,3,...,3000(n)
#p: 1,2,3,...,12(p)
#X será a variável de input -> preditor, variavel independente, features
#Y a variável de output -> resposta ou variável dependente
#f -> formula que determina o comportamento de X em relação a Y
#f é uma estimativa -> por que estimar ? para predição e inferência
#Yˆ = ˆf(X)
#a predição de f pode ser bem precisa, mas não 100% certo, 
#sendo chamado de erro redutível
#o erro padrão, é erro irredutível e sempre irá existir
#há ótimas técnicas para estimar o f, e reduzir o erro redutível
#Inferência -> trata-se de supor os efeitos de uma determinada alteração
#ex: qual o efeito nas vendas de mudar o preço de venda de determinado um produto ?
#há dois tipos de metodos estimar o f
#parametricos e não-parametricos

#parametricos ->
#PRIMEIRO faz uma suposição de como f se comporta em relação ao X, ex: modelo linear
#modelo linear: assume que f é linear, então f(x) = B + B1*x1 + B2*x2...
#SEGUNDO ter um processo que use a data de treinamento para treinar o modelo ex: ordinary least squares

#não paramétricos:
#Não faz suposições de f, ele faz uma estimativa de f baseado nos pontos dos dados
#de forma que não fique grosseira
#porém há uma gigantesca desvantagem,
#apesar de ter uma precisão melhor na estimativa de f, ele precisa de um número bem maior de 
#observações para se ter uma estimativa de f confiável.
#tomar cuidado com o overfitting, que é o caso de se criar uma placa de precisão
#muito perfeita que se encaixa perfeitamente nos pontos de dados de treinamento, 
# não é um resultado desejado pois não irá produzir estimativas precisas 
#nas novas observações que não se encaixarem nos dados de treinamento
#importante escolher bem o grau de suavidade (smoothness)

#regressão linear é uma abordagem não flexivel pois somente gera funções lineares
#thin plates splines são mais flexiveis pois pode gerar muitas outros formatos de estimativas para f

#aprendizado supervisionado e não supervisionado

#não supervisionado
#no aprendizado nao supervisionado não é possivel faz regressão linear
#pois não se terá histórico de respostas para traçar um f relacionado as variáveis
#que traga uma correlação linear entre elas.
#clustering é uma ferramenta estatística excelente do aprendizado não supervisionado
#a segmentação de indivíduos, como exemplo estilos de personas de mercado,
#através de seus padrões

#há dois tipos de variáveis, quantitativas e qualitativas (ou categorias)
#problemas com variáveis quantitativas são chamados de regression problems
#com variáveis qualitativas de classification problems
#linear regression é usada para regression problemas
#logical regression usada para classification problemas (duas classes ou binários)
#há metodos estatísticos que podem ser usados para os dois, como K-nearest neighbors
#e boosting

#escolher o melhor método é importante para determinar a precisão de suas predições

#Medindo o quality fit
#Mean squared error (MSE) -> o MSE será pequeno se as respostas previstas estiverem perto da verdade
#selecionar o método que tiver a menor média de testes MSE
#nem sempre o método mais flexivel terá os melhores resultados em Training MSE e e test MSE
#metodo de estimar o test MSE é usando o cross-validation usando o training data
#MSE nunca pode estar abaixo do Var(erro irredutível)

#Variance(variância) e bias(viés)
#variância diz respeito ao tanto que o f mudaria caso mudasse o training data set.
#bias diz respeito ao erro que é introduzido ao aproximar um problema da vida real
#exemplo: assumir que duas variáveis tem relação linear, a estimativa de f terá um viés,
#geralmente, métodos não lineares, mais flexiveis resultam em viés menor
#mas assim como métodos mais flexíveis também aumentam a variância
#importante encontrar o ponto ótimo entre as variáveis bias, var e MSE -> bias-variance trade-off
