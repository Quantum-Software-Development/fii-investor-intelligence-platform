<!-- LANGUAGE BUTTONS -->
**\[[🇧🇷 Português](GOLD_SCHEMA.md)\] \[**[🇬🇧 English](../../🇬🇧English/architecture/GOLD_SCHEMA.md)**\]**

<br><br>

## [Gold Layer Schema — Datasets Analíticos]()
### Investor Intelligence Platform — FIIs Brasil 🇧🇷

<br><br>

**Camada:** Gold · **Localização:** `data/gold/` · **Gerado por:** NB03–NB07

<br><br>

## [Visão Geral dos Subdiretórios]()

<br><br>

```
data/gold/
├── word_count/               ← NB03: MapReduce
├── tfidf_bm25/                ← NB04: Índices de busca (TF-IDF + BM25 + FAISS)
├── sentiment/                 ← NB05: Análise de sentimento
├── marketing_intelligence/    ← NB06: MI por FII
└── dashboard/                 ← NB07: Datasets prontos para consumo
```

<br><br>

## [1. Word Count (`data/gold/word_count/`)]()

<br><br>

[***`global_word_count.parquet`***]()

<br><br>

| Campo | Tipo | Descrição |
|---|---|---|
| `term` | str | Token normalizado (NFD, lowercase) |
| `count` | int | Frequência total no corpus |
| `rank` | int | Posição no ranking global (1 = mais frequente) |

<br><br>

[***`source_word_count.parquet`***]()

<br><br>

| Campo | Tipo | Descrição |
|---|---|---|
| `source_label` | str | Nome comercial da fonte |
| `term` | str | Token normalizado |
| `count` | int | Frequência nesta fonte |

<br><br>

[***`tofu_frequency.parquet`***]()

<br><br>

| Campo | Tipo | Descrição |
|---|---|---|
| `term` | str | Termo TOFU do léxico de marketing |
| `count` | int | Frequência global |
| `rank` | int | Rank global |
| `tofu_rank` | int | Rank dentro do vocabulário TOFU |
| `n_sources` | int | Número de fontes em que aparece |

<br><br>

[***`negative_context.parquet`***]()

<br><br>

| Campo | Tipo | Descrição |
|---|---|---|
| `term` | str | Termo de risco monitorado |
| `global_count` | int | Frequência total no corpus |
| `negative_ctx_ratio` | float | Razão de co-ocorrência com palavras negativas (janela ±5) |
| `risk_level` | str | `high` · `medium` · `low` |
| `n_docs_with_term` | int | Número de documentos contendo o termo |

<br><br>

## [2. TF-IDF + BM25 + FAISS (`data/gold/tfidf_bm25/`)]()

<br><br>

[***`tfidf_vectorizer.pkl` (pickle)***]()

<br><br>

Objeto `sklearn.TfidfVectorizer` treinado. `ngram_range=(1,2)` · `max_features=50_000` · `sublinear_tf=True` · `min_df=2`

<br><br>

[***`tfidf_matrix.npz` (scipy sparse)***]()

<br><br>

Matriz TF-IDF: shape `(N_docs × V_vocab)`. Formato CSR comprimido.

<br><br>

[***`bm25_index.pkl` (pickle)***]()

<br><br>

Objeto `rank_bm25.BM25Okapi` treinado. `k1=1.5` · `b=0.75`.

<br><br>

[***`corpus_tokens.pkl` (pickle)***]()

<br><br>

`List[List[str]]` — corpus tokenizado. Necessário para reconstrução/busca BM25.

<br><br>

[***`embeddings.npy` + `faiss_index.faiss` (Camada 3, opcional)***]()

<br><br>

Embeddings `float32[N × 384]` (`paraphrase-multilingual-MiniLM-L12-v2`) e índice `faiss.IndexFlatIP` persistido. Gerados apenas se `ENABLE_SEMANTIC_SEARCH=true` e o download do modelo tiver sucesso — ver [`FAISS.md`](../metodologia/FAISS.md).

<br><br>

[***`doc_index_map.parquet`***]()

<br><br>

| Campo | Tipo | Descrição |
|---|---|---|
| `doc_index` | int | Índice posicional no corpus (0-based) |
| `article_id` | str | SHA-256 — FK para Silver |
| `source` | str | Domínio da fonte |
| `title` | str | Título do artigo |

<br><br>

[***`document_relevance.parquet`***]()

<br><br>

| Campo | Tipo | Descrição |
|---|---|---|
| `query` | str | Query de busca usada |
| `query_index` | int | Índice da query na lista de queries predefinidas |
| `rank` | int | Posição no ranking para esta query |
| `article_id` | str | FK para Silver |
| `source` | str | Fonte do artigo |
| `title` | str | Título |
| `score_tfidf` | float | Score coseno TF-IDF [0.0, 1.0] |
| `score_bm25` | float | Score BM25 bruto |
| `score_semantic` | float | Score coseno FAISS [0.0, 1.0] — `null` se Camada 3 indisponível |
| `score_hybrid` | float | `score_hybrid_v2` (3 camadas) ou `score_hybrid_v1` (fallback 2 camadas) — ver [`ARQUITETURA.md`](ARQUITETURA.md) |

<br><br>

## [3. Sentiment (`data/gold/sentiment/`)]()

<br><br>

[***`articles_sentiment.parquet`***]()

<br><br>

| Campo | Tipo | Descrição |
|---|---|---|
| `article_id` | str | FK para Silver |
| `source` | str | Fonte |
| `source_type` | str | Tipo de fonte |
| `source_label` | str | Nome comercial |
| `title` | str | Título |
| `url` | str | URL |
| `published_dt` | str | Data normalizada |
| `collected_at` | str | Data de coleta |
| `polarity_score` | float | Score [-1.0, +1.0] pelo léxico FII PT-BR |
| `sentiment_label` | str | `positivo` · `neutro` · `negativo` |
| `n_pos_terms` | int | Termos positivos encontrados |
| `n_neg_terms` | int | Termos negativos encontrados |
| `flag_dividendo` | bool | Sinal de dividendo/provento presente |
| `flag_oportunidade` | bool | Sinal de oportunidade/compra presente |
| `flag_risco` | bool | Sinal de risco presente |
| `flag_crise` | bool | Sinal de crise/queda presente |
| `flag_vacancia` | bool | Sinal de vacância presente |
| `flag_inadimplencia` | bool | Sinal de inadimplência presente |
| `score_dividendo` | float | Intensidade [0.0, 1.0] |
| `score_oportunidade` | float | Intensidade [0.0, 1.0] |
| `score_risco` | float | Intensidade [0.0, 1.0] |
| `score_crise` | float | Intensidade [0.0, 1.0] |

<br><br>

[***`sentiment_by_source.parquet`***]()

<br><br>

| Campo | Tipo | Descrição |
|---|---|---|
| `source_label` | str | Nome comercial da fonte |
| `n_articles` | int | Total de artigos nesta fonte |
| `avg_polarity` | float | Média de `polarity_score` |
| `pct_positivo` | float | % de artigos positivos |
| `pct_negativo` | float | % de artigos negativos |
| `pct_neutro` | float | % de artigos neutros |
| `n_dividendo` | int | Artigos com `flag_dividendo=True` |
| `n_risco` | int | Artigos com `flag_risco=True` |
| `n_crise` | int | Artigos com `flag_crise=True` |

<br><br>

[***`sentiment_by_month.parquet`***]()

<br><br>

| Campo | Tipo | Descrição |
|---|---|---|
| `pub_month` | str | Mês de publicação (Period "YYYY-MM") |
| `n_articles` | int | Total de artigos neste mês |
| `avg_polarity` | float | Média de `polarity_score` |
| `pct_pos` | float | % positivos |
| `pct_neg` | float | % negativos |

<br><br>

## [4. Marketing Intelligence (`data/gold/marketing_intelligence/`)]()

<br><br>

[***`mi_signals.parquet`***]()

<br><br>

| Campo | Tipo | Descrição |
|---|---|---|
| `ticker` | str | Código B3 do FII (ex: `HGLG11`) |
| `full_name` | str | Nome completo do fundo |
| `segment` | str | Segmento: `logistica` · `shopping` · `laje` · `papel` · `hibrido` · `varejo` |
| `mentions` | int | Total de documentos relevantes |
| `sentiment_avg` | float | Média de `polarity_score` nos docs relevantes |
| `relevance_avg` | float | Média de `score_hybrid` |
| `pct_positivo` | float | % docs positivos |
| `pct_negativo` | float | % docs negativos |
| `n_dividendo` | int | Docs com `flag_dividendo=True` |
| `n_oportunidade` | int | Docs com `flag_oportunidade=True` |
| `n_risco` | int | Docs com `flag_risco=True` |
| `n_crise` | int | Docs com `flag_crise=True` |
| `n_vacancia` | int | Docs com `flag_vacancia=True` |
| `n_inadimplencia` | int | Docs com `flag_inadimplencia=True` |
| `risk_score` | float | `(n_risco + 2·n_crise + 2·n_vacancia + 2·n_inadimpl) / mentions` |
| `opportunity_score` | float | `(n_dividendo + n_oportunidade) / mentions` |
| `mi_score` | float | `0.5·relevance + 0.3·\|sentiment\| + 0.2·opportunity` |

<br><br>

[***`mi_top_articles.parquet`***]()

<br><br>

| Campo | Tipo | Descrição |
|---|---|---|
| `ticker` | str | Código B3 |
| `rank` | int | Posição no top-10 deste FII |
| `article_id` | str | FK para Silver |
| `title` | str | Título |
| `url` | str | URL |
| `source` | str | Fonte |
| `published_dt` | str | Data normalizada |
| `sentiment_label` | str | Sentimento |
| `polarity_score` | float | Score de polaridade |
| `score_bm25` | float | Score BM25 |
| `score_tfidf` | float | Score TF-IDF |
| `score_hybrid` | float | Score híbrido |
| `mi_article_score` | float | `0.5·hybrid + 0.3·\|polarity\| + 0.2·flag_dividendo` |
| `flag_dividendo` | bool | Flag de dividendo |
| `flag_risco` | bool | Flag de risco |
| `flag_crise` | bool | Flag de crise |

<br><br>

[***`mi_funnel.parquet`***]()

<br><br>

| Campo | Tipo | Descrição |
|---|---|---|
| `stage` | str | `TOFU` · `MOFU` · `BOFU` |
| `query` | str | Query de referência usada |
| `article_id` | str | FK para Silver |
| `source` | str | Fonte |
| `source_type` | str | Tipo |
| `score_hybrid` | float | Relevância híbrida |
| `sentiment_label` | str | Sentimento |
| `polarity_score` | float | Score de polaridade |
| `flag_dividendo` | bool | Flag de dividendo |
| `flag_risco` | bool | Flag de risco |

<br><br>

[***`mi_source_ranking.parquet`***]()

<br><br>

| Campo | Tipo | Descrição |
|---|---|---|
| `source` | str | Domínio da fonte |
| `n_articles` | int | Artigos nos top-10 de qualquer FII |
| `avg_relevance` | float | Relevância média `score_hybrid` |
| `avg_polarity` | float | Polaridade média |
| `n_dividendo` | int | Artigos com flag_dividendo |
| `n_risco` | int | Artigos com flag_risco |
| `source_mi_score` | float | `0.5·avg_relevance + 0.3·\|avg_polarity\|` |

<br><br>

## [5. Dashboard (`data/gold/dashboard/`)]()

<br><br>

[***`dashboard_articles.parquet` + `.csv`***]()

<br><br>

Catálogo completo de artigos com TODOS os scores consolidados. Colunas: union de Silver + sentimento + MI scores. **Tabela central consultada por FastAPI e Streamlit.**

<br><br>

[***`dashboard_fii_signals.parquet` + `.csv`***]()

<br><br>

Uma linha por FII. Métricas consolidadas + `sentiment_trend` normalizado [0,1].

<br><br>

[***`dashboard_source_stats.parquet` + `.csv`***]()

<br><br>

Uma linha por fonte. Stats de volume, sentimento e sinais por portal.

<br><br>

[***`dashboard_funnel_stats.parquet` + `.csv`***]()

<br><br>

Uma linha por estágio TOFU/MOFU/BOFU. Volumetria e sentimento médio.

<br><br>

[***`dashboard_word_cloud.parquet` + `.csv`***]()

<br><br>

Top 200 termos. Campos: `term`, `count`, `freq_normalized`, `is_tofu`.

<br><br>

[***`api_payload_summary.json`***]()

<br><br>

Resumo estruturado para FastAPI `/health` e cache de primeiro carregamento.

<br><br>

```json
{
  "generated_at": "2026-01-15T10:30:00Z",
  "pipeline_version": "1.0.0",
  "random_seed": 42,
  "totals": { "articles": 1320, "sources": 21, "fii_entities": 15 },
  "sentiment_distribution": { "neutro": 680, "positivo": 420, "negativo": 220 },
  "top_sources": [...],
  "top_fii_by_mi_score": [...],
  "source_types": { "rss": 800, "scraping": 400, "reddit": 120 },
  "data_paths": { ... }
}
```

<br><br>

## [Ver Também]()

<br><br>

- **[`SILVER_SCHEMA.md`](SILVER_SCHEMA.md)** — camada de origem consumida por NB03–NB05
- **[`BM25_FOUNDATION.md`](../metodologia/BM25_FOUNDATION.md)**, **[`FAISS.md`](../metodologia/FAISS.md)** — fundação matemática dos índices em `tfidf_bm25/`
- **[`SENTIMENT_METHODOLOGY.md`](../metodologia/SENTIMENT_METHODOLOGY.md)** — léxico completo por trás de `sentiment/`

<br><br>

---

<br><br>

*Gold Layer Schema v1.0.0 · Investor Intelligence Platform FIIs Brasil*
