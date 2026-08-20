# [Engajamento por hashtag na coleta de makeup]

## Pergunta

> A taxa de engajamento de um post é influenciada pelas hashtags que foram utilizadas nele?

## Dados

**Fonte:** exportação do TikTok via Zeeschuimer, Aula 7

**Período coletado:** 19/08/2026

**Tamanho da amostra:** 1138

**Limites conhecidos da coleta:** 
As hashtags comparadas foram extraídas em quantidades diferentes (ex: fy - 51 posts, girls - 15 posts) e rankeadas conforme engajamento médio. Isso gera uma possibilidade de enviezar o resultado visto que uma delas apresenta uma quantidade de posts muito menor, aumentando a chance de obter um post que suba muito a média do engajamento, mesmo que todos os outros posts daquela mesma hashtag tenham métricas parecidas. Resumindo, quanto menor a quantidade de posts de uma hashtag, mais chance de obter um resultado que "só está ali" por conta de uma publicação que aumentou muito o engajamento médio.


## Método

> Foi calculado o engajamento médio dos posts a partir das hashtags. Foram removidas linhas duplicadas (nenhuma encontrada) e posts com `plays` igual a zero (nenhum descartado nesta coleta). Taxa de engajamento calculada como `(likes + comments + shares) / plays` por post, depois agrupada por hashtags com 10 ou mais posts (uma hashtags por post, coluna `hashtags` separada por vírgula) com a média da taxa de engajamento de cada grupo.

## Achados

> 1. A hashtag com mais de 10 posts que possui maior engajamento médio é a "girls", com um engajamento médio de 0.08991679124179573. Referência (`dados/resumo_hashtags.csv`).
> 2. A hashtag com maior engajamento médio, sem precisar ter 10 posts ou mais é a "beatrizrizzato", com engajamento médio de 0.284283. Referência (`dados/resumo_hashtags_2.csv`).
> 3. A hashtag com mais de 10 posts com maior curtidas médias, nesse caso "lipcombo", não é a mesma que a com maior engajamento médio, nesse caso "girls". Referência (`dados/resumo_hashtags.csv`).

## Limitações

> Os dados gerados na tabela (`dados/resumo_hashtags_2.csv`) consideram hahstags que possuíram apenas 1 post e um engajmeno médio muito alto, ou seja, não é garantido que ao utilizar essa mesma hashtag em outro post ela terá um engajamento médio tão alto, pois pode ter sido uma questão de sorte.
> Não é possível concluir se uma hashtag está ocupando um lugar no ranking de enjamento médio por conta de apenas um post que aumentou ou desceu muito a sua colocação, ou se realmente todos os posts daquela hashtag possuem uma mesma média.

## Recomendações

> O ideial seria utilizar uma maior e mesma quantidade de posts para cada hashtag antes de comparar o engajamento médio entre elas. Desse modo, a comparação seria mais "justa", visto que com coletas maiores a possibilidade de um engajemnto medio ser enviezado por apenas um post diminui - Depende dos achados 1 e 2.
> Seria ideal realizar um filtro que remova posts considerados "outliers", ou seja, que fogem muito do padrão de engajamento daquela hashtag. - Depende dos achados 1 e 2.

## Revisão por pares

**Revisado por:** 

**Comentários recebidos:**

>

**O que mudou no relatório por causa da revisão (ou por que nada mudou):**

> 


## Declaração de uso de IA

> Não usei IA nesta entrega.
