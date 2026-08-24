**Fonte (nome da página e URL):**

> Books to Scrape - http://books.toscrape.com/catalogue/category/books/classics_6/index.html

**Tag/classe/id usados no `.find()` / `.find_all()` para extrair os dados:**

> item.find("h3").find("a")["title"]
> item.find("p", {"class": "price_color"})
> item.find("p", class_="instock")

**Data e hora da coleta:**

> 21/08/2026, 21:21 - 22:33

**Falhas encontradas durante a coleta (status diferente de 200, busca que não bateu de primeira, item sem algum campo, etc.) e como foram resolvidas:**

> Na primeira montagem do csv não estava vindo a informação se o livro estava ou não em estoque, foi resolvido com uso de IA para entender o que estava dando errado. Além disso, na mesma tag do título do livro está o link dele, então antes estava vindo o "href" e não o "title", foi resolvido relendo o código e a aba de inspecionar da página.

**Declaração de uso de IA:** Claude AI, utilizada na parte 4 da entrega. O código foi alterado para "estoque_livro = item.find("p", class_="instock").get_text(strip=True)"
