"""API de exemplo da Aula 20 (segunda metade: lendo de um arquivo Parquet).

Diferente de exemplos/api.py, este servidor NÃO tem os dados escritos no
código. Cada endpoint lê o arquivo dados/coleta.parquet (criado na Seção 10
do notebook), calcula o que foi pedido e devolve o resultado.

Antes de rodar, garanta que dados/coleta.parquet existe: rode a Seção 10 do
notebook 20-api-e-persistencia.ipynb (a célula que faz posts_slim.to_parquet(...)).

Para rodar (na pasta aulas/20-api-e-persistencia/, com o ambiente já criado
e as dependências instaladas):

Windows (Prompt de Comando ou Terminal integrado do VS Code):
    uv run uvicorn exemplos.api_dados:app --reload

Mac (Terminal ou Terminal integrado do VS Code):
    uv run uvicorn exemplos.api_dados:app --reload

Depois abra no navegador:
    http://127.0.0.1:8000/docs

Para parar o servidor, volte ao terminal e aperte Ctrl+C.
"""

from pathlib import Path

import pandas as pd
from fastapi import FastAPI

app = FastAPI(
    title="API da Aula 20 — lendo do Parquet",
    description="Os endpoints leem o arquivo data/coleta.parquet, não uma lista no código.",
)

ARQUIVO = Path(__file__).resolve().parent.parent / "data" / "coleta.parquet"


def ler(colunas):
    """Lê do Parquet só as colunas pedidas e devolve um DataFrame."""
    return pd.read_parquet(ARQUIVO, columns=colunas)


def como_registros(tabela):
    """Transforma o DataFrame numa lista de dicionários que o FastAPI converte em JSON."""
    # valores ausentes (NaN) viram None (null no JSON); NaN puro quebraria a resposta
    tabela = tabela.astype(object).where(tabela.notna(), None)
    return tabela.to_dict(orient="records")


@app.get("/")
def raiz():
    return {"mensagem": "API da Aula 20 no ar, lendo de data/coleta.parquet. Veja /docs."}


@app.get("/posts")
def listar_posts(limite: int = 10):
    # limite é parâmetro de query (?limite=3); o ": int = 10" valida e dá um padrão
    posts = ler(["id", "author", "timestamp", "plays", "likes"])
    return como_registros(posts.head(limite))


@app.get("/autores")
def contar_por_autor():
    # o groupby (Aula 5) roda aqui na API: ela devolve o resultado já agregado
    posts = ler(["author", "plays"])
    por_autor = (
        posts.groupby("author")
        .agg(n_posts=("plays", "size"), media_plays=("plays", "mean"))
        .round()
        .sort_values("n_posts", ascending=False)
        .reset_index()
        .rename(columns={"author": "autor"})
    )
    return como_registros(por_autor)
