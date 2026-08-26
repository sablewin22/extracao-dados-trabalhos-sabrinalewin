# Lê o CSV da listagem (script 02), abre cada /article/, extrai summary,
# links de sources e o painel Coverage Details, e salva outro CSV.
# Rode DEPOIS do 02, na pasta da aula:
#   uv run exemplos/03_detalhar_stories.py
# Autor: Matheus C. Pestana

import csv  # ler a lista e gravar os detalhes
import time  # pausa entre páginas (gentil com o site)
from pathlib import Path  # caminhos de arquivo

from playwright.sync_api import sync_playwright  # Playwright síncrono

# Pasta dados/ ao lado do notebook.
pasta_dados = Path(__file__).parent.parent / "dados"
pasta_dados.mkdir(exist_ok=True)

# CSV produzido pelo script 02 (precisa existir antes).
caminho_lista = pasta_dados / "ground-russia-lista.csv"

# CSV de saída deste script.
caminho_detalhes = pasta_dados / "ground-russia-detalhes.csv"

# Redes sociais e o próprio Ground News não contam como "source" de jornal.
dominios_ignorar = (
    "ground.news",
    "twitter.com",
    "x.com",
    "instagram.com",
    "linkedin.com",
    "facebook.com",
    "reddit.com",
)


def fechar_overlays(page):
    """Fecha cookies e onboarding se estiverem na frente do conteúdo."""
    for texto_botao in ["Accept", "Aceitar", "Reject non-essential", "Negar não essencial", "Deny", "Accept All", "Accept all"]:
        botao = page.get_by_role("button", name=texto_botao)
        if botao.count() > 0:
            try:
                botao.first.click(timeout=3000)
            except Exception:
                pass
            break
    botao_fechar = page.query_selector('[data-testid="onboarding-close-button"]')
    if botao_fechar is not None:
        try:
            botao_fechar.click()
        except Exception:
            pass


def valor_do_painel(linhas, rotulo):
    """
    No painel Coverage Details o texto vem em linhas tipo:
      Leaning Left
      9
    Esta função devolve a linha seguinte ao rótulo pedido.
    """
    for i, linha in enumerate(linhas):
        if linha.strip() == rotulo and i + 1 < len(linhas):
            return linhas[i + 1].strip()
    return ""


# Lê as URLs que o script 02 salvou.
linhas_lista = []
with open(caminho_lista, encoding="utf-8", newline="") as arquivo:
    leitor = csv.DictReader(arquivo)
    for linha in leitor:
        linhas_lista.append(linha)

print(f"stories na lista: {len(linhas_lista)}")

# Aqui vamos acumulando um dicionário por story.
detalhes = []

with sync_playwright() as p:
    # headless=False: abre a janela do Chromium para a turma ver cada story.
    browser = p.chromium.launch(headless=False)
    context = browser.new_context(
        user_agent=(
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0.0.0 Safari/537.36"
        ),
        locale="en-US",
    )
    page = context.new_page()

    for indice, item in enumerate(linhas_lista):
        url = item["url"]
        print(f"[{indice + 1}/{len(linhas_lista)}] {url}")

        # Abre a página da story.
        page.goto(url, wait_until="domcontentloaded")

        # Na primeira (e se reaparecer), tira overlays da frente.
        fechar_overlays(page)

        # Espera o título principal.
        page.wait_for_selector("h1", timeout=30000)

        # Título visível da notícia.
        titulo_el = page.query_selector("h1")
        titulo = (titulo_el.text_content() or "").strip() if titulo_el else ""

        # Summary curto: o site coloca um dek em h2.sr-only.
        summary = ""
        dek = page.query_selector("h2.sr-only")
        if dek is not None:
            summary = (dek.text_content() or "").strip()

        # Se o dek vier vazio, tenta o primeiro parágrafo longo da página.
        if summary == "":
            for paragrafo in page.query_selector_all("p"):
                texto = (paragrafo.text_content() or "").strip()
                if len(texto) > 80:
                    summary = texto
                    break

        # Painel direito: bloco cujo texto contém Coverage Details.
        total_news_sources = ""
        leaning_left = ""
        leaning_right = ""
        center = ""
        last_updated = ""
        bias_distribution = ""

        # Percorre divs e pega a primeira que parece o painel de métricas.
        for bloco in page.query_selector_all("div"):
            texto = (bloco.inner_text() or "").strip()
            # Painel compacto: tem os rótulos e não é a página inteira.
            if "Coverage Details" in texto and "Bias Distribution" in texto and len(texto) < 800:
                linhas = [ln for ln in texto.splitlines() if ln.strip() != ""]
                total_news_sources = valor_do_painel(linhas, "Total News Sources")
                leaning_left = valor_do_painel(linhas, "Leaning Left")
                leaning_right = valor_do_painel(linhas, "Leaning Right")
                center = valor_do_painel(linhas, "Center")
                last_updated = valor_do_painel(linhas, "Last Updated")
                bias_distribution = valor_do_painel(linhas, "Bias Distribution")
                break

        # Links externos das sources (jornais), sem redes e sem o próprio Ground.
        source_urls = []
        for ancora in page.query_selector_all('a[href^="http"]'):
            href = ancora.get_attribute("href") or ""
            href_lower = href.lower()
            if any(dom in href_lower for dom in dominios_ignorar):
                continue
            if href not in source_urls:
                source_urls.append(href)

        # Junta as URLs numa string só, separadas por | (fácil de abrir no Excel depois).
        source_urls_str = "|".join(source_urls)

        detalhes.append({
            "url": url,
            "titulo": titulo,
            "summary": summary,
            "total_news_sources": total_news_sources,
            "leaning_left": leaning_left,
            "leaning_right": leaning_right,
            "center": center,
            "last_updated": last_updated,
            "bias_distribution": bias_distribution,
            "source_urls": source_urls_str,
        })

        # Screenshot só da primeira story (evidência, sem encher o disco).
        if indice == 0:
            page.screenshot(path=str(pasta_dados / "screenshot-ground-russia-story.png"))

        # Pausa de 1 segundo entre stories.
        time.sleep(1)

    browser.close()

# Grava o CSV de detalhes.
with open(caminho_detalhes, "w", encoding="utf-8", newline="") as arquivo:
    colunas = [
        "url",
        "titulo",
        "summary",
        "total_news_sources",
        "leaning_left",
        "leaning_right",
        "center",
        "last_updated",
        "bias_distribution",
        "source_urls",
    ]
    escritor = csv.DictWriter(arquivo, fieldnames=colunas)
    escritor.writeheader()
    escritor.writerows(detalhes)

print(f"detalhes salvos: {len(detalhes)}")
print(f"CSV: {caminho_detalhes}")
