# ROSSMANN SALES PREDICTION 

![image](https://user-images.githubusercontent.com/104724574/168178979-0d9d19c1-e824-4364-a10c-835811b47f15.png)


## Contexto de negócio
Dirk Rossmann GmbH é uma das maiores redes de drogarias da Europa, possuindo mais de 4000 drogarias espalhadas em 9 países. Com o intuito de promover uma remodelagem no layout das lojas da rede, o CFO da Rossmann deu a tarefa de prever 6 semanas de fluxo de vendas diários aos gerentes de cada loja a fim de utilizar parte dessa receita no orçamento das reformas. As vendas da loja são influenciadas por muitos fatores como a duração de promoções, distância dos competidores e feriados escolares.

## Dados
O conjunto de dados utilizado nesse projeto estão disponíveis na plataforma do Kaggle no endereço: https://www.kaggle.com/c/rossmann-store-sales/data. O dataset possui os seguintes atributos:

O DataSet possui as seguintes informações.


**Store** - numero de identificação (ID) unico de cada estabelecimento

**Sales** - o volume vendas na data específica.

**Customers** - volume de clientes em um determinado dia

**Open** - um indicador para saber se a loja estava aberta (1) ou fechada (0)

**StateHoliday** - indica um feriado estadual. Normalmente todas as lojas, com poucas exceções, fecham nos feriados estaduais. Observe que todas as escolas fecham nos feriados e finais de semana. a = feriado, b = feriado da Páscoa, c = Natal, 0 = Nenhum

**SchoolHoliday** - indica se (Loja, Data) foi afetado pelo fechamento de escolas públicas

**StoreType** - diferença entre 4 modelos de loja diferentes: a, b, c, d

**Assortment** - descreve um nível de sortimento: a = básico, b = extra, c = estendido

**CompetitionDistance** - distância em metros até a loja concorrente mais próxima

**CompetitionOpenSince[Month/Year]** - o ano e mês aproximados em que o concorrente mais próximo foi aberto

**Promo** - indica se uma loja está fazendo uma promoção naquele dia

**Promo2** - Promo2 é uma promoção contínua e consecutiva para algumas lojas: 0 = a loja não está participando, 1 = a loja está participando

**Promo2Since[Year/Week]** - descreve o ano e a semana em que a loja começou a participar da Promo2

**PromoInterval** - descreve os intervalos consecutivos de início da promoção 2, nomeando os meses em que a promoção é iniciada novamente. Por exemplo. "Fev, maio, agosto, novembro" significa que cada rodada começa em fevereiro, maio, agosto, novembro de qualquer ano para aquela loja

## Planejamento da solução baseado na metodologia CRISP

1. **Entendimento do negócio*** - Busca entender de forma mais profunda o real problema do negócio e definir os objetivos para a resolução do negócio. Neste caso especifico, foi decidido que o objetivo será a realização de um modelo de machine learning para a predição das vendas como as métricas afetam o fluxo de vendas e consequentemente a predição. Além disto, também foi definida hipoteses iniciais que deverão ser validadas através da exploração de dados.

2. **Coleta de dados** - Acesso a plataforma do Kaggle para download dos arquivos que serão usados.

3.**Limpeza dos dados** - Os dados são rigorosamente analisados para se verificar dados nulos (NA), outliers, transformação de tipo de variável e qualquer outra irregularidade visando assim criar um dataset mais coeso para a análise na próxima etapa.

4. **Exploração dos dados** - Nessa etapa os dados são analisados de forma isolada (univariada) e em conjunto (valoradas) buscando achar as variáveis que melhor se relacionam e causam maior impacto nas vendas. O uso de bibliotecas de Python que criam gráficos, como a Seaborn, auxilia na criação de um maior conhecimento e entendimento do comportamento dos dados. Nessa parte as hipoteses inicias tambem sao analisadas e ao somar o resultado de tal processo e o da analise das relaçoes das variaveis se é possivel gerar insights que axuliaram tanto nas seguintes etapas do projeto quanto para dar uma nova perspectiva da empresa para o time de negocios.  

5. **Preparação dos dados** - Visa transformar, balancear e regularizar os dados a fim de que incoerências não interfiram no resultado dos algoritmos de machine learning. 

6. **Aplicação dos algoritmos de machine learning** . Com o auxílio da cross validation, os melhores modelos de machine learning foram selecionados, treinados e testados com partes diferentes do dataset. Nesta etapa foram escolhidos os algoritmos de machine learning que seriam usados e então os mesmos foram treinados com os dados. 

7. **Avaliação do algoritmo** - Apos a selecao do melhor mdoelo foi utilizado a tecnica de Fine Tuning de Random Parameters para a selȩao dos melhores parametros visando aumentar a qualidade dos resultados do algoritmo.

8. **Tradução do erro em métricas de negócio** - Nessa etapa é quando a magia acontece, nesse momento os resultados do mdoelo sao convertidos em metricas de negocio para se tornar facilmente entendivel o impacto financeiro que tal iomplementação gerará

9. **Deploy do modelo em produção** - O modelo foi colocado em produção no ambiente cloud Heroku para que as predições possam ser utilizadas através de requisições a uma API e possa ser facilmente acessado via bot do Telegram.

## MELHORES INSIGHTS

1. Lojas com maior sortimento vendem mais

**Verdadeiro**, quanto maior for o sortimento da loja, maior é o número de vendas

![image](https://user-images.githubusercontent.com/104724574/168179775-28fde4ef-69d0-4f4b-b0de-a380bb518c9a.png)


2. Lojas com competidores mais próximos deveriam vender menos.

**Falso**, lojas com competidores nas proximidades tendem a vender mais

![image](https://user-images.githubusercontent.com/104724574/168181284-511ea1b6-b639-40ef-bcd2-a48766689190.png)

3. Lojas com promoções ativas por mais tempo vendem menos, depois de um certo periodo de promoção

**Falso**, lojas com promoções ativas a mais tempo vendem menos depois de certo período de tempo

![image](https://user-images.githubusercontent.com/104724574/168181165-766b0c05-d498-43ea-b788-bffb91011ef5.png)


4. Lojas deveriam vender mais ao longo dos anos.

**Falso**, o fluxo de vendas anuais estão em constante caimento

![image](https://user-images.githubusercontent.com/104724574/168180602-1b8ab372-a741-4650-81ef-8e8e16c91bc5.png)


##### OBS: Quando tal dataset foi publicado os dados de 2015 ainda não estavam fechado, entretanto é perceptivel a decaděcia do volume de vendas.

##Machine learning Models

Algoritmos utilizados para a predição foram:
 • Modelo e média 
 • Linear Regression
 • Linear Regression Regularized (Lasso)
 • Random Forest Regressor
 • XGBoost Regressor
 
 • MAE (Mean Absolute error) - Mostra o erro médio absoluto do modelo, tanto para mais quanto para menos.
 • MAPE (Mean Absolute percentage error) - Erro médio absoluto em percentual.
 • RMSE (Root mean squared error) - Erro médio absoluto quadrado, erro médio absoluto elevado ao quadrado. Não é a melhor métrica para uma análise de negócios, porém é muito util para avaliar a performance do modelo em si.
 
 ![image](https://user-images.githubusercontent.com/104724574/168181789-b3dfbf25-09e5-4846-8a4e-16e067a44a37.png)
 
 Após a aplicação do Cross Validation e Fine Tuning optei por usar o XGBoost como modelo base visto que era uma modelo mais leve e rápido em compração com o de Random Forest 

![image](https://user-images.githubusercontent.com/104724574/168182276-b8d2d989-bb04-4f74-9af6-23d765d9d8d6.png)

## Resultados
Apòs a tradução da performance do algoritmo de machine learning foi possivel demonstrar de maneira facil de se absorver qual seria o arrecadamento de cada loja no período estipulado

![image](https://user-images.githubusercontent.com/104724574/168182378-403c5159-bd52-4b5a-8f4b-6697f1ffd8e4.png)

## Modelo em produção
 
  •  A API foi hospedada na Cloud Heroku e pode ser acessada aprtir deste url: https://rossmann--sales--prediction.herokuapp.com/rossmann/predict
  
  • O bot Telegram esta disponivel atraves deste link: t.me/rossmann_week_prediction_bot
    Para a consulta individual e rápida de alguma predição, basta entrar em contato com o Bot pelo link acima e digitar o número da loja
    
 ![image](https://user-images.githubusercontent.com/104724574/168182928-58c7abf1-8f3e-4bb9-8699-b134f8604187.png)

 
 ## Conclusão
 
 Com o resultado deste projeto tivemos uma performance satisfatoria visto que o modelo, mesmo sendo simples, apresentou um baixo erro (em comparação com a grandeza de valores do fluxo de vendas).
 
 
 
