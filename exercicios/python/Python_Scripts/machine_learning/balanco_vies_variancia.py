#Balanco vies variância
#Tópico fundamental para entender a performance do seu modelo
#Ele basicamente leva em conta a relação entre a complexidade do modelo
#e quanto erro ele é capaz de gerar nos grupos de dados de teste e de treino
#capítulo 2 do livro
#O balanço viés-variância é quem determina o ponto em que estamos
#apenas adicionando ruído ao nosso modelo a medida que adicionamos complexidade para ele
#O erro nos dados de treino começa a cair a medida em que o erro nos dados de teste aumenta
#Efeito OVERFITTING
#A variância mede a amplitude dos erros do modelo
#O modelo ganha viés a medida que a média das prediçoes se afasta do valor correto
#O mesmo tambem ganha variância quanto mais diferentes forem as tentativas entre si
#IDEAL é baixo viés e baixa variância

#Uma tentação comum dos iniciantes é continuamente adicionar complexidade aos modelos 
#para que os mesmo se ajustem perfeitamente aos dados de treino
#Ao fazer isso, estamos overfittando o nosso modelo, fazendo com que o mesmo não consiga captar
#o comportamento geral do conjunto de dados, apenas se adequando ao grupo de treino
#Assim, quando se apresentar novos dados de teste, o modelo terá um erro maior