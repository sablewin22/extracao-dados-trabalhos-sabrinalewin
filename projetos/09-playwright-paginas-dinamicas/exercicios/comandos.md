# Comandos da Aula 9: Playwright e Ground News

Roteiro prático da aula. **Copie e cole no terminal**, um passo de cada vez.
A coleta **não** roda no Jupyter: use o Terminal integrado do VS Code (ou CMD no Windows / Terminal no Mac).

Trabalhe a partir da pasta da aula:

`aulas/09-playwright-paginas-dinamicas`

O ambiente Python é o `.venv` da **raiz** do repositório da disciplina (não crie outro `.venv` aqui dentro).

---

## 0. Ir até a pasta da aula

**Windows (Prompt de Comando ou Terminal do VS Code):**
```cmd
cd caminho\para\aulas\09-playwright-paginas-dinamicas
```

**Mac (Terminal ou Terminal do VS Code):**
```bash
cd caminho/para/aulas/09-playwright-paginas-dinamicas
```

Troque `caminho/...` pelo caminho real no seu computador.

---

## 1. Instalar bibliotecas e o navegador do Playwright

Faça na **raiz** do repositório da disciplina (onde está o `requirements.txt` grande e o `.venv`).

Há **dois caminhos**. Use o que combina com o seu ambiente. Nos dois casos o passo do navegador (`playwright install chromium`) é **obrigatório** e separado da instalação da biblioteca Python: sem ele, os scripts abrem e quebram pedindo o Chromium.

### Caminho A: com `uv` (preferido)

**Windows:**
```cmd
cd caminho\para\repositorio-da-disciplina
uv pip install -r requirements.txt
uv run playwright install chromium
```

**Mac:**
```bash
cd caminho/para/repositorio-da-disciplina
uv pip install -r requirements.txt
uv run playwright install chromium
```

### Caminho B: com `.venv` ativado (`venv` / virtualenv, sem `uv`)

Se o seu `.venv` foi criado com `python -m venv` (ou virtualenv) e você **não** usa `uv`, ative o ambiente primeiro e depois instale.

**Windows:**
```cmd
cd caminho\para\repositorio-da-disciplina
.venv\Scripts\activate
pip install -r requirements.txt
playwright install chromium
```

**Mac:**
```bash
cd caminho/para/repositorio-da-disciplina
source .venv/bin/activate
pip install -r requirements.txt
playwright install chromium
```

**OBS:** com o `(.venv)` ativado, `playwright` e `python -m playwright` são equivalentes. Se `playwright` não for reconhecido, use:

```bash
python -m playwright install chromium
```

**O que observar:** o `playwright install chromium` baixa o navegador uma vez por computador (algumas dezenas de MB). Depois volte para a pasta da aula (passo 0).

Se o `uv` não funcionar na máquina do lab, o guia completo está em `tutoriais/uv_nao_funcionando.md`.

---

## 2. Por que requests não basta (script 01)

Com `uv`:
```bash
uv run exemplos/01_requests_vs_playwright.py
```

Com `.venv` ativado (sem `uv`):
```bash
python exemplos/01_requests_vs_playwright.py
```

**O que observar:** o `requests` conta os cards do HTML bruto; o Playwright clica uma vez em **More stories** e a contagem **cresce**. Só o navegador executa o JavaScript.

---

## 3. Listar notícias com 10 cliques em More stories (script 02)

Com `uv`:
```bash
uv run exemplos/02_listar_com_more_stories.py
```

Com `.venv` ativado:
```bash
python exemplos/02_listar_com_more_stories.py
```

**O que observar:** a janela do Chromium abre (os scripts usam `headless=False`). No terminal, dez linhas do tipo `clique 1: ok, cards agora = 20`, etc. Ao final:

- CSV: `dados/ground-russia-lista.csv` (colunas `titulo`, `url`)
- Screenshot: `dados/screenshot-ground-russia-lista.png`

Abra o CSV no Excel / Numbers / VS Code e confira se as URLs começam com `https://ground.news/article/`.

---

## 4. Entrar em cada notícia e salvar detalhes (script 03)

Rode **depois** do passo 3 (ele lê o CSV da lista).

