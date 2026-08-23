# [Engajamento por hashtag na coleta de makeup]

## Pergunta

> A quantidade de posts de uma hashtag influencia na taxa de engajamento média dela?

## Dados

**Fonte:** exportação do TikTok via Zeeschuimer, Aula 7

**Período coletado:** 19/08/2026

**Tamanho da amostra:** 1138

**Limites conhecidos da coleta:** Foram feitas duas tabelas distintas para realizar os gráficos. A primeira delas considera as 10 hashtags que possuem maior engajemento médio sem considerar a quantidade de posts, já a segunda tabela considera as 10 hahstags que possuem 10 ou mais posts. Desse modo, existem hashtags que poderiam ser úteis para responder a pergunta, mas estão sendo desconsideradas pois não alcançam o mesmo engajemnto médio das que estão no top 10 geral, ou não possuem 10 posts ou mais, não entrando na tabela mesmo tendo um engajamento médio maior.


## Método

> Foi calculado o engajamento médio das hashtags pela quantidades de posts que a hashtag tinha. Foram removidas linhas duplicadas (nenhuma encontrada) e posts com `plays` igual a zero (nenhum descartado nesta coleta). Taxa de engajamento calculada como `(likes + comments + shares) / plays` por post, depois, na tabela "resumo_hashtags_10_posts" agrupada por hashtags com 10 ou mais posts (uma hashtags por post, coluna `hashtags` separada por vírgula) com a média da taxa de engajamento de cada grupo e na tabela "resumo_hashtags" agrupada apenas pelas hashtags sem considerar uma quantidade mínima de posts.

## Achados

> 1. A hashtag com mais de 10 posts que possui maior engajamento médio é a "girls", com um engajamento médio de 0.08991679124179573. Referência (`dados/resumo_hashtags_10_posts.csv`).
> 2. A hashtag com maior engajamento médio, sem precisar ter 10 posts ou mais é a "beatrizrizzato", com engajamento médio de 0.284283. Referência (`dados/resumo_hashtags.csv`).
> 3. A quantidade de posts de uma hashtag não influencia no engajamento médio dela. Referência (`dados/resumo_hashtags.csv` e `dados/resumo_hashtags_10_posts.csv`).
> 4. Hashtags que possuem apenas um post geraram um engajemnto médio muito maior do que hashtags com 10 ou mais posts. Referência (`dados/resumo_hashtags.csv` e `dados/resumo_hashtags_10_posts.csv`).



## Limitações

> A tabela (`dados/resumo_hashtags.csv`) possui hahstags com apenas 1 post e um engajmeno médio muito alto. Dessa forma, esses resultado pode estar relacionado ao acaso, não sendo possível afirmar que ao utlizar essas hashtags, gerará o mesmo engajamento médio.
> Na tabela `dados/resumo_hashtags_10_posts.csv` não é possível concluir se uma hashtag está ocupando um lugar no ranking de enjamento médio por conta de apenas um post que aumentou ou desceu muito a sua colocação, ou se realmente todos os posts daquela hashtag possuem uma mesma média.

## Recomendações

> O ideial seria utilizar uma maior e mesma quantidade de posts para cada hashtag antes de comparar o engajamento médio entre elas. Desse modo, a comparação seria mais "justa", visto que com coletas maiores a possibilidade de um engajemnto medio ser enviezado por apenas um post diminui - Depende dos achados 3 e 4.
> Seria ideal realizar um filtro que remova posts considerados outliers no engajamento médio, ou seja, que estão muito além ou muito abaixo do engajamento "padrão" daquela hashtag. - Depende dos achados 3 e 4.

## Revisão por pares

**Revisado por:** 

**Comentários recebidos:**

>

**O que mudou no relatório por causa da revisão (ou por que nada mudou):**

> 

## Declaração de uso de IA

> Não usei IA nesta entrega.
