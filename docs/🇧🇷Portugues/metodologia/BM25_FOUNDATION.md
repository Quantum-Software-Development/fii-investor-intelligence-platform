<!-- LANGUAGE BUTTONS -->
**\[[🇧🇷 Português](BM25_FOUNDATION.md)\] \[**[🇬🇧 English](../../🇬🇧English/methodology/BM25_FOUNDATION.md)**\]**

<br><br>

## [BM25 Foundation — Referência Matemática]()
### Investor Intelligence Platform — FIIs Brasil 🇧🇷

<br><br>

## [Visão Geral]()

<br><br>

BM25 (Best Matching 25) é o algoritmo de ranking de relevância principal usado para pontuar as 21 fontes monitoradas pela relevância do conteúdo FII.

<br><br>

## [Fórmula]()

<br><br>



$$
\huge \text{BM25}(D,Q) = \sum \text{IDF}(q_i) \cdot \frac{f(q_i,D) \cdot (k_1 + 1)}{f(q_i,D) + k_1 \cdot \left(1 - b + b \cdot \frac{|D|}{\text{avgdl}}\right)}
$$




<br><br><br><br>

| Parâmetro | Padrão | Efeito |
|---|---|---|
| k1 | 1.5 | Saturação de termo |
| b | 0.75 | Normalização por comprimento |

<br><br>

## [Papel Neste Projeto]()

<br><br>

```mermaid
%%{init:{
'theme':'dark',
'themeVariables':{
'background':'#090d13',
'primaryTextColor':'#F5F7FA',
'lineColor':'#2dd4bf'
}}}%%

graph LR

CORPUS["Corpus Silver<br/>documentos tokenizados"]:::silver

BM25L["BM25<br/>Camada 2 — ranking probabilístico"]:::gold

TFIDFL["TF-IDF<br/>Camada 1 — ponderação estatística"]:::bronze

CORPUS --> BM25L
CORPUS --> TFIDFL

classDef bronze fill:#2a1512,stroke:#a85a4a,color:#F5F7FA,stroke-width:2.5px;
classDef silver fill:#1b2430,stroke:#b0b7c3,color:#F5F7FA,stroke-width:2.5px;
classDef gold fill:#2a2208,stroke:#e6c35a,color:#F5F7FA,stroke-width:2.5px;
```

<br><br>

- **BM25** = Camada 2 — ranking probabilístico de relevância por fonte
- **TF-IDF** = Camada 1 — ponderação estatística de termos (ver [`TFIDF_FOUNDATION.md`](TFIDF_FOUNDATION.md))
- **FAISS** = Camada 3 — similaridade semântica (ver [`FAISS.md`](FAISS.md))

<br><br>

## [Justificativa de Negócio]()

<br><br>

O objetivo central da plataforma é identificar **quais fontes digitais têm maior concentração de conteúdo relevante sobre FIIs** — um problema clássico de Recuperação de Informação, para o qual o BM25 é o padrão de fato da indústria (motores de busca, sistemas documentais, pipelines de IR).

<br><br>

[***Por Que BM25 em Vez de Apenas TF-IDF***]()

<br><br>

| Critério | TF-IDF | BM25 | Embeddings (FAISS) |
|---|---|---|---|
| Interpretabilidade | Alta | Muito alta | Baixa |
| Explicabilidade (XAI) | Alta | Alta | Baixa — não decompõe por termo |
| Captura semântica (sinônimos) | Baixa | Baixa | Alta |
| Controle de saturação de termo | Fraco | Forte | N/A |
| Normalização por tamanho de documento | Limitada | Forte | N/A |
| Custo computacional | Baixo | Baixo | Mais alto (~10-50ms/query) |
| Robustez multi-fonte (estilos editoriais distintos) | Média | Alta | Alta |

<br><br>

Nenhuma das três camadas substitui as outras — por isso a plataforma combina as três em `score_hybrid_v2` (ver [`FUNDAMENTOS_CONCEITUAIS_RECUPERACAO_HIBRIDA.md`](FUNDAMENTOS_CONCEITUAIS_RECUPERACAO_HIBRIDA.md)), em vez de escolher uma única técnica.

<br><br>

[***Exemplo Interpretável (XAI)***]()

<br><br>

Diferente de modelos *black-box*, o BM25 permite justificar tecnicamente por que uma fonte foi ranqueada acima de outra:

<br><br>

> *Um portal especializado recebe score BM25 elevado porque "dividend yield" apareceu 18 vezes, "vacância" 12 vezes e "P/VP" 9 vezes no seu corpus — termos raros no restante do corpus (IDF alto) e presentes de forma consistente (não saturada) nesse portal. Um portal financeiro genérico, sem esses termos, recebe score próximo de zero.*

<br><br>

Essa capacidade de justificar cada score decompondo-o por termo é o que torna o ranqueamento auditável, e não uma caixa-preta — ver [`RESPONSIBLE_AI.md`](../governanca/RESPONSIBLE_AI.md) para o princípio de explicabilidade aplicado a toda a plataforma.

<br><br>

## [Alinhamento com XAI]()

<br><br>

Todo score BM25 se decompõe em contribuições por termo (NB05).

<br><br>

## [Referência]()

<br><br>

Robertson & Zaragoza (2009). The Probabilistic Relevance Framework: BM25 and Beyond. *Foundations and Trends in IR*, 3(4), 333–389.

<br><br>

## [Ver Também]()

<br><br>

- **[`FAISS.md`](FAISS.md)** — camada semântica que complementa BM25/TF-IDF na Camada 3
- **[`FUNDAMENTOS_CONCEITUAIS_RECUPERACAO_HIBRIDA.md`](FUNDAMENTOS_CONCEITUAIS_RECUPERACAO_HIBRIDA.md)** — enquadramento conceitual da recuperação híbrida

<br><br>

---

<br><br>

*BM25 Foundation v1.0.0 · Investor Intelligence Platform FIIs Brasil*