Com `uv`:
```bash
uv run exemplos/03_detalhar_stories.py
```

Com `.venv` ativado:
```bash
python exemplos/03_detalhar_stories.py
```

**O que observar:** a janela do Chromium abre e vai passando de story em story. No terminal, uma linha por notícia (`[1/N] https://...`). Com 10 cliques a lista fica grande: o script 03 pode demorar vários minutos (abre cada página e espera 1 segundo entre elas). Nem toda story tem o painel Coverage Details completo; nesses casos as colunas do painel ficam vazias.

Ao final:

- CSV: `dados/ground-russia-detalhes.csv`
- Screenshot da primeira story: `dados/screenshot-ground-russia-story.png`

Colunas do CSV de detalhes:

| Coluna | Conteúdo |
|---|---|
| `url` | Link da story no Ground News |
| `titulo` | Título (`h1`) |
| `summary` | Resumo curto |
| `total_news_sources` | Total News Sources (painel) |
| `leaning_left` / `leaning_right` / `center` | Contagens do painel |
| `last_updated` | Last Updated |
| `bias_distribution` | Bias Distribution (ex.: `47% Right`) |
| `source_urls` | Links das fontes, separados por `\|` |

---

## 5. Checagens rápidas do CSV

**Windows:**
```cmd
more dados\ground-russia-lista.csv
more dados\ground-russia-detalhes.csv
```

**Mac:**
```bash
head dados/ground-russia-lista.csv
head dados/ground-russia-detalhes.csv
```

---

## Referência rápida: Playwright (sync)

| Trecho | Efeito |
|---|---|
| `from playwright.sync_api import sync_playwright` | Importa a API síncrona. |
| `with sync_playwright() as p:` | Liga o Playwright e fecha tudo ao final. |
| `p.chromium.launch(headless=False)` | Abre o Chromium **com** janela (a turma vê o que acontece). `True` = sem janela. |
| `browser.new_page()` | Abre uma aba. |
| `page.goto(url)` | Navega até a URL. |
| `page.wait_for_selector("...")` | Espera o elemento aparecer. |
| `page.query_selector_all("...")` | Lista todos os elementos que batem com o seletor. |
| `elemento.click()` | Clica. |
| `elemento.scroll_into_view_if_needed()` | Rola a página até o elemento ficar visível. |
| `elemento.text_content()` | Texto do elemento. |
| `elemento.get_attribute("href")` | Valor de um atributo HTML. |
| `page.screenshot(path="...")` | Salva um PNG da página. |
| `browser.close()` | Fecha o navegador. |

Seletores estáveis usados nesta aula:

| Seletor | Onde |
|---|---|
| `[data-testid="story-item"]` | Card na listagem |
| `[data-testid="load-more-stories-button"]` | Botão More stories |
| `a[href*="/article/"]` | Link da story |
| `h4` (dentro do card) | Título na listagem |
| `h1` | Título na página da story |

---

## Erros comuns

| Mensagem / sintoma | O que fazer |
|---|---|
| `TimeoutError` esperando seletor | Confira internet; feche cookies; aumente o `timeout`; veja se o site mudou o `data-testid`. |
| Status `403` no `requests` | Inclua um `User-Agent` de navegador no `headers` (os scripts da aula já fazem isso). |
| Lista não cresce no More stories | Use `scroll_into_view_if_needed()` antes do clique; aceite o banner de cookies (`Accept`). |
| `Sync API inside the asyncio loop` | Você tentou Playwright sync **dentro** do Jupyter. Rode no terminal (`uv run` ou `python` com `.venv` ativado). |
| Script 03 não acha o CSV | Rode o script 02 antes. |
| `playwright install` / navegador faltando | Com `uv`: `uv run playwright install chromium`. Com `.venv` ativado: `playwright install chromium` (ou `python -m playwright install chromium`). |

---

## Ética (curto)

- O `robots.txt` do Ground News permite `/` (bloqueia `/mediaopoly`).
- Use pausas entre páginas (o script 03 já espera 1s).
- Material educacional: não martelar o site, não contornar login/paywall.
- Não pedimos campos premium (factuality / ownership).
