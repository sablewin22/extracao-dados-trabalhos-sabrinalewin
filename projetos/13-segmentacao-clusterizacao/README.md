README do case

**Fonte, período e tamanho da coleta:**

> Fonte: Exportação do TikTok via Zeeschuimer, Aula 7. Período: 19/08/2026. Tamanho da coleta: 1138 posts.

**As duas variáveis que você criou (a contínua da Parte A e o rótulo da Parte B), com a fórmula/critério de cada uma:**

> A variável contínua criada na Parte A foi a taxa de engajamento, a partir da fórmula ( df["likes"] + df["comments"] + df["shares"] )/ df["plays"]. O rótulo da Parte B foi o corte no percentil 75 de plays, ou seja, posts com 688,375 plays. Posts que tiveram mais visualizações que isso foram classificados como virais (285 de 1138 da coleta, 25%).

**As features usadas nas Partes A e B, e quais colunas você descartou por vazamento:**

> Features usadas na Parte A e B foram: 'seguidores_autor', 'videos_autor', 'tam_legenda', 'n_emojis', 'n_hashtags', 'hora', 'dia_semana'. Foram descartadas as colunas "likes", "comments", "shares" e "plays", pois elas são diretamente utilizadas para fazer o cálculo do engajamento médio (Parte A) e do rótulo de viralização (Parte B), ou seja, utilizar elas seria apenas informar as métricas exatas para calcular as respostas desejadas, isto é, não estaria sendo feita nenhuma previsão.


**Parte A — resultado:** MAE e R² do modelo bobo, da linear e da árvore. O seu melhor modelo bateu o bobo?

> Modelo bobo:  MAE = 0.0324   R2 = -0.000 / Regressão linear:   MAE = 0.0330   R2 = -0.007 / Árvore (prof. 5):   MAE = 0.0323   R2 = -0.295. Neste caso, o melhor MAE alcançado foi o da Árvore, com uma diferença de 0.0001 (muito pequena) para o modelo bobo. Já no R2, o melhor continuou sendo o do modelo bobo, visto que o dos algoritmos testados deu um resultado negativo mais alto.

**Parte B — resultado:** a matriz de confusão e uma leitura: a favor de quem o modelo erra?

> A matriz de confusão da regressão logística fica assim: VN = 211 / FN = 61 / FP = 3 / VP = 10. Ele está errando a favor dos falsos negativos, ou seja, existem 61 posts que deveriam ser classificados como virais, mas não estão sendo. Também foi analisado o resultado da árvore de decisões, que fica assim: VN = 168 / FN = 28 / FP = 46 / VP = 43. Este modelo está errando a favor dos falsos positivos, ou seja, está falando que existem posts que são virais, quando na verdade não são. É possível comparar esta diferenciação dos resultados nos modelos por meio da precisão e do recall. O recall da regressão logística estava mais baixo (0,14), isto é, selecionando poucos posts que realmente viralizaram, classificando muitos dos que eram para serem virais como não virais, e a precisão estava alta (0,77), ou seja, dos posts que ele estava selecionando como "viral", a maioria ele acertava, mas isso acontecia justamente por conta do recall baixo ao ser muito seletivo no que chamava de viral. Já na árvore de decisões, o recall está mais alto (0,61), mostrando que o modelo está selecionando mais posts como virais, porém isso afeta diretamente a precisão, que fica mais baixa (0.48), isso acontece pois ao selecionar mais posts como viras, a chance de acertar a classificação diminui, abaixando a precisão, por ser um modelo menos seletivo.

**Parte C — resultado:** quantos segmentos, como você escolheu `k`, e a descrição de cada segmento (uma frase com número).

> Foram escolhidos 2 segmentos. Foi escolhido k = 2, pois foram feitos gráficos de silhueta e cotovelo, e a partir deles pode-se concluir que o maior valor de K foi o igual a 2 (0.534), mostrando que dividir em dois segmentos seria a melhor escolha a ser feita. Além disso, por ser uma coleta pequena, dividir ela em 2 seria mais consciente do que dividir em 3 (por mais que esse seja o melhor cotovelo), visto que os dados possuem pouca variabilidade. No segmento 0, estão inseridos 616 posts, com uma média de likes de 416.3, média de comentários de 7.4, média de compartilhamentos de 38.4 e média de plays de 33482.1. Já no segmento 1, estão inseridos 522 posts, com uma média de likes de 207348.5, média de comentários de 1304.5, média de compartilhamentos de 9187.3 e média de plays de 3574317.2. Dito isso, é possível observar que o segmento 0 agrupa os posts com métricas menores, enquanto o segmento 1, agrupa posts com métricas maiores

**Uma conclusão que os seus dados sustentam** (sem extrapolar para além da sua coleta):

> Ao utilizar as features ['seguidores_autor', 'videos_autor', 'tam_legenda', 'n_emojis', 'n_hashtags', 'hora', 'dia_semana'] e corte no percentil 75 para classificar os posts da minha coleta como virais ou não, é possível concluir que usar o modelo de regressão logística garante menos falsos positivos, ou seja, ele irá acertar mais ao classificar um post como viral (precisão alta, 0.77), porém isso tem um custo, que nesse caso seria o recall baixo (0.14), ou seja, ele tende a acertar quando classifica um post como viral, porém também deixa passar muitos posts que deveriam estar sendo classificados como virais, gerando muitos falsos negativos.

> No modelo da árvore de decisões, é possível observar que ele garante mais falsos positivos. Isso ocorre pois o recall dele está mais alto (0.61), ou seja, está selecionando mais posts como virais, ocasionando um modelo menos seletivo, o que afeta diretamente a precisão, que fica mais baixa (0.48), justamente por conta das chances maiores de errar ao classificar um post como viral. Mesmo assim, ele tende a ser um modeo que promove uma menor quantidade de falsos negativos, pois a maioria dos posts que são virais estão sendo classificados como tais.

> Dito isso, entende-se que cada modelo deve ser utilizado para um objetivo específico. Se o objetivo era ter certeza ao classificar um post como viral, a melhor opção é a regressão logística, pois por ser um modelo mais seletivo (recall baixo), ela tende a achar menos falsos positivos. Agora, se o objetivo era classificar a maior quantidade possível de posts virais, o ideal seria utilizar um modelo com recall mais alto, nesse caso, a árvore de decisões, que garante que mais posts virais estarão sendo classificados dessa forma, gerando menos falsos negativos. 


**Revisão por pares:** nome do colega **da turma** que revisou, o que ele apontou, e o que você mudou (ou por que não mudou).

> O trabalho está perfeito. Mas é sugerível coletar uma amostra maior visto que o modelo bobo superou o R2.

**Declaração de uso de IA:** 

> Foi utilizado Claude IA na quinta célula da Parte C. Ele foi utilizado pois foi percebido que os 2 segmentos gerados estavam com uma divisão extremamente desequilibrada, muitos posts em um segmento e pouquíssimos em outro (deixei os códigos no notebook para comprovar - é a segunda, terceira e quarta célula da Parte C - vale ressaltar que mesmo aumentando o número de K, o resultado segue desbalanceado). Desse modo, pensei que o modelo poderia estar classificando dessa forma, pois achou que o(os) segmento(os) com poucos posts era(m) destinado(os) a outliers. Assim, achei melhor usar a escala log por conta da grande distância de valores nas variáveis da coleta, mas para isso precisei utilizar IA, visto que não sabia como gerar o código necessário.