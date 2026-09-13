# Correção do Prof. Matheus, exercício 4 (coleta de redes)

Oi, Sabrina! LEMBRETE: Esse exercício não valia ponto! Tô corrigindo pq você pediu!

De modo geral você foi além do que a Parte 5 pedia e lidou bem com um problema real de dados. Ficou faltando fechar dois detalhes: uma célula que não rodou e um resultado estranho que passou batido.

## O que ficou bom

- Você identificou sozinha (com apoio de IA, e declarou isso, ótimo) que a coluna `body` não estava sendo reconhecida por causa de espaços em branco no nome da coluna, e resolveu com `df.columns = df.columns.str.strip()`, logo na célula em que você carrega o CSV. Isso é exatamente o tipo de problema real que aparece em dado raspado de rede social, e você não travou nele.
- A Parte 5 inteira está completa, inclusive os trechos que eram "avançados" em relação à aula: estatísticas das quatro métricas (na célula que roda o `describe()`), taxa de engajamento por vídeo calculada corretamente (na célula que calcula a taxa de engajamento, a fórmula `(likes + shares + comments) / plays` está certa), gráfico de curtidas médias por autor (na célula que plota o gráfico de barras) e uma pergunta própria com código e interpretação (nas últimas células da Parte 5, onde você formula, calcula e interpreta sua própria pergunta).
- A pergunta que você formulou ("o autor do vídeo mais curtido é o autor que mais posta?") é uma pergunta boa: compara duas métricas diferentes (pico vs. frequência) em vez de só repetir o que a aula já tinha mostrado.
- O README documenta a fonte, a busca (Rare Beauty e Fenty Beauty), os campos exportados e um limite ético específico da coleta (nada de conteúdo sensível/fotossensível), não é um texto genérico.
- A declaração de uso de IA está presente e específica: você disse onde usou (parte 2, parte 4, resposta da pergunta), que é exatamente o que a regra de transparência do curso pede.
- Na célula que baixa as thumbnails você adicionou uma checagem a mais (`linha.thumbnail_url.strip() != ""`) para evitar tentar baixar URL vazia, e declarou que usou IA ali. Mostra que você testou e ajustou, não só copiou.

## O que faltou ou está errado

- **A célula que baixa os vídeos nunca foi executada.** Olhando o notebook, essa célula não tem número de execução nem output, ou seja, ficou faltando rodar essa parte da Parte 4. Vale voltar lá e rodar, mesmo que o resultado seja "nenhum vídeo baixado" (TikTok às vezes não expõe `video_url` para todos os posts).
- **O resultado da célula que agrupa por autor pra achar quem mais postou é estranho e não foi questionado.** O código encontrou que o "autor com mais vídeos na coleta" é `@ no` (sim, o texto literal "no"), com 81 de 424 vídeos, quase 20% da coleta inteira. Isso não é um nome de usuário real, é quase certamente um problema de qualidade nos dados (a coluna `author` provavelmente tem valores vazios, mal formados ou você só limpou os *nomes* das colunas com `.str.strip()`, mas não os *valores* dentro delas, a célula que faz esse strip só limpa `df.columns`). Repare também nos outputs de outras células que os valores de texto vêm com espaços sobrando (`"rarebeauty          "`, `" melinda_melrose     "`). Isso é um sinal de que faltou também `df["author"] = df["author"].str.strip()` (e talvez em outras colunas de texto). Esse resultado acabou indo parar na interpretação escrita logo depois sem que o problema fosse notado, o que é um erro de leitura dos dados, não de código: sempre que um `value_counts()` ou `groupby()` devolver algo estranho demais (um autor sem nome com quase 20% dos posts), vale parar e desconfiar antes de reportar.
- **O README ficou com o período de coleta incompleto.** No notebook (célula da Parte 6) você escreveu "10/08/2026, 19:40 - 10/08/2026, 22:30", mas no `README.md` da pasta `projetos/04-coleta-redes/` ficou só "10/08/2026, 19:40 -", sem o horário de término. Parece um corta-e-cola que ficou pela metade.

## Sugestões de melhoria

- Depois de qualquer `.str.strip()` em nomes de coluna, vale já limpar também os valores de texto do DataFrame inteiro, algo como `df = df.apply(lambda col: col.str.strip() if col.dtype == "object" else col)`, isso evita exatamente o tipo de autor fantasma que apareceu naquela contagem.
- Antes de reportar um resultado de `groupby`/`value_counts` como conclusão, dá uma olhada rápida nas primeiras linhas do resultado (`.head()`) para ver se os valores fazem sentido. Um autor com quase 1 em cada 5 posts da coleta merece uma segunda olhada antes de virar interpretação final.
- Roda a célula que baixa os vídeos antes de considerar a entrega fechada, mesmo que só para confirmar que não há vídeo para baixar (o checklist da Parte 7 pede exatamente isso).
- Ao preencher o README a partir do notebook, vale reler o texto final para não perder metade de uma resposta no corta-e-cola.

## Fechamento

No geral, é um exercício sólido, com pensamento crítico de verdade (o ajuste da coluna `body`, a checagem extra no download de thumbnails) e a Parte 5 bem resolvida. O que falta é revisão fina: rodar a célula que ficou pendente e desconfiar de um resultado estatístico esquisito antes de aceitá-lo como resposta. Segue assim!

Prof. Matheus
