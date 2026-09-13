# Correção do exercício 10 (limpeza, normalização e pipeline)

Oi, Sabrina! LEMBRETE: Esse exercício não valia ponto! Tô corrigindo pq você pediu! (a entrega que conta ponto, a Entrega do Módulo 3, é o notebook principal na pasta `10-limpeza-normalizacao-pipeline/`, fora dessa subpasta `exercicios/`.)

Resumo geral: pipeline roda de ponta a ponta, os números do log batem com o CSV bruto e o `data/raw/` ficou intocado. O maior furo é a Parte 7 (validação de colunas obrigatórias), que ficou sem ser preenchida de verdade.

## O que ficou bom

- **Parte 0 e 2** bem registradas: você identificou corretamente que `preço_livro` precisava virar número e que não havia valores ausentes (conferi, bate com o CSV).
- **Parte 3**: normalização de texto certa (`titulo_livro.str.strip()`, `estoque_livro.str.title()`), e você acertou em não inventar uma coluna de data que não existe no seu CSV, em vez de forçar um `pd.to_datetime` sem sentido.
- **Parte 4**: conversão de `preço_livro` de texto pra número ficou correta (`str.replace("£", "")` seguido de `pd.to_numeric`). Conferi o `data/processed/coleta_tratada.csv` e os 19 preços saíram numéricos e certinhos.
- **Parte 5**: contagem e remoção de duplicata feita do jeito certo, mesmo não havendo duplicata nesse CSV.
- **Parte 8 é o ponto mais legal do notebook**: você percebeu (ou testou) que o primeiro `try`/`except` nunca ia cair no `except`, porque a coluna já estava convertida pra número antes dessa célula, então criou uma segunda célula injetando `"abc_invalido"` numa cópia dos dados pra provar que o tratamento de exceção funciona de verdade. Isso é exatamente o tipo de raciocínio que a Parte 8 pede ("se nenhum valor problemático apareceu, explique como você testou que o tratamento funciona mesmo assim") e você não só explicou, testou. Também gostei de você ter declarado o uso do Claude para esse teste específico, isso é declaração de IA bem feita: pontual, sobre o que exatamente foi usado.
- **Parte 9**: log com os números certos, salvo em `data/processed/log-pipeline.txt`, e o `data/raw/coleta.csv` permanece intocado (conferi os dois arquivos lado a lado).
- **Parte 11 (README)**: respostas honestas e específicas, inclusive explicando o "porquê" da diferença de linhas (não houve, porque não havia duplicata).

## O que faltou ou está errado

- **Parte 7 é o problema real do notebook.** A célula está assim:
  ```python
  colunas_obrigatorias = []  # substitua pela lista de colunas que o seu pipeline exige
  ```
  Você deixou a lista vazia, então o `for coluna in colunas_obrigatorias` nunca executa nenhuma iteração, e o `print("Validação de colunas obrigatórias: OK")` aparece mesmo que todas as colunas do CSV tivessem sumido. Ou seja, a validação existe no papel, mas não valida nada de verdade. O comentário ao lado da linha já avisava pra substituir isso pela lista real (algo como `["titulo_livro", "preço_livro", "estoque_livro"]`), e esse passo ficou pra trás.
- **Parte 6**: a célula ficou só com `pass` (o comentário pedia pra remover essa linha quando escrevesse o código de verdade). Como não havia valor ausente mesmo, não tinha o que aplicar, tudo bem, mas o `pass` sozinho passa a impressão de que a parte ficou incompleta em vez de "não se aplica, e por isso está vazia de propósito".
- **Ordem de execução das células**: os números entre colchetes pulam de forma estranha ([2], [3], [4], [17], [6], [7], [20], [25]...), o que mostra que você rodou fora de ordem em algum momento. Isso não muda o resultado final salvo (conferi que bate), mas a Parte 10 do enunciado pede exatamente pra você rodar a Parte 9 de novo e conferir que só `data/processed/` muda. Vale rodar o notebook inteiro de cima pra baixo (Restart & Run All) antes de considerar pronto, só pra garantir que não existe nenhuma dependência escondida de uma célula anterior que você rodou fora de ordem.
- Pequeno typo no README (Parte 11): "`10-limpeza-normalizacao-pipiline.ipynb`" (sobrou um "i" a mais em "pipiline").

## Sugestões de melhoria

- Preencha `colunas_obrigatorias` na Parte 7 com as três colunas reais do seu CSV e teste de propósito removendo uma coluna numa cópia do `df`, só pra ver o `ValueError` disparar (o mesmo espírito de teste que você já usou muito bem na Parte 8).
- Evite recalcular a mesma coisa duas vezes: a conversão de `preço_livro` aparece de novo na célula da Parte 9 (`df["preço_livro"] = df["preço_livro"].astype(str)...`), quando ela já tinha sido feita na Parte 4. Não quebra nada, mas é código repetido à toa; dá pra confiar no `df` que já vem da Parte 4.
- Antes de considerar o exercício pronto, roda tudo de novo do zero (Kernel → Restart & Run All), exatamente como a Parte 10 pede, pra garantir que a sequência de células conta a história certa.

Fora esses dois pontos (a validação vazia e a ordem de execução), o pipeline está sólido: os dados batem, o log é coerente e o raciocínio de teste da Parte 8 foi além do que a maioria costuma fazer. Só fechar essa lacuna da Parte 7 que fica redondo.

Prof. Matheus
