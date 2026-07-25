<!-- LANGUAGE BUTTONS -->
**\[[🇧🇷 Português](TFIDF_FOUNDATION.md)\] \[**[🇬🇧 English](../../🇬🇧English/methodology/TFIDF_FOUNDATION.md)**\]**

<br><br>

## [TF-IDF FUNDAMENTOS — Referência Matemática]()
### Investor Intelligence Platform — FIIs Brasil 🇧🇷

<br><br>

## [Visão Geral]()

<br><br>

TF-IDF (Term Frequency–Inverse Document Frequency) é a Camada 1 do motor de recuperação híbrida da plataforma — a camada estatístico-lexical que identifica quais termos são *distintivos* de um documento, em vez de apenas frequentes no corpus como um todo.

<br><br>

## [Fórmula]()

<br><br>

$$
\Huge \text{TF-IDF}(t,d) = \text{TF}(t,d) \times \log\left(\frac{N+1}{df(t)+1}\right) + 1
$$


<br><br><br>


| Variável | Significado |
|---|---|
| `TF(t,d)` | Frequência do termo `t` no documento `d` |
| `N` | Total de documentos no corpus |
| `df(t)` | Número de documentos que contêm o termo `t` |
| Suavização `+1` | Evita divisão por zero e amortece valores extremos de IDF para termos muito raros |

<br><br>

## [Por Que Só Frequência Não Basta]()

<br><br>

Um termo como *"fundo"* pode aparecer em 95% do corpus FII — alta frequência bruta, poder discriminativo quase zero (isso é exatamente o que a contagem MapReduce do NB03 revela, e exatamente a limitação que motivou adicionar esta camada). O TF-IDF penaliza termos onipresentes e valoriza termos específicos a um subconjunto menor de documentos — é isso que permite que n-gramas específicos do domínio como *"laje corporativa"* ou *"dividend yield"* apareçam acima do vocabulário financeiro genérico.

<br><br>

## [Configuração Usada]()

<br><br>

```python
TfidfVectorizer(
    ngram_range=(1, 2),
    max_features=50_000,
    sublinear_tf=True,
    min_df=2,
)
```

<br><br>

| Parâmetro | Valor | Efeito |
|---|---|---|
| `ngram_range` | `(1, 2)` | Captura tanto palavras isoladas quanto expressões de 2 palavras (ex: *"dividend yield"*, não só *"dividend"* e *"yield"* separados) |
| `max_features` | `50.000` | Limita o tamanho do vocabulário por eficiência de memória nesta escala de corpus |
| `sublinear_tf` | `True` | Usa `1 + log(TF)` em vez de TF bruto — reduz o impacto de repetição extrema dentro de um único documento |
| `min_df` | `2` | Descarta termos que aparecem em apenas 1 documento — remove erros de digitação e ruído isolado |

<br><br>

## [Papel no Pipeline]()

<br><br>

- O `NB04` treina o vetorizador uma vez sobre o corpus Silver completo, persistindo `tfidf_vectorizer.pkl` e `tfidf_matrix.npz`
- A relevância em tempo de query usa similaridade coseno entre o vetor da query e o vetor de cada documento
- Peso no `score_hybrid_v2`: **20%** — o menor das três camadas, porque a força do TF-IDF (revelar n-gramas raros e específicos) é complementar, não substituta, ao ranking probabilístico do BM25 e ao matching semântico do FAISS

<br><br>

## [Fórmula do Score Híbrido]()

<br><br>



<h2 align="center">
  $\text{score\_hybrid\_v2} = 0.20 \times \text{TF-IDF}_{\text{norm}} + 0.30 \times \text{BM25}_{\text{norm}} + 0.50 \times \text{Semantic}_{\text{norm}}$
</h2>



<br><br><br>

## [TF-IDF vs. BM25 — Por Que Não Parar no TF-IDF]()

<br><br>

| Limitação do TF-IDF isolado | Como o BM25 (Camada 2) corrige |
|---|---|
| Sem normalização por comprimento de documento — artigos longos podem dominar só por terem mais termos | BM25 normaliza explicitamente por `\|D\|/avgdl` |
| Contribuição da frequência de termo cresce quase linearmente (mesmo com `sublinear_tf`) | A curva de saturação `k1` do BM25 limita o valor marginal de termos repetidos |
| Trata toda posição do corpus como igualmente comparável | BM25 foi projetado especificamente para ranking sob um framework de relevância probabilística |

<br><br>

Por isso a plataforma não para no TF-IDF isolado — ver [`BM25_FOUNDATION.md`](BM25_FOUNDATION.md) para a camada que endereça diretamente essas lacunas, e [`FAISS.md`](FAISS.md) para a camada semântica que vai além do matching lexical por completo.

<br><br>

## [Alinhamento com XAI]()

<br><br>

O TF-IDF é totalmente decomponível: para qualquer documento, os termos de maior contribuição e seus pesos individuais podem ser listados diretamente a partir do vetorizador treinado e do vetor esparso do documento — nenhuma etapa de caixa-preta está envolvida. Ver [`RESPONSIBLE_AI.md`](../governanca/RESPONSIBLE_AI.md), seção 2, para o código exato de decomposição usado neste projeto.

<br><br>

## [Referência]()

<br><br>

Manning, C. D., Raghavan, P., & Schütze, H. (2008). *Introduction to Information Retrieval*. Cambridge University Press.

<br><br>

## [Ver Também]()

<br><br>

- **[`BM25_FOUNDATION.md`](BM25_FOUNDATION.md)** — Camada 2, a camada de ranking probabilístico que se constrói sobre esta
- **[`FAISS.md`](FAISS.md)** — Camada 3, a camada semântica
- **[`FUNDAMENTOS_CONCEITUAIS_RECUPERACAO_HIBRIDA.md`](FUNDAMENTOS_CONCEITUAIS_RECUPERACAO_HIBRIDA.md)** — enquadramento conceitual mais amplo da arquitetura em 3 camadas

<br><br>

---

<br><br>

*TF-IDF Foundation v1.0.0 · Investor Intelligence Platform FIIs Brasil*
