#Machine Learning
#Método de análise de dados que automatiza o processo de criação de modelos
#Usando algoritmos que iterativamente aprendem com os dados, Machine Learning
#permite que computadores encontrem padrões escondidos nos dados sem terem sido programados
#para isso
#Machine learning é uma das bases da inteligência artificial
#Para que é usado?
#Detecção de fraudes
#Pesquisas na web
#Anuncios automáticos na internet
#Predição de falhas em equipamentos
#Modelos de precificação de ativos financeiros
#Detecção de invasores em redes
#Sistemas de recomendação (Netflix, spotify)
#Segmentação de clientes
#Análise de sentimentos em textos
#Reconhecimento de padrões em imagens
#Filtros de spams em emails
#Organograma
#                                         Dados de teste \/
#Aquisição dos dados <-> Limpeza dos dados /\         \/  Teste do modelo  -> Uso prático
#                            /\ Dados de treinamento e construção do modelo

#3 tipos de Machine Learning

#Supervised Learning -> Se tem parâmetros rotulados que são usados para
#construir o modelo e tentar predizer os demais rótulos, baseados nos parâmetros apenas
#Ex: você tem características técnicas de peças e equipamentos que falharam "F"
#e não falharam "NF" e quer predizer o comportamento das demais peças
#O algoritmo de aprendizado recebe entradas com as saídas corretas e ajusta o seu modelo
#de forma iterativa para que o mesmo se adapte as condições apresentadas no conjunto de dados
#de treino, então o algoritmo irá conferir a precisão do modelo criado usando o conjunto
#de dados de teste


#Unsupervised Learning -> Você possui apenas os parâmetros, sem rótulos (saídas)
#e quer encontrar subgrupos dentro dos dados que possuam algum tipo de semelhança
#É usado quando os dados não tem um classificação prévia
#A resposta não é dita ao algoritmo, cabendo a ele encontrar padrões nos dados e agrupá-los/classificá-los
#baseando nas similaridades no conjunto de parâmetros.
#Técnicas populares: k-means clustering, singular value decomposition -> mapas organizáveis
#Também são utilizados para segmentar textos em tópicos, identificar outliers em conjuntos de dados
#e recomendação de itens à clientes


#Reinforcement Learning-> Algoritmos que aprendem a executar ações baseados em experiências do mesmo
#com algum meio. Usado para robótica, jogos e navegação.
#O algoritmo aprende através de tentativa e erro, apresenta para ele uma série de estados e ele
#vai interagindo com o meio até encontrar a melhor atitude em cada situação.
#O objetivo do agente é escolher ações que maximizem a recompensa esperada dada uma determinada 
#quantidade de tempo
#O agente dessa forma irá criar uma política de decisões, baseado no seu estado atual