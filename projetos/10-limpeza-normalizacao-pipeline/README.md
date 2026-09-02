README

**Fonte da coleta bruta (aula de origem, site, data da coleta original):**

> Aula 8, site original: Book to Scrape, data da coleta original, 21/08/2026

**Como rodar o pipeline do zero (comandos de ambiente, nome do notebook, ordem das células):**

> Ativar o ambiente virtual (.venv), abrir o notebook 10-limpeza-normalizacao-pipiline.ipynb, executar todas as células de cima para baixo em ordem.

**Que tipos de sujeira o pipeline trata, e como (uma frase por tipo: texto, data, número, duplicata, valor ausente):**

> Texto: Remove espaços em branco usando ".str.strip()". Número: Remove o símbolo da moeda libra com .str.replace() e converte a coluna para formato numérico usandoo pd.to_numeric(). Duplicata: remove linhas repetidas do csv usando .drop_duplicates(). Valor ausente: converte falhas falhas de conversão em NaN pelo comando errors="coerce"

**Quantas linhas entraram, quantas saíram e por que a diferença (baseado no log):**

> Entraram 19 linhas e saíram 19 linhas. Isso aconteceu pois não tinha duplicatas no csv.

**Que erro(s) o `try`/`except` da Parte 8 tratou de verdade nesta coleta (se nenhum valor problemático apareceu, explique como você testou que o tratamento funciona mesmo assim):**

> O `try`/`except` da Parte 8 trata de possíveis erros de conversão do tipo ValueError na coluna preco_livro. Não apareceu nenhum valor problemático, mas sei que funciona pois coloquei um erro propositalmente na base dados para ver se ele reagia.

**Declaração de uso de IA:** Foi usado o Claude para testar se o tratamento da Parte 8 realmente funciona.