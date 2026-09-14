# Correção do Exercício 12 (classificação)

Oi, Sabrina! Antes de mais nada: esse exercício não vale nota individualmente (só vai entrar consolidado, junto com as Aulas 11 e 13, lá no Projeto 3). Isso aqui é feedback de prática mesmo, pra você chegar no Projeto 3 com a base já bem resolvida.

Resumo geral: entrega sólida, das mais completas que vi até agora. Você foi além do pedido em quase todo ponto (mais thresholds, mais features, leitura crítica de precisão/recall) e o README está bem escrito. O que falta é mais rigor na comparação entre modelos, algo que teria deixado a análise ainda mais redonda.

## O que ficou bom

- **A justificativa do corte de "viralizou" (na célula em que você define o percentil de corte, e no README) é a parte mais forte do trabalho.** Você não só escolheu o percentil 75, como explicou por que não usou o 90 (coleta pequena, 1138 posts, classe ficaria rara demais). Isso é exatamente o tipo de raciocínio que o exercício pede e que muita gente pula.
- **Sete features, todas sem vazamento** (`seguidores_autor`, `videos_autor`, `tam_legenda`, `n_emojis`, `n_hashtags`, `hora`, `dia_semana`), bem acima do mínimo de três. Gostei especialmente de `n_emojis` com regex e `n_hashtags` contando a lista de hashtags, mostra que você pensou em sinais de conteúdo, não só em metadados óbvios.
- **Threshold: você testou quatro cortes (0,50 / 0,30 / 0,20 / 0,15)**, o dobro do pedido, e para cada um imprimiu não só precisão/recall/F1 mas também quantos virais foram pegos e quantos alarmes falsos isso gerou (na célula que testa os quatro thresholds). Isso deixa a tabela muito mais legível do que só números soltos.
- **A leitura da matriz de confusão no README é substantiva, não descritiva.** Você não só disse "o recall é baixo", explicou o porquê em termos de negócio: "o modelo é seletivo, só marca viral quando tem confiança, por isso erra pouco na precisão, mas deixa passar a maioria dos virais de verdade". Isso é exatamente a "leitura de a favor de quem o modelo erra" que a Parte 5 pede.
- **A árvore rodou certinho com os parâmetros pedidos** (`max_depth=4`, `class_weight="balanced"`) e você imprimiu as `feature_importances_` ordenadas. Boa disciplina em seguir a especificação à risca.
- README completo, respondendo todos os itens da Parte 5, com declaração de uso de IA presente (mesmo que "não usei").

## O que faltou ou está errado

- **O maior ponto: você não comparou os modelos para escolher o "melhor" antes de analisar a matriz de confusão.** A Parte 5 pergunta pela matriz "do seu melhor modelo", mas você usou a regressão logística padrão (threshold 0,50, F1 = 0,24) sem justificar que ela é a melhor opção. Olhando os seus próprios números, a árvore teve F1 = 0,54 (bem melhor equilíbrio entre precisão 0,48 e recall 0,61) e até a logística com threshold 0,20 teve F1 = 0,45. Ou seja, pelos seus próprios dados, a logística padrão não era a melhor candidata para a leitura final, só a mais "padrão". Não tem problema nenhum ter feito assim, mas faltou uma frase dizendo "escolhi analisar esse modelo porque X" ou, melhor ainda, ter usado a árvore (ou a logística com threshold ajustado) como "melhor modelo" na análise.
- **A árvore nunca aparece no README.** Você a treinou e leu as `feature_importances_` no notebook, mas o README não menciona o resultado dela em nenhum momento, nem para comparar com a logística. Seria natural fechar com algo como "a árvore teve F1 melhor que a logística padrão porque..." isso amarraria as Partes 4 e 5.
- **Sobra de comentário desatualizado na célula em que você define o corte de "viralizou":** o comentário diz `# o valor de plays que separa os 10% mais vistos`, mas o código usa `quantile(0.75)`, ou seja, os 25% mais vistos. Ficou um resíduo do exemplo dado no enunciado (que usava percentil 90) que você esqueceu de ajustar ao trocar o corte. Não afeta o resultado, mas confunde quem lê o notebook depois.
- **A importância esmagadora de `seguidores_autor` (70% da importância da árvore) não foi discutida em nenhum lugar.** Isso é um achado relevante: sugere que o modelo está, na prática, prevendo "quem já tem mais seguidores" mais do que "o que faz um post específico viralizar". Valeria uma frase de reflexão sobre isso, é o tipo de limitação que os professores adoram ver identificada pelo próprio aluno.
- Pequenos deslizes de digitação no texto do README ("classificao", "classficados", "postsvirais" sem espaço em um trecho) — não prejudica o conteúdo, mas vale uma revisão rápida antes de reaproveitar esse texto no Projeto 3.

## Sugestões de melhoria

1. Quando for consolidar isso no Projeto 3, adicione uma célula (ou trecho no README) comparando explicitamente os F1 de logística (nos 4 thresholds) e da árvore lado a lado, e escolha o "melhor modelo" com base nisso antes de escrever a leitura da matriz de confusão.
2. Aproveite a árvore: ela teve o melhor F1 do exercício (0,54) e ainda te dá `feature_importances_`, que é uma informação melhor pra contar uma história (por que o modelo erra, o que ele mais usa) do que só os coeficientes da logística.
3. Puxe o achado de `seguidores_autor` dominar a árvore para o texto: isso é uma limitação real do seu modelo e mostra leitura crítica, exatamente o que o plano de aulas pede quando fala em "conclusão que não extrapola a amostra".
4. Antes de reaproveitar o notebook no Projeto 3, dá uma limpada nos comentários residuais (tipo o da `cell-5`) para não levar confusão adiante.

Fechando: o raciocínio sobre precisão/recall e a justificativa do corte estão no nível que eu queria ver em toda a turma. Falta só amarrar a comparação entre os dois modelos antes de dizer qual é "o melhor", e isso já deixa a base pronta pra render um Projeto 3 muito bom. Parabéns pelo capricho, Sabrina!

Prof. Matheus
