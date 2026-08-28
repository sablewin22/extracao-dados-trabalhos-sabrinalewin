# Script de apoio: valida se um CSV processado tem as colunas obrigatórias,
# e se nenhuma delas está inteiramente vazia. É a mesma checagem da Seção 11
# do notebook da aula, isolada aqui como script, para rodar sozinha fora do
# Jupyter (por exemplo, como último passo de um pipeline mais automatizado).
#
# Uso:
#   Windows (CMD ou Terminal integrado do VS Code):
#       uv run exemplos/validar_colunas.py dados/processed/livros-tratado.csv
#   Mac (Terminal ou Terminal integrado do VS Code):
#       uv run exemplos/validar_colunas.py dados/processed/livros-tratado.csv

import sys  # para ler o caminho do arquivo passado na linha de comando
from pathlib import Path  # para lidar com caminho de arquivo

import pandas as pd  # biblioteca de tabelas

# colunas que este pipeline considera obrigatórias (mesmo conjunto da Seção 11 do notebook)
COLUNAS_OBRIGATORIAS = ["titulo", "categoria", "preco", "avaliacao", "data_coleta"]


def validar_colunas(caminho_csv):
    """Confere se um CSV tem as colunas obrigatórias, todas com algum dado.

    Entrada: caminho_csv (str ou Path), o endereço de um arquivo CSV.
    Saída: None (a função não devolve nada); levanta ValueError se algo faltar.

    Exemplo:
        validar_colunas("dados/processed/livros-tratado.csv")
        # imprime "Validação de colunas obrigatórias: OK" se estiver tudo certo

    Teste rápido (rode isto manualmente para conferir o comportamento):
        import pandas as pd
        pd.DataFrame({"titulo": ["Livro 1"], "categoria": ["Poetry"]}).to_csv("teste.csv", index=False)
        validar_colunas("teste.csv")
        # deve levantar ValueError, porque faltam "preco", "avaliacao" e "data_coleta"
    """
    df = pd.read_csv(caminho_csv)  # lê o CSV indicado

    for coluna in COLUNAS_OBRIGATORIAS:  # percorre cada coluna obrigatória
        if coluna not in df.columns:  # a coluna nem existe na tabela
            raise ValueError(f"Coluna obrigatória ausente: {coluna}")
        if df[coluna].isna().all():  # a coluna existe, mas está inteiramente vazia
            raise ValueError(f"Coluna obrigatória totalmente vazia: {coluna}")

    print("Validação de colunas obrigatórias: OK")
    print(f"Linhas no arquivo: {len(df)}")


if __name__ == "__main__":
    if len(sys.argv) != 2:  # o script espera exatamente um argumento: o caminho do CSV
        print("Uso: uv run exemplos/validar_colunas.py caminho/para/arquivo.csv")
        sys.exit(1)

    caminho = Path(sys.argv[1])  # pega o caminho passado na linha de comando

    if not caminho.exists():  # confere se o arquivo realmente existe antes de tentar ler
        print(f"Arquivo não encontrado: {caminho}")
        sys.exit(1)

    try:
        validar_colunas(caminho)
    except ValueError as erro:  # captura especificamente o erro de validação, não qualquer erro
        print(f"Validação falhou: {erro}")
        sys.exit(1)
