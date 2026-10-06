# Comandos da Aula 20 — API de leitura e camada de dados

Este arquivo lista os comandos usados nesta aula. Cada comando tem uma descrição objetiva. Use este arquivo como referência rápida, não como material de estudo principal. O notebook `20-api-e-persistencia.ipynb` explica cada comando em contexto.

Para `requests.get(url)` e `resposta.status_code`, confere na Aula 8, que tem mais desse comando. Para `uv venv`/`uv pip install -r requirements.txt`, confere na Aula 4. Para `.env` e `.gitignore` guardando chave/segredo, confere na Aula 2. Para `groupby()` no pandas, confere na Aula 5. Para `pd.to_datetime`, confere na Aula 10.

## Python — resposta de API como JSON

| Trecho | Efeito |
|---|---|
| `resposta.json()` | Transforma o corpo da resposta (texto JSON) direto num dicionário ou lista Python, sem precisar de parser manual. |

### Snippet — consumir uma API pública e checar o status antes de usar o resultado

```python
resposta = requests.get(url)

if resposta.status_code == 200:
    dado = resposta.json()
else:
    dado = None
    print("A API não respondeu como esperado, confira a URL e a conexão antes de continuar.")
```

## Python — autenticação por chave (conceitual)

| Trecho | Efeito |
|---|---|
| `headers={"Authorization": f"Bearer {chave}"}` | Passa a chave de API num cabeçalho da requisição, jeito mais comum em APIs sérias. |
| `requests.get(url, params={"api_key": chave})` | Passa a chave como parâmetro de query, outra forma comum. |
| `load_dotenv()` (biblioteca `python-dotenv`) | Lê as variáveis do arquivo `.env` da pasta do projeto. |
| `os.getenv("API_KEY")` | Pega o valor de uma variável de ambiente (aqui, a chave), sem escrevê-la no código. |

**ATENÇÃO:** nunca escreva uma chave de API direto no código (*hardcoded*), nem faça commit de um arquivo `.env` com chave real. Guarde a chave num `.env` listado no `.gitignore`.

## Python — criar uma API com FastAPI

| Trecho | Efeito |
|---|---|
| `from fastapi import FastAPI` | Importa a classe principal do framework. |
| `FastAPI()` | Cria o objeto da aplicação (aceita `title` e `description`, usados na documentação automática). |
| `@app.get("/rota")` | Registra a função logo abaixo para responder requisições GET nesse endereço. |
| `@app.get("/rota/{parametro}")` | Registra um endpoint com parâmetro de rota: o valor entre `{}` vem da própria URL. |
| `def funcao(parametro: int):` | Tipar o parâmetro (`int`, `str`, etc.) faz o FastAPI validar sozinho; se o tipo não bater, devolve erro `422` automaticamente, antes de a função rodar. |
| `return dicionario_ou_lista` | Dentro de um endpoint, devolver um dicionário ou lista faz o FastAPI converter para JSON sozinho. |

### Snippet — endpoint de leitura e endpoint com parâmetro de rota

```python
from fastapi import FastAPI

app = FastAPI()

produtos = [
    {"id": 1, "nome": "Caderno"},
    {"id": 2, "nome": "Caneta"},
]

@app.get("/produtos")
def listar_produtos():
    return produtos

@app.get("/produtos/{produto_id}")
def obter_produto(produto_id: int):
    for produto in produtos:
        if produto["id"] == produto_id:
            return produto
    return {"erro": f"Nenhum produto com id {produto_id}."}
```

## Terminal — rodar o servidor

| Comando | Efeito |
|---|---|
| `uv run uvicorn arquivo:app --reload` | Sobe o servidor FastAPI a partir do objeto `app` dentro de `arquivo.py`. `--reload` reinicia sozinho a cada alteração salva no código. |
| `uv run uvicorn pasta.arquivo:app --reload` | Mesma coisa, quando o arquivo está dentro de uma pasta (por exemplo `exemplos.api:app`). |
| `uv run uvicorn arquivo:app --reload --port 8002` | Mesma coisa, numa porta diferente da padrão (`8000`), útil quando a porta padrão já está em uso. |
| `Ctrl+C` (no terminal onde o servidor está rodando) | Para o servidor. |

## Navegador — testar a API

| Endereço | Efeito |
|---|---|
| `http://127.0.0.1:8000/docs` | Abre o Swagger UI: documentação automática, gerada pelo FastAPI a partir do próprio código, com botão "Try it out" para testar cada endpoint sem escrever código. |

## Python — camada de dados: Parquet

| Trecho | Efeito |
|---|---|
| `df.to_parquet("arquivo.parquet", index=False)` | Salva o DataFrame em Parquet: formato por coluna, arquivo menor que o CSV e que lembra o tipo de cada coluna (precisa da biblioteca `pyarrow`). |
| `pd.read_parquet("arquivo.parquet")` | Lê um Parquet de volta para DataFrame, com os tipos originais (datas continuam datas). |
| `pd.read_parquet("arquivo.parquet", columns=["a", "b"])` | Lê só as colunas pedidas; o resto do arquivo nem é carregado. |
| `Path("arquivo.parquet").stat().st_size` | Tamanho do arquivo em bytes, útil para comparar com o CSV equivalente. |
| `df.astype(object).where(df.notna(), None).to_dict(orient="records")` | Transforma o DataFrame numa lista de dicionários, trocando valores ausentes (`NaN`) por `None` (vira `null` no JSON). Usado nos endpoints da aula. |

**Por que Parquet:** é menor que o CSV, guarda o tipo das colunas, lê só as colunas necessárias, é aceito pela maioria das ferramentas de dados e é um arquivo só, sem servidor. Limites: é binário (não abre no Bloco de Notas nem no Excel) e não se edita uma linha por vez (o arquivo é regravado inteiro).

### Snippet — guardar uma coleta em Parquet e ler só duas colunas

```python
import pandas as pd

posts = pd.read_csv("dados/exportacao.csv", sep=";")
posts["timestamp"] = pd.to_datetime(posts["timestamp"])

posts.to_parquet("dados/coleta.parquet", index=False)

so_duas = pd.read_parquet("dados/coleta.parquet", columns=["author", "plays"])
```

## Boas práticas ao consumir e publicar APIs, e ao persistir dados

- Leia a documentação da API antes de programar em cima dela: endpoints, parâmetros obrigatórios, formato da resposta e limite de uso.
- Sempre confira `resposta.status_code` antes de chamar `.json()`.
- Nunca deixe chave de API escrita no código nem commitada; use `.env` e `.gitignore` (mesma regra das Aulas 2 e 3).
- Ao criar uma API própria, teste cada endpoint pela `/docs` antes de considerar pronto.
- Um endpoint que lê do Parquet pede só as colunas de que precisa (`columns=[...]`) e devolve o resultado. Se o arquivo não existir, a API responde `500`: gere o Parquet antes de subir o servidor.
- Arquivos `.parquet` são gerados, não versionados: mantenha `dados/*.parquet` no `.gitignore`.
