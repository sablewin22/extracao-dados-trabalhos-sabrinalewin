README de reprodução

**Fonte e período dos dados:**

> Fonte: Exportação do TikTok via Zeeschuimer, Aula 7. Período: 19/08/2026

**Quantos posts entraram no modelo (depois de remover duplicata e `plays` = 0):**

> 1138 posts

**Quais features você usou, e por quê:**

> Features criadas: 'seguidores_autor', 'videos_autor', 'tam_legenda', 'n_emojis', 'n_hashtags', 'hora', 'dia_semana'. Foram utilizadas essas features, pois mesmo elas não conseguindo provar exatamente qual seria a taxa de engajamento de um post, elas conseguem chegar em uma média muito boa de qual seria aquela taxa, analisando outros posts que obteram valores parecidos nessas variáveis. Além disso, não seria ideal usar "likes", "comments", "shares" e "plays", pois eles são diretamente utilizados para fazer o cálculo do engajamento médio, ou seja, você não estaria prevendo nada pois você já teria informado os números para fazer o cálculo exato do engajamento, isto é, não seria uma previsão.

**Quais colunas você deixou de fora por vazamento, e por quê:**

> As colunas "likes", "comments", "shares" e "plays", pois elas são diretamente utilizadas para fazer o cálculo do engajamento médio, ou seja, você não estaria prevendo nada pois você já teria informado os números para fazer o cálculo exato do engajamento, isto é, não seria uma previsão.

**Resultado: MAE e R² do modelo bobo, da linear e da árvore. O seu melhor modelo bateu o bobo?**

> Modelo bobo:  MAE = 0.0324   R2 = -0.000 / Regressão linear:   MAE = 0.0330   R2 = -0.007 / Árvore (prof. 5):   MAE = 0.0323   R2 = -0.295. Neste caso, o melhor MAE alcançado foi o da Árvore, com uma diferença de 0.001 (muito pequena) para o modelo bobo. Já no R2, o melhor continuou sendo o do modelo bobo, visto que o dos algoritmos testados deu um resultado negativo mais alto.

**Uma leitura de coeficiente (associação, não causa):**

> Nesta coleta, o modelo encontrou que posts de autores com mais seguidores e que possuiam mais hashtags tiveram uma taxa de engajamento maior. Isso é uma associação nos meus dados, não quer dizer que ganhar mais seguidores ou usar mais hahstags sempre aumentará o engajamento.".

**Declaração de uso de IA:** 
> Não usei IA nesta entrega.