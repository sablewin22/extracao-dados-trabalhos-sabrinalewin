**README:**

**Pergunta:**
> o que este recorte de notícias da Agência Brasil e da CNN Brasil mostra sobre a cobertura de Lula e Flávio Bolsonaro?

**Objetivo:**
> Transformar textos curtos de notícias em dados auditáveis (tokens, tópicos, contagens de menções, fichas extraídas por modelo de linguagem e buscas) e tirar conclusões proporcionais ao tamanho da amostra.

**Preparação:**
> Fonte: dados/noticias_lula_flavio_2026.csv, publicado no repositório da disciplina.

> Janela temporal: 3 a 13 de outubro de 2026.

> Regra de seleção: 40 matérias escolhidas, 10 por combinação de veículo e foco.

> Campo analisado: texto_analise (título + resumo). Mediana de 203,5 caracteres, cerca de 32 palavras por matéria.

> Denominadores:
        foco_amostral   Flávio Bolsonaro   Lula
veiculo                               
Agência Brasil                10            10
CNN Brasil                    10            10

**Revisão das aulas 21-22:**
> Aula 21: O texto original deve ser preservado e cada regra precsa ser justificada e mostrada em exemplos.

> Aula 22: o TF-IDF dá peso às palavras que distinguem um documento dos outros, e o NMF agrupa essas palavras em poucos tópicos. O nome de cada tópico é uma leitura humana das palavras e machates representativas, e alguns tópicos não formam um tema coerente.

**Roteiro de análise:**
> Carregar a base e conferir 40 linhas, datas, URLs e o equilíbrio 10x4.

> Crias o texto_preparado e a versão sem stopwords. Contar tokens antes e depois. Mostrar três casos lado a lado

> Aplicar TF-IDF + NMF com 4 tópicos (random-state=42). Nomear os tópicos. cruzar com veículo e foco.

> Contar menções a Lula e a Flávio por grupo, sempre com denominador.

> Extrair fichas estrturadas com Groq numa amostra de 16 matérias (4 por grupo) e auditar 4 delas.

> Comparar o top 3 da busca por palavra com busca por semântica para uma pergunta fixa.

**Achados:**
> 1. as matérias sobre Bolsonaro se concentram em tópicos diferentes em cada veículo. Na CNN se concentram no tópico 0 (ex: P37, "Centrão mira pastas com maior orçamento se Flávio vencer" https://www.cnnbrasil.com.br/blogs/isabel-mega/eleicoes/centrao-mira-pastas-com-maior-orcamento-se-flavio-vencer/) e na Agência Brasil no tópico 2.

> 2. apoio político aparece para os dois candidatos, em veículos diferentes. Na Agência Brasil: P14, "Flávio Bolsonaro recebe apoio de governadores eleitos e Cury" (https://agenciabrasil.ebc.com.br/politica/noticia/2026-10/flavio-bolsonaro-recebe-apoios-de-governadores-eleitos-e-cury). Na CNN: P21, "MDB em dez estados do Norte e Nordeste declaram apoio à reeleição de Lula" (https://www.cnnbrasil.com.br/eleicoes/mdb-em-dez-estados-do-norte-e-nordeste-declaram-apoio-a-reeleicao-de-lula/).

**Tópico confuso:**
> O Tópico 3 é o mais confuso, pois junta assuntos diversos ("Minha Casa, Minha Vida", "custo de vida" e "site de criptomoedas") apenas porque compartilham palavras como "casa", "vida e "site". Isso acontece justamente por os textos serem curtos e usarem poucas palavras, assim o modelo agrupa matérias diferentes.

**Fichas auditadas:**
> P16 (Agência Brasil x Flávio): ausência. o "fato" omite que a campanha nega envolvimento e a denúncia à PGE. "limite" veio como texto "null". Atribuição ambígua: a "pessoa_central" é o Flávio, mas quem age é o site.

> P09 (Agência Brasil x Lula): ausência. possui "limite" igual a "48 horas" sem explicar a que se refere.

> P33 (CNN x Flávio): ausência. omite que TSE e entidades atribuíram o problema a falha técnica. O "limite" não é um limite.

> P23 (CNN x Lula): exagero. a "evidência" é o texto inteiro, não um trecho. A "pessoal_central" veio como texto "null".

**Comparação de buscas:**

> P21, P14, P21 são relevantes

> P40 não é relavante (falso positivo)

> P37, P04 são parciais, visto que uma delas fala sobre negociação de cargos, não um apoio declarado, já a segunda utiliza a palavra estudantes, e eles não são necessariamente lideranças.

**Limitações:**
> 40 materias escolhidas, não aleatórias, 10 por grupo.

> Textos curtos (título + resumo), o que deixa os tópicos dependentes de poucas palavras.

> A limpeza remove números (percentuais, 6x1, prazos...)

> A avaliação de relevância das buscas é manual e feita pelos critérios determinados pela pessoa.


**Uso de Ia:** Foi utilizada para corrigir erro na cécula de stopwords que estava vindo igual a "depois". A célula de contagem de menções também foi feita com auxílio de IA.