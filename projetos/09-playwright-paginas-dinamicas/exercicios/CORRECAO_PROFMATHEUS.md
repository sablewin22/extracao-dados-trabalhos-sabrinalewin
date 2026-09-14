# Correção, Prof. Matheus (Aula 9, Playwright)

Oi, Sabrina! LEMBRETE: Esse exercício não valia ponto! Tô corrigindo pq você pediu! Valeu por ter feito e deixado no repositório, dá muito mais pra comentar um exercício de verdade do que um notebook em branco.

## Resumo geral

O script (`exercicio_09_script.py`) está sólido, roda de ponta a ponta e resolve os dois estágios pedidos (listagem + detalhamento). O ponto fraco não é o código, é a parte de registro no notebook: o que você anotou na Parte 0/1 não bate com o que o script realmente coletou, e a Parte 4/5 ficaram rasas.

## O que ficou bom

- A estrutura geral do script segue exatamente o roteiro pedido: abre a URL, fecha overlays, espera o `story-item`, clica 2 vezes em "More stories" com `scroll_into_view_if_needed()` antes do clique, salva a lista, depois percorre cada URL para os detalhes. Passo a passo certinho.
- A função `fechar_overlays()`, logo no início do script, tem plano A (texto do botão) e plano B (botão de onboarding), e não quebra o script se não achar nada, isso é maturidade, não só copiar o exemplo da aula.
- No trecho que extrai o título de cada story você fez fallback em cascata: `h4` → `alt` da imagem → a própria URL. Isso mostra que você pensou no caso em que o seletor principal falha, que é exatamente o tipo de robustez que interessa em scraping.
- A lista `dominios_ignorar`, perto do topo do script, para filtrar links de redes sociais e do próprio Ground News das `source_urls`, é uma sacada boa, evita sujar o CSV de fontes com lixo.
- O `wait_for_function` esperando o número de cards crescer, logo depois de cada clique em "More stories", em vez de um `sleep` fixo, é a forma certa de esperar conteúdo dinâmico carregar, ótimo uso do Playwright aí.
- O `time.sleep(1)` entre stories, dentro do laço que percorre cada URL de detalhe, está presente e você citou isso certo na Parte 5.
- O CSV de detalhes tem as 10 colunas exatamente como pedido no enunciado (no trecho final, onde você monta e salva esse CSV).

## O que faltou ou está errado

- **A URL não bate com o que você registrou.** Na Parte 0 e na Parte 1 do notebook você escreveu `https://ground.news/interest/sanctions` como o interesse escolhido. Mas logo no topo do script, onde a URL é definida, o código usa `url = "https://ground.news/interest/russia"`, e os arquivos em `dados/` confirmam isso (`ground-russia-lista.csv`, `ground-russia-detalhes.csv` ao lado dos `exercicio-*.csv`). Ou seja, o que você documentou não é o que rodou de fato. Isso é o tipo de coisa que, numa entrega que valesse nota, derrubaria a confiança no restante do registro, presta atenção nisso daqui pra frente.
- **Os CSVs foram salvos fora da pasta pedida.** O enunciado (Parte 2, item 5) pede `dados/exercicio-lista.csv` dentro de `exercicios/`. O seu script calcula, logo no início, `pasta_dados = Path(__file__).parent.parent / "dados"`, ou seja, sobe um nível e salva em `projetos/09-playwright-paginas-dinamicas/dados/`, junto dos arquivos que vieram dos scripts de exemplo da aula (`ground-russia-*`, screenshots). Funciona, mas mistura a sua entrega com o material de demonstração na mesma pasta.
- **A Parte 4 (log) não tem o nível de detalhe pedido.** O enunciado pede log por etapa: "listagem: quantos cards após 2 cliques" e "cada story: ok ou timeout". Seu script até imprime isso no terminal (o `print` de `clique {clique+1}: ok, cards agora = ...`, logo depois de cada clique, e o `print` de `[{indice+1}/{len(linhas_lista)}] {url}`, no laço que percorre cada story), só que você não colou esse log real no notebook, colou um resumo genérico de 4 linhas com contagem final. O log granular existe, só faltou trazer ele pra cá.
- **A resposta de ética (Parte 5) está com bastante erro de digitação e rasa no conteúdo**: "quai rota" (creio que seria "quais rotas"), "crawlwer", "acessraem". Além da questão de digitação, a pergunta pede especificamente o que o `robots.txt` do Ground News permite, e você respondeu de forma genérica ("define quais rotas o site autoriza") sem dizer o que de fato está liberado ou bloqueado para esse site. Vale a pena ter realmente aberto `ground.news/robots.txt` e citado algo concreto de lá.
- Você colou só 2 linhas de exemplo do CSV de detalhes na Parte 3, o enunciado pede 3.
- Tem uns trechos de indentação estranha no script (por exemplo, o laço `for clique in range(...)` que faz os cliques em "More stories", e o bloco que extrai o "Painel direito" de cada story, mais adiante no arquivo, que têm indentação extra e comentários alinhados de forma inconsistente). Não quebra a execução porque o Python só olha blocos relativos, mas dá pra ver que foi colado de outro lugar e não reformatado, o que é exatamente o tipo de "copy-paste sem leitura completa" que o enunciado pediu pra evitar.

## Sugestões de melhoria

1. Antes de preencher o notebook, roda o script e só depois registra as respostas, conferindo se o que você escreveu bate com o que saiu no terminal (isso teria pego a diferença "sanctions" vs "russia" na hora).
2. Ajusta o `pasta_dados` do script pra apontar pra dentro de `exercicios/dados/`, como pedido, em vez de subir um nível.
3. Cola o log real (as linhas que o script já imprime) na Parte 4, em vez de escrever um resumo à parte, você já tem a informação, só falta trazer ela pro lugar certo.
4. Passa um corretor ortográfico rápido nas respostas em texto livre antes de considerar a entrega pronta, principalmente na parte de ética que é avaliada pelo conteúdo, não só pela mecânica.
5. Dá uma limpada na indentação do script (um "reformatar documento" no VS Code resolve isso em segundos) pra ele ficar consistente do início ao fim.

Tirando esses pontos, o esqueleto do scraping em si está bem encaminhado, dá pra ver que você entendeu a lógica de espera de conteúdo dinâmico, cliques e coleta em duas etapas.

Prof. Matheus
