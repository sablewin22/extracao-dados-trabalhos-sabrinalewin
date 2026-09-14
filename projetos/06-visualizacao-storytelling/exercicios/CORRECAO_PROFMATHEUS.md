# Correção do Prof. Matheus (Exercício 6, sem nota)

Oi, Sabrina! LEMBRETE: Esse exercício não valia ponto! Tô corrigindo pq você pediu!

De modo geral, foi um exercício bem resolvido: os dois gráficos estão completos, as interpretações mostram cuidado real em não extrapolar além do que os dados permitem, e você adaptou o roteiro (dispersão) pra responder à sua própria pergunta em vez de simplesmente copiar o exemplo da aula. Isso é exatamente o espírito do exercício.

## O que ficou bom

- **Parte 0:** a pergunta ("a quantidade de seguidores do autor influencia na quantidade de curtidas dele?") é clara e bem justificada.
- **Parte 2 (gráfico de barras):** segue o checklist inteiro (`figsize`, título, rótulos nos dois eixos, fonte dos dados, rotação dos nomes das hashtags pra não sobrepor). Muito bom sinal que você tenha usado `tick_params(axis="x", rotation=45)`, é um detalhe que várias pessoas esquecem.
- **Interpretação do gráfico de barras:** você pegou exatamente o cuidado que o enunciado pedia na OBS, notou que "rock" ficou no topo com **1 post só** e não generalizou o resultado pra além desta coleta. Isso é o tipo de leitura crítica que o exercício quer treinar.
- **Parte 3 (dispersão):** aqui teve uma boa adaptação: em vez de reproduzir literalmente o par sugerido no enunciado (`author_followers` vs. `taxa_engajamento`), você trocou o eixo Y pra `author_likes`, porque é o que a sua pergunta da Parte 0 pedia (curtidas do autor, não engajamento do post). O enunciado permite essa troca ("outros pares também valem, desde que a pergunta da Parte 0 peça isso") e você usou essa liberdade corretamente, não é um erro, é a aplicação certa da regra.
- **Escala log no eixo X:** usada e justificada no comentário do código, exatamente como a aula ensinou pra não esmagar as contas pequenas.
- **Interpretações em texto (barras e dispersão):** as duas cumprem o que a Parte 6 pede, dizem o que o gráfico permite concluir e o que não permite. Gostei em especial de você citar os "pontos fora do padrão" na interpretação da dispersão, isso mostra que você olhou o gráfico de verdade, não só descreveu o que esperava ver.
- **Parte 4 (resposta final):** está bem calibrada, sem "sempre", sem "garante", plenamente de acordo com o que a Parte 4 pede.
- **README:** as duas perguntas dos gráficos e a declaração de uso de IA estão lá, preenchidas.

## O que faltou ou está errado

- **Duplicação de pontos no gráfico de dispersão:** como `author_followers` e `author_likes` são atributos do **autor**, não do post, um autor com vários posts na coleta aparece várias vezes no gráfico, sempre no mesmo ponto (ou quase, se `author_likes` mudar entre coletas do mesmo autor). Isso não invalida a leitura que você fez, mas pode estar deixando o gráfico "pesado" em regiões onde um autor específico postou muito, dando a impressão de mais dados do que realmente existem autores distintos ali.

## Sugestões de melhoria

- Na dispersão, vale testar um `df_posts.drop_duplicates(subset=["author_followers", "author_likes"])` (ou agrupar por autor) antes de plotar, só pra ver se o padrão visual muda quando cada autor conta uma vez só. Pode ser um exercício rápido de comparação, sem precisar refazer a entrega.
- Também dá pra colocar escala log no eixo Y além do X, se as curtidas tiverem uma cauda longa parecida com a de seguidores (alguns autores com poucas curtidas, poucos com muitas). Só olhando o gráfico gerado dá pra decidir se vale a pena.
- Bom hábito pra próximas entregas: mesmo em exercício sem nota, marcar o checklist final ajuda a pegar esquecimentos antes de considerar a entrega fechada.

Continue assim, o raciocínio nas interpretações está no ponto certo (nem subestima nem exagera o que o gráfico mostra). 

Prof. Matheus
