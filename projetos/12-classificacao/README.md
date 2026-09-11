README de reprodução

**Fonte e período dos dados; quantos posts entraram:**

> Fonte: Exportação do TikTok via Zeeschuimer, Aula 7. Período: 19/08/2026. Posts que entraram: 1138.

**Como você definiu "viralizou", e por quê:**

> Marquei como'viralizou' os posts com plays acima do percentil 75 da minha coleta. Desse modo, cerca de 25% dos posts será classificao como viral. Por exemplo, se fosse colocado como viral posts com plays acima do percentil 90, a quantidade de posts marcadas como viral seria extremamente baixa, ainda mais porque a coleta de posts não é tão grande. Usar o percentil 75 seria mais "justo" em uma coleta pequena como está (1138 posts), visto que o objetivo é ver posts que performaram relativamente melhor do que a maioria (nada muito exagerado), e não selecionar apenas os posts que tiveram uma performance de extrema viralização. 

**Quantos posts ficaram como "viral" (a classe é rara?):**

> Foram 285 de 1138 posts marcados como 'viralizou'(25%). A classe pode ser considerada rara, mas ao analisar o recall (0,14), ele se apresenta baixo, ou seja, o modelo classificou apenas 14% dos posts que realmente eram virais como virais, ignorando 86% dos posts que deveriam ser classficados desse modo também, gerando falsos negativos. Observando a precisão, ela mostra que em 77% das vezes que o modelo marca um post como viral, ele acerta. Ou seja, o modelo se mostra seletivo, visto que só marca viral quando tem bastante confiança naquele resultado, por isso erra pouco (23% das vezes), porém, por ser cauteloso demais, ele deixa passar a maioria dos virais de verdade (recall baixo)

**Features usadas; colunas descartadas por vazamento:**

> Features criadas: 'seguidores_autor', 'videos_autor', 'tam_legenda', 'n_emojis', 'n_hashtags', 'hora', 'dia_semana'. Colunas descartadas por vazamento: "likes", "comments", "shares" e "plays".

**Matriz de confusão do seu melhor modelo, e uma leitura: a favor de quem ele erra?** (deixa passar muitos virais = recall baixo; ou dá muito alarme falso = precisão baixa)

> A matriz de confusão da regressão logística fica assim: VN = 211 / FN = 61 / FP = 3 / VP = 10. Ele está errando a favor dos falsos negativos, ou seja, existem 61 posts que deveriam ser classificados como virais, mas não estão sendo. Isso também pode ser observado por meio do recall de 0.14, ou seja, ele está baixo, deixando passar muitos posts que deveriam estar sendo considerados como virais.

**O que mudou quando você baixou o threshold:**

> Quando abaixei o threshold a precisão tende a cair e o recall tende a aumentar, ou seja, ele começa a pegar mais posts virais (recall), mas começa a errar mais ao classificar um posts como viral (precisão)

**Declaração de uso de IA:** 

> Não usei IA nesta entrega.