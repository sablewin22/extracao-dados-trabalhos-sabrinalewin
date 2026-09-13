# Correção do exercício 5, Prof. Matheus

Oi, Sabrina! LEMBRETE: Esse exercício não valia ponto! Tô corrigindo pq você pediu! (só um detalhe: esse notebook é a base do fluxo métricas → exploração → hashtags que depois vira o Projeto 2, consolidado na Aula 7, então vale revisar com carinho porque os problemas daqui podem se arrastar pra lá.)

Resumo geral: a parte técnica (carregar, inspecionar, calcular taxa de engajamento, comparar média e mediana, agrupar por hashtag) está sólida, mas a Parte 6, que responde a sua pergunta, tem um bug de conta e um furo de método que comprometem a conclusão.

## O que ficou bom

- Na célula que confere valores ausentes: você foi além do pedido e checou não só nas quatro métricas, mas também em `hashtags`, `effects` e `warning`. Boa iniciativa, mostra que você olhou a tabela inteira, não só o que o enunciado listou.
- Nas células que filtram e calculam a taxa de engajamento: o filtro de `plays > 0` e o cálculo de `taxa_engajamento` estão corretos, e você conferiu quantas linhas foram descartadas (0, nesse caso), o que é exatamente o tipo de checagem que a aula pede.
- Na célula que compara média e mediana: a comparação entre média (9902,4) e mediana (1573,0) de curtidas está certa, e a interpretação escrita é boa: você identificou que a diferença grande entre os dois indica presença de vídeos com curtidas muito acima do resto, puxando a média para cima. Isso é exatamente o que se espera entender sobre distribuição assimétrica.
- Nas células do `explode` de hashtags: o `explode` e o `groupby` com `qtd_posts`, `curtidas_medias` e `engajamento_medio` estão corretos, sem erros de sintaxe ou de lógica.
- Parte 7 (salvar): a tabela final foi ordenada e salva em `dados/resumo_hashtags.csv` como pedido.

## O que faltou ou está errado

- **Bug na célula que monta a tabela final da Parte 6:** você aplicou `tabela_final["Curtidas médias"] = (tabela_final["Curtidas médias"] * 100).round(1)`. Esse `* 100` fazia sentido no comentário original do template (converter uma *taxa* como 0,14 em porcentagem, 14,0), mas você aplicou ele em cima de `curtidas_medias`, que já é uma contagem de curtidas, não uma taxa entre 0 e 1. O resultado é uma tabela com "Curtidas médias" de 43.170.000 para a hashtag `edit`, quando na verdade o valor real (antes da conta errada) seria 431.700. Vale conferir: se o objetivo era mostrar a taxa de engajamento em porcentagem, o `* 100` deveria estar na coluna `engajamento_medio`, não em `curtidas_medias`.
- **A pergunta não foi realmente respondida com código, na Parte 6.** Sua pergunta era comparar curtidas entre hashtags de política e hashtags de entretenimento, mas o código dessa mesma célula da Parte 6 só ordena `resumo_hashtags` inteiro por `curtidas_medias` e mostra o top 15 geral (que inclui `edit`, `lyricsvideo`, `coldplay`, `fyp`, mas nenhuma hashtag claramente política ali). A interpretação em texto ("vídeos com hashtags relacionadas a entretenimento possuem mais curtidas do que vídeos com hashtags relacionadas à política") não está apoiada em nenhuma comparação explícita entre os dois grupos, é uma leitura visual do top 15 geral. Isso é o tipo de "achado por impressão" que a aula pede pra evitar: para responder essa pergunta de verdade, seria preciso classificar quais hashtags são "política" e quais são "entretenimento" (uma lista de cada) e comparar as médias dos dois grupos, não só olhar o topo da tabela geral.
- **Fonte dos dados:** no README (Parte 8) você registrou "CSV disponibilizado pelo professor na aula 5" como fonte. Vale conferir com atenção se isso é mesmo o que você quer registrar aqui, porque o enunciado (Parte 0) pede a sua própria coleta da Aula 4 (ou um recorte dela). Se você usou o dataset de demonstração da aula em vez da sua coleta, bom deixar isso claro e, se possível, repetir a análise com os seus próprios dados na versão que vale nota.

## Sugestões de melhoria

- Para corrigir a Parte 6: monte duas listas de hashtags, por exemplo `hashtags_politica = ["trump", "estadosunidos", ...]` e `hashtags_entretenimento = ["coldplay", "lyricsvideo", "edit", ...]` (usando os nomes reais que aparecem na sua coleta), filtre `resumo_hashtags` com `.isin()` para cada grupo, e compare a média de `curtidas_medias` (ou some `qtd_posts * curtidas_medias` se quiser um total ponderado) entre os dois grupos. Aí sim a frase da interpretação fica apoiada em número, não em impressão.
- Depois de corrigir a lista de hashtags por categoria, revise a interpretação escrita: hoje ela generaliza para "vídeos com hashtags de entretenimento" a partir de só 4 hashtags no topo (`edit`, `lyricsvideo`, `coldplay`, `2016`), quase todas com só 1 post cada. Com `qtd_posts = 1`, uma curtida enorme domina a média sozinha, então vale comentar essa limitação (poucos posts por hashtag = média pouco confiável) na parte de limitações do README.
- Uma dica geral para não repetir o bug do `* 100`: sempre que copiar um comentário de exemplo do template, confira se ele ainda faz sentido para a coluna que você está de fato manipulando na linha de baixo.

Passado esse ajuste, o esqueleto do pipeline está bem feito, Sabrina: os cálculos de taxa de engajamento e a leitura de média vs. mediana mostram que você entendeu o que estava fazendo, só falta fechar o laço entre a pergunta que você mesma escolheu e o código que realmente a responde.

Prof. Matheus
