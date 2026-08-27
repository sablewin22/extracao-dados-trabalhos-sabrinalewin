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
MAX_MORE_CLICKS = 2

# Caminho do CSV de saída.
caminho_csv = pasta_dados / "exercicio-lista.csv"

# CSV produzido pelo script 02 (precisa existir antes).
caminho_detalhes = pasta_dados / "exercicio-detalhes.csv"

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


dominios_ignorar = (
    "ground.news",
    "twitter.com",
    "x.com",
    "instagram.com",
    "linkedin.com",
    "facebook.com",
    "reddit.com",
)

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

          # Na primeira (e se reaparecer), tira overlays da frente.
    fechar_overlays(page)
    
            # Espera o título principal.
    page.wait_for_selector("h1", timeout=30000)

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
    
        # Fecha o navegador.
    browser.close()
    
with open(caminho_csv, "w", encoding="utf-8", newline="") as arquivo:
    colunas = ["titulo", "url"]
    escritor = csv.DictWriter(arquivo, fieldnames=colunas)
    escritor.writeheader()
    escritor.writerows(noticias)

print(f"notícias únicas salvas: {len(noticias)}")
print(f"CSV: {caminho_csv}")

linhas_lista = []
with open(caminho_csv, encoding="utf-8", newline="") as arquivo:
    leitor = csv.DictReader(arquivo)
    for linha in leitor:
        linhas_lista.append(linha)

print(f"stories na lista: {len(linhas_lista)}")

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

        # Pausa de 1 segundo entre stories.
        time.sleep(1)

    browser.close()

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


print(f"notícias únicas salvas: {len(noticias)}")
print(f"CSV: {caminho_csv}")
print(f"detalhes salvos: {len(detalhes)}")
print(f"CSV: {caminho_detalhes}")
