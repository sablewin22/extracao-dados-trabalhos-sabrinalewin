# Correção, Prof. Matheus (Exercício 11, regressão com scikit-learn)

> Antes de mais nada: este exercício não vale nota individualmente, é só um treino de aula. A boa notícia é que essa base já pode ser reaproveitada no Projeto 3 (case, peso 2), então vale a pena deixar bem redondinha antes de chegar lá.

Oi, Sabrina! Esse exercício ficou muito bom. A parte mais importante da aula (não vazar dado) você acertou de cara, e ainda por cima defendeu a escolha por escrito com clareza. Só tem alguns pontos de acabamento pra ajustar antes de reaproveitar isso no Projeto 3.

## O que ficou bom

- **Zero vazamento de dado.** No `X` (célula da Parte 2) você não colocou `likes`, `comments`, `shares` nem `plays`, e ainda por cima explicou por escrito, no README, exatamente por que essas colunas não podem entrar (é o próprio cálculo do alvo). Esse é o erro mais comum dessa aula e você não caiu nele.
- **As sete features são todas "de antes da publicação"** e fazem sentido: `seguidores_autor`, `videos_autor`, `tam_legenda`, `n_emojis`, `n_hashtags`, `hora`, `dia_semana`. Gostei especialmente da conta de emojis com regex de faixa Unicode (`\U0001F000-\U0001FAFF`, `☀-➿`) e do parsing de hashtags tratando string vazia (`0 if s == "" else len(s.split(","))`), isso é exatamente o tipo de detalhe que quebra o código de quem esquece o caso vazio.
- **Você conferiu tipo e valor ausente antes de seguir** (célula da Parte 3, `X.dtypes` e `X.isna().sum()`), que é justamente o passo que o exercício pede como checkpoint antes de treinar.
- **Leitura dos resultados com espírito crítico de verdade.** Na resposta "o seu melhor modelo bateu o bobo?" você não só copiou os números, comparou MAE e R² e percebeu que eles contam histórias diferentes: a árvore teve o menor MAE (por pouquíssima margem, 0.0323 contra 0.0324), mas o R² dela ficou pior que o do bobo (-0.295 contra -0.000). Isso é sofisticado: muita gente ia só olhar "menor MAE = ganhou" e carimbar a árvore como vencedora, sem perceber que ela está overfitando e generalizando pior. Você percebeu.
- **A leitura do coeficiente é cautelosa do jeito certo**: "é uma associação nos meus dados, não quer dizer que sempre vai aumentar o engajamento". Isso é exatamente a diferença entre correlação e causa que a aula queria que vocês internalizassem.
- **README completo e no lugar certo** (`projetos/11-regressao-scikit-learn/README.md`), com todos os itens pedidos: fonte, número de posts, features, colunas descartadas, os três resultados e a leitura de coeficiente.

## O que faltou ou está errado

- **O notebook salvo não parece ter rodado do início ao fim numa única passada.** Reparei que a célula da árvore (Parte 4) está com `execution_count: null` no arquivo `.ipynb`, mesmo tendo output visível. Isso normalmente acontece quando você edita uma célula depois de já ter os resultados e salva sem rodar de novo (ela "perde" o número de execução mas mantém o output antigo na tela). O item do checklist "roda do início ao fim sem erro com Kernel → Restart e Run All" pede justamente pra evitar isso, porque não dá pra garantir que os números que aparecem na tela são os mesmos que o código atual produziria. Vale rodar `Restart Kernel & Run All` de novo antes de considerar fechado.
- **Import duplicado** na célula da Parte 4: `from sklearn.tree import DecisionTreeRegressor` aparece duas vezes seguidas. Não quebra nada, mas é sinal de código colado sem revisar depois.
- **`dados/exportacao.csv` foi commitado** (ele apareceu no `git pull`, não está no `.gitignore` dessa pasta). O checklist pede que a pasta `dados/` esteja ignorada. Não é grave (o professor já flexibilizou isso pra turma inteira no Projeto 2), mas como é fácil de resolver, deixo o alerta pra próxima entrega que valer nota.

## Sugestões de melhoria

- Antes de reaproveitar essa base no Projeto 3, dá um `Restart Kernel & Run All` fresco e confere se os números da árvore batem com o que está no README (evita divergência entre o que o notebook mostra hoje e o que foi escrito).
- Já que o R² de todos os modelos ficou perto de zero ou negativo, seria interessante, mais pra frente, investigar se a distribuição de `taxa_engajamento` tem outliers muito fortes (posts com `plays` baixíssimo geram taxa de engajamento artificialmente alta). Um histograma rápido de `y` ajudaria a enxergar isso, e pode ser parte do que você discute no Projeto 3 quando for justificar a variável de regressão.
- Como próximo passo de curiosidade (não obrigatório aqui): tentar um `max_depth` menor pra árvore, tipo 2 ou 3, pra ver se ela para de overfitar tanto e o R² dela melhora. Com sete features e poucos posts em cada "folha", profundidade 5 pode estar sendo demais para o tamanho da base.
- Adicionar `dados/` ao `.gitignore` desta pasta antes da entrega que valer nota (Projeto 3), pra não subir o CSV bruto pro repositório público.

## Fechamento

Você entendeu o conceito central da aula (vazamento de dado) e ainda soube ler criticamente resultados de modelo fraco, que é mais raro do que parece nessa etapa do curso. É só dar aquela passada de "rodar tudo de novo do zero" antes do Projeto 3 e está pronto pra reaproveitar sem susto. Bom trabalho, Sabrina!

Prof. Matheus
