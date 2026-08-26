# Abre a página Russia do Ground News, clica 10 vezes em "More stories",
# coleta título e URL de cada notícia e salva em CSV.
# Rode na pasta da aula:
#   uv run exemplos/02_listar_com_more_stories.py
# Autor: Matheus C. Pestana

import csv  # para escrever o arquivo CSV no final
import time  # para uma pausinha curta entre cliques (educacional / gentil)
from pathlib import Path  # caminhos de pasta/arquivo de forma simples

from playwright.sync_api import sync_playwright  # API síncrona do Playwright

# Pasta dados/ fica um nível acima de exemplos/ (ao lado do notebook da aula).
pasta_dados = Path(__file__).parent.parent / "dados"

# Cria a pasta se ainda não existir (não dá erro se já existir).
pasta_dados.mkdir(exist_ok=True)

# URL da listagem que vamos automatizar.
url = "https://ground.news/interest/russia"

# Quantas vezes vamos clicar em "More stories" nesta aula.
MAX_MORE_CLICKS = 10

# Lista de dicionários: cada um vira uma linha no CSV.
noticias = []

# Guarda URLs já vistas, para não repetir a mesma notícia no CSV.
urls_ja_vistas = set()

# Inicia o Playwright; o with fecha tudo ao final.
with sync_playwright() as p:
    # headless=False: abre a janela do Chromium para a turma ver o que acontece.
    browser = p.chromium.launch(headless=False)

    # User-Agent de navegador real reduz chance de bloqueio automático.
    context = browser.new_context(
        user_agent=(
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0.0.0 Safari/537.36"
        ),
        locale="en-US",
    )

    # Nova aba.
    page = context.new_page()

    # Abre a página (domcontentloaded é mais estável neste site do que networkidle).
    page.goto(url, wait_until="domcontentloaded", timeout=45000)

    # Fecha cookies, se o banner aparecer (Accept costuma ser o da edição EN).
    for texto_botao in ["Accept", "Aceitar", "Reject non-essential", "Negar não essencial", "Deny"]:
        botao = page.get_by_role("button", name=texto_botao)
        if botao.count() > 0:
            try:
                botao.first.click(timeout=3000)
            except Exception:
                pass
            break

    # Alguns banners usam só o texto "Accept All" / similares.
    for texto_botao in ["Accept All", "Accept all", "Aceitar todos"]:
        botao = page.get_by_role("button", name=texto_botao)
        if botao.count() > 0:
            try:
                botao.first.click(timeout=3000)
            except Exception:
                pass
            break

    # Fecha onboarding, se existir.
    botao_fechar = page.query_selector('[data-testid="onboarding-close-button"]')
    if botao_fechar is not None:
        try:
            botao_fechar.click()
        except Exception:
            pass

    # Espera o primeiro card (attached = existe no DOM, mesmo se animando).
    page.wait_for_selector('[data-testid="story-item"]', state="attached", timeout=45000)

    # Clica "More stories" algumas vezes para carregar mais cards.
    for clique in range(MAX_MORE_CLICKS):
        # Quantos cards existem agora (antes do clique).
        quantidade_antes = len(page.query_selector_all('[data-testid="story-item"]'))

        # Localiza o botão pelo data-testid estável do site.
        botao_more = page.query_selector('[data-testid="load-more-stories-button"]')

        # Plano B: texto do botão.
        if botao_more is None and page.get_by_role("button", name="More stories").count() > 0:
            botao_more = page.get_by_role("button", name="More stories").first

        # Se o botão sumiu, não tem mais o que carregar.
        if botao_more is None:
            print(f"clique {clique + 1}: botão More stories não encontrado, parando")
            break

        # Rola até o botão ficar visível (senão o clique pode falhar em silêncio).
        botao_more.scroll_into_view_if_needed()

        # Clica no botão.
        botao_more.click()

        # Espera a lista crescer (mais cards no DOM).
        try:
            page.wait_for_function(
                f"document.querySelectorAll('[data-testid=\"story-item\"]').length > {quantidade_antes}",
                timeout=20000,
            )
            agora = len(page.query_selector_all('[data-testid="story-item"]'))
            print(f"clique {clique + 1}: ok, cards agora = {agora}")
        except Exception:
            # Se não cresceu a tempo, avisa e segue (às vezes a página já no limite).
            print(f"clique {clique + 1}: lista não cresceu a tempo, seguindo assim mesmo")

        # Pausa curta entre cliques (uso educacional, sem martelar o site).
        time.sleep(1)

    # Agora percorre todos os cards visíveis e coleta título + URL.
    cards = page.query_selector_all('[data-testid="story-item"]')
    print(f"total de cards na tela: {len(cards)}")

    for card in cards:
        # Dentro do card, o link da story aponta para /article/...
        link = card.query_selector('a[href*="/article/"]')

        # Se por algum motivo não achar link, pula este card.
        if link is None:
            continue

        # URL completa da notícia no Ground News.
        href = link.get_attribute("href")

        # Se o href vier relativo, o Playwright às vezes já devolve absoluto;
        # se ainda for relativo, montamos na mão.
        if href is None:
            continue
        if href.startswith("/"):
            href = "https://ground.news" + href

        # Evita duplicata (o mesmo article pode aparecer mais de uma vez na página).
        if href in urls_ja_vistas:
            continue
        urls_ja_vistas.add(href)

        # Título limpo: o card guarda o headline em um h4.
        titulo_el = card.query_selector("h4")
        titulo = (titulo_el.text_content() or "").strip() if titulo_el else ""

        # Se não achar h4, tenta o alt da imagem do card.
        if titulo == "":
            img = card.query_selector("img[alt]")
            if img is not None:
                titulo = (img.get_attribute("alt") or "").strip()

        # Último recurso: usa a própria URL.
        if titulo == "":
            titulo = href

        # Guarda um dicionário por notícia (vira linha no CSV).
        noticias.append({"titulo": titulo, "url": href})

    # Screenshot de evidência da listagem depois dos cliques.
    page.screenshot(path=str(pasta_dados / "screenshot-ground-russia-lista.png"))

    # Fecha o navegador.
    browser.close()

# Caminho do CSV de saída.
caminho_csv = pasta_dados / "ground-russia-lista.csv"

# Escreve o CSV com cabeçalho.
with open(caminho_csv, "w", encoding="utf-8", newline="") as arquivo:
    colunas = ["titulo", "url"]
    escritor = csv.DictWriter(arquivo, fieldnames=colunas)
    escritor.writeheader()
    escritor.writerows(noticias)

print(f"notícias únicas salvas: {len(noticias)}")
print(f"CSV: {caminho_csv}")
print(f"Screenshot: {pasta_dados / 'screenshot-ground-russia-lista.png'}")
