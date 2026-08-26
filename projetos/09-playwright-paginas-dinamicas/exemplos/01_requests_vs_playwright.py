# Compara a mesma URL do Ground News com requests (HTML bruto, sem JavaScript)
# e com Playwright (navegador de verdade). O ponto central: só o navegador
# consegue clicar em "More stories" e carregar mais cards.
# Rode na pasta da aula:
#   uv run exemplos/01_requests_vs_playwright.py
# Autor: Matheus C. Pestana

import requests  # baixa o HTML "cru" da página, sem executar JavaScript
from bs4 import BeautifulSoup  # interpreta o HTML baixado, no estilo da Aula 8
from playwright.sync_api import sync_playwright  # abre um navegador controlado por código

# Página de interesse "Russia" no Ground News.
url = "https://ground.news/interest/russia"

# Cabeçalho simples: alguns sites respondem 403 sem User-Agent de navegador.
cabecalhos = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )
}

print("=== 1) Com requests (sem JavaScript) ===")

# Pede a página ao servidor, como na Aula 8.
resposta = requests.get(url, headers=cabecalhos, timeout=30)

# Mostra o código HTTP (200 = ok).
print("status_code:", resposta.status_code)

# Ajusta a codificação do texto, para não bagunçar acentos.
resposta.encoding = resposta.apparent_encoding

# Transforma a string HTML numa "sopa" navegável.
sopa = BeautifulSoup(resposta.text, "html.parser")

# Cards que já vieram no HTML inicial (às vezes o servidor manda alguns).
cards_brutos = sopa.find_all("div", {"data-testid": "story-item"})
print("cards no HTML bruto:", len(cards_brutos))

# O botão de carregar mais existe no HTML? Contamos só a tag.
botao_bruto = sopa.find("button", {"data-testid": "load-more-stories-button"})
print("botão More stories no HTML bruto:", "sim" if botao_bruto else "não")
print("OBS: mesmo com o botão no HTML, o requests NÃO clica nele nem espera o JS.")
print()

print("=== 2) Com Playwright (com JavaScript) ===")

# Inicia o Playwright e garante que tudo fecha ao final, mesmo se der erro.
with sync_playwright() as p:
    # Abre o Chromium sem janela visível (mais leve para a aula).
    # headless=False: abre a janela do Chromium para a turma ver o que acontece.
    browser = p.chromium.launch(headless=False)

    # Contexto com User-Agent de navegador real (evita bloqueio bobinho).
    context = browser.new_context(
        user_agent=(
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0.0.0 Safari/537.36"
        ),
        locale="en-US",
    )

    # Cria uma aba nova.
    page = context.new_page()

    # Navega até a URL (domcontentloaded é mais estável que networkidle neste site).
    page.goto(url, wait_until="domcontentloaded", timeout=45000)

    # Tenta fechar o banner de cookies (Accept = edição em inglês).
    for texto_botao in ["Accept", "Aceitar", "Reject non-essential", "Negar não essencial", "Deny", "Accept All", "Accept all"]:
        botao = page.get_by_role("button", name=texto_botao)
        if botao.count() > 0:
            try:
                botao.first.click(timeout=3000)
            except Exception:
                pass
            break

    # Fecha o diálogo de onboarding, se existir.
    botao_fechar = page.query_selector('[data-testid="onboarding-close-button"]')
    if botao_fechar is not None:
        try:
            botao_fechar.click()
        except Exception:
            pass

    # Espera até pelo menos um card de notícia existir no DOM.
    page.wait_for_selector('[data-testid="story-item"]', state="attached", timeout=45000)

    # Conta os cards logo após o carregamento.
    antes = len(page.query_selector_all('[data-testid="story-item"]'))
    print("cards no navegador (antes do More stories):", antes)

    # Clica uma vez em More stories (isso o requests nunca faz).
    botao_more = page.query_selector('[data-testid="load-more-stories-button"]')
    if botao_more is None:
        # Plano B: achar pelo texto do botão.
        if page.get_by_role("button", name="More stories").count() > 0:
            botao_more = page.get_by_role("button", name="More stories").first

    if botao_more is not None:
        botao_more.scroll_into_view_if_needed()
        # Clica e espera a lista crescer (às vezes o site demora um pouco).
        botao_more.click()
        try:
            page.wait_for_function(
                f"document.querySelectorAll('[data-testid=\"story-item\"]').length > {antes}",
                timeout=25000,
            )
        except Exception:
            # Segunda tentativa: clicar de novo pelo texto do botão.
            if page.get_by_role("button", name="More stories").count() > 0:
                page.get_by_role("button", name="More stories").first.scroll_into_view_if_needed()
                page.get_by_role("button", name="More stories").first.click()
                page.wait_for_timeout(3000)
        depois = len(page.query_selector_all('[data-testid="story-item"]'))
        print("cards no navegador (depois de 1 clique em More stories):", depois)
        if depois <= antes:
            print("OBS: a lista não cresceu desta vez (rede/site). Rode o script de novo.")
    else:
        print("botão More stories não apareceu no navegador")

    # Fecha o navegador de forma explícita.
    browser.close()

print()
print("O requests vê o HTML inicial. O Playwright clica, espera o JS e a lista cresce.")
print("É por isso que usamos Playwright nesta aula.")
