# Aula 9: Playwright e páginas dinâmicas (Ground News)

Comece pelo roteiro de terminal: **[comandos.md](comandos.md)**. É nele que você copia e cola os comandos, aos poucos.

O notebook [09-playwright-paginas-dinamicas.ipynb](09-playwright-paginas-dinamicas.ipynb) só explica o contexto (por que Playwright, o que vamos coletar no [Ground News – Russia](https://ground.news/interest/russia), ética). **A coleta não roda no Jupyter** (a API síncrona do Playwright não combina com o loop do notebook).

## Scripts em `exemplos/`

1. `01_requests_vs_playwright.py`: HTML bruto (`requests`) vs navegador (clique em More stories).
2. `02_listar_com_more_stories.py`: 10 cliques em More stories → `dados/ground-russia-lista.csv`.
3. `03_detalhar_stories.py`: abre cada `/article/` → `dados/ground-russia-detalhes.csv`.

Todos usam Playwright **sync**, com comentários quase linha a linha. Rode com `uv`:

```bash
uv run exemplos/01_requests_vs_playwright.py
uv run exemplos/02_listar_com_more_stories.py
uv run exemplos/03_detalhar_stories.py
```

Ou, com o `.venv` da raiz **ativado** (sem `uv`): `python exemplos/01_requests_vs_playwright.py` (e o mesmo para 02 e 03).

Use o `.venv` da **raiz** do repositório da disciplina. Instale as libs e o Chromium do Playwright (passo separado):

- com `uv`: `uv pip install -r requirements.txt` e depois `uv run playwright install chromium`
- com `.venv` ativado: `pip install -r requirements.txt` e depois `playwright install chromium` (ou `python -m playwright install chromium`)

Detalhes em [comandos.md](comandos.md).

## Exercício

Depois: [exercicios/exercicio-09-playwright-paginas-dinamicas.ipynb](exercicios/exercicio-09-playwright-paginas-dinamicas.ipynb). Você escreve um script `.py` próprio (outro interesse do Ground News, 2 cliques em More stories) e roda no terminal.
