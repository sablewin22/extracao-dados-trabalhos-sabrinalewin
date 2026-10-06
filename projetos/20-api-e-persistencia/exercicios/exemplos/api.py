"""API de exemplo da Aula 20 (primeira metade: catálogo fixo no código).

Este arquivo NÃO roda dentro do notebook. Ele roda no terminal, num processo
separado, porque um servidor fica ligado esperando pedidos (não termina
sozinho como uma célula normal).

Para rodar (na pasta aulas/20-api-e-persistencia/, com o ambiente já criado
e as dependências instaladas):

Windows (Prompt de Comando ou Terminal integrado do VS Code):
    uv run uvicorn exemplos.api:app --reload

Mac (Terminal ou Terminal integrado do VS Code):
    uv run uvicorn exemplos.api:app --reload

Depois de rodar, abra no navegador:
    http://127.0.0.1:8000/docs

Para parar o servidor, volte ao terminal e aperte Ctrl+C.
"""

from fastapi import FastAPI  # classe principal do framework, cria o app

app = FastAPI(
    title="API da Aula 20",
    description="API de exemplo: catálogo pequeno de produtos, fixo no código. A Seção 11 da aula tem a versão que lê de um Parquet (api_dados.py).",
)  # cria a aplicação; o Swagger em /docs usa esse título e descrição

# "base de dados" fixa, só para a aula: uma lista de dicionários em memória.
# Isso significa que, se você reiniciar o servidor, os dados voltam ao estado original
# (a Seção 11 da aula troca isso por dados lidos de um arquivo Parquet).
produtos = [
    {"id": 1, "nome": "Caderno", "preco": 12.5, "categoria": "papelaria"},
    {"id": 2, "nome": "Caneta", "preco": 3.0, "categoria": "papelaria"},
    {"id": 3, "nome": "Mochila", "preco": 89.9, "categoria": "acessorios"},
]


@app.get("/")  # endpoint raiz, útil só para confirmar que o servidor está de pé
def raiz():
    return {"mensagem": "API da Aula 11 está no ar. Veja /docs para a documentação."}


@app.get("/produtos")  # endpoint de leitura: devolve a lista inteira
def listar_produtos():
    return produtos  # FastAPI converte a lista de dicionários em JSON sozinho


@app.get("/produtos/{produto_id}")  # parâmetro de rota: {produto_id} vem da URL
def obter_produto(produto_id: int):  # o ": int" pede ao FastAPI para validar o tipo
    # se alguém pedir /produtos/abc (não é número), o FastAPI devolve erro 422
    # automaticamente, antes mesmo de esta função rodar
    for produto in produtos:
        if produto["id"] == produto_id:
            return produto  # achou: devolve o dicionário do produto

    return {"erro": f"Nenhum produto com id {produto_id}."}  # não achou: resposta simples
