"""API do exercício da Aula 20.

Assim como os exemplos da aula (`exemplos/api.py` e `exemplos/api_dados.py`),
este arquivo NÃO roda dentro do notebook. Ele roda no terminal, num processo
separado, porque um servidor fica ligado esperando pedidos.

A ideia deste exercício é a da segunda metade da aula: a API NÃO tem os dados
escritos no código. Ela lê de um arquivo Parquet (`dados/coleta.parquet`) que
você cria na Parte 3B do notebook, a partir de uma coleta sua de uma aula
anterior.

Para rodar (nesta pasta `exercicios/`, com o ambiente já criado, as
dependências instaladas e o `dados/coleta.parquet` já gerado pelo notebook):

Windows (Prompt de Comando ou Terminal integrado do VS Code):
    uv run uvicorn api_exercicio:app --reload

Mac (Terminal ou Terminal integrado do VS Code):
    uv run uvicorn api_exercicio:app --reload

Depois de rodar, abra no navegador:
    http://127.0.0.1:8000/docs

Para parar o servidor, volte ao terminal e aperte Ctrl+C.

O QUE FAZER NESTE ARQUIVO
--------------------------
1. Rode a Parte 3B do notebook para gerar `dados/coleta.parquet` a partir da
   sua coleta.
2. Complete o endpoint `listar_registros`: leia o Parquet com `ler()` e devolva
   as primeiras `limite` linhas (siga o modelo de `exemplos/api_dados.py`,
   endpoint `/posts`).
3. Complete o endpoint `resumo`: leia o Parquet e agregue com `groupby()` por
   alguma coluna de categoria da sua coleta (autor, hashtag, dia...),
   devolvendo a contagem por grupo (modelo: endpoint `/autores` do exemplo).
4. Rode o servidor e teste os dois endpoints pela documentação automática em
   `/docs`. Depois apague `dados/coleta.parquet` e teste de novo: o erro que
   aparece mostra que a API agora depende do arquivo existir.
"""

from pathlib import Path

import pandas as pd
from fastapi import FastAPI

app = FastAPI(
    title="API do exercício - Minha Coleta",  # TODO: troque por um título seu
    description="Os endpoints da API para consulta dos dados coletados.",  # TODO
)

# caminho do Parquet criado na Parte 3B do notebook (pasta dados/ ao lado deste arquivo)
ARQUIVO = Path(__file__).resolve().parent / "dados" / "coleta.parquet"


def ler(colunas=None):
    """Lê o Parquet e devolve um DataFrame (com `colunas`, lê só essas; sem, lê todas)."""
    return pd.read_parquet(ARQUIVO, columns=colunas)


def como_registros(tabela):
    """Transforma o DataFrame numa lista de dicionários que o FastAPI converte em JSON."""
    # valores ausentes (NaN) viram None (null no JSON); NaN puro quebraria a resposta
    tabela = tabela.astype(object).where(tabela.notna(), None)
    return tabela.to_dict(orient="records")


@app.get("/")
def raiz():
    return {"mensagem": "API do exercício no ar, lendo de dados/coleta.parquet. Veja /docs."}


@app.get("/registros")
def listar_registros(limite: int = 10):
    # TODO: devolva as primeiras `limite` linhas da sua coleta.
    # Modelo: registros = ler(); return como_registros(registros.head(limite))
    posts = ler(["id", "author", "timestamp", "plays", "likes"])
    return como_registros(posts.head(limite))


@app.get("/resumo")
def resumo():
    # TODO: devolva uma contagem por grupo, com groupby, sobre a sua coleta.
    # Escolha a coluna de agrupamento que faça sentido para a sua coleta.
    # Modelo: o endpoint /autores de exemplos/api_dados.py.
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
