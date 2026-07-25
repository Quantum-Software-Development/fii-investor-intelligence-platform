<!-- LANGUAGE BUTTONS -->
**\[[🇧🇷 Português](SILVER_SCHEMA.md)\] \[**[🇬🇧 English](../../🇬🇧English/architecture/SILVER_SCHEMA.md)**\]**

<br><br>

## [Silver Schema — 20 Campos]()
### Investor Intelligence Platform — FIIs Brasil 🇧🇷

<br><br>

**Camada:** Silver · **Localização:** `data/silver/` · **Gerado por:** NB02

<br><br>

> ⚠️ **Correção pós-execução real:** versões anteriores desta documentação citavam 22 campos base. A execução real do pipeline (v2.0.0) confirmou **20 campos base** — `raw_html` é descartado no Silver (sem utilidade após a limpeza), o que reduz a contagem de 17 campos do Bronze menos 1 (`raw_html`) mais 4 novos campos derivados no NB02 (`source_label`, `text_clean`, `published_dt`, `word_count`, `char_count`, `has_content`) = 20. As 12 colunas de sentimento do NB05 são um enriquecimento **adicional**, aplicado por cima desses 20.

<br><br>

## [Transformações Bronze → Silver]()

<br><br>

| Transformação | UDF / Função | Detalhe |
|---|---|---|
| Limpeza de HTML | `clean_text()` | Remove tags, entidades HTML, URLs, boilerplates |
| Normalização de datas | `parse_date()` | Converte qualquer formato para ISO-8601 UTC |
| Label de fonte | `source_label()` | Domínio → nome comercial legível |
| Word count | `F.size(F.split(...))` | Número de palavras no `text_clean` |
| Char count | `F.length(...)` | Número de caracteres no `text_clean` |
| has_content flag | `word_count >= 30` | Flag boolean de qualidade mínima |

<br><br>

## [Quality Gates (NB02)]()

<br><br>

| Gate | Condição | Ação se falha |
|---|---|---|
| **G1 — Null IDs** | `article_id != null AND url != null` | Descarta registro |
| **G2 — Word Count** | `word_count >= 30` | Descarta registro |
| **G3 — Dedup** | `Window.partitionBy("article_id").orderBy(collected_at DESC)` | Mantém mais recente |

<br><br>

## [Schema Completo — 20 Campos]()

<br><br>

| # | Campo | Origem | Descrição |
|---|---|---|---|
| 1 | `article_id` | Bronze | SHA-256(url) — PK |
| 2 | `source` | Bronze | Domínio do portal |
| 3 | `source_type` | Bronze | `rss` · `scraping` · `reddit` |
| 4 | `source_label` | NB02 UDF | Nome comercial (ex: "InfoMoney") |
| 5 | `title` | Bronze | Título do artigo |
| 6 | `url` | Bronze | URL canônica |
| 7 | `author` | Bronze | Autor (nullable) |
| 8 | `published_at` | Bronze | Data original (nullable para scraping) |
| 9 | `published_dt` | NB02 UDF | ISO-8601 UTC normalizado (nullable) |
| 10 | `collected_at` | Bronze | ISO-8601 UTC da coleta |
| 11 | `language` | Bronze | `pt-br` |
| 12 | `tags` | Bronze | Tags separadas por vírgula |
| 13 | `query_used` | Bronze | FII_FILTER_TERM que ativou a coleta |
| 14 | `ingestion_method` | Bronze | Método de ingestão |
| 15 | `text_clean` | NB02 UDF | Corpo limpo — sem HTML, URLs, boilerplate |
| 16 | `word_count` | NB02 Spark | Número de palavras em `text_clean` |
| 17 | `char_count` | NB02 Spark | Número de caracteres em `text_clean` |
| 18 | `has_content` | NB02 Spark | `True` se `word_count >= 30` |
| 19 | `content_hash` | Bronze | MD5(title + content[:500]) |
| 20 | `metadata_json` | Bronze | JSON string com extras |

<br><br>

> `raw_html` é descartado no Silver — não tem utilidade após a limpeza.

<br><br>

## [Silver Enriched (NB05 adiciona 12 colunas)]()

<br><br>

Após o NB05, o Silver é enriquecido com colunas de sentimento e sinais:

<br><br>

| Campo adicional | Tipo | Descrição |
|---|---|---|
| `polarity_score` | float | Score numérico [-1.0, +1.0] pelo léxico FII PT-BR |
| `sentiment_label` | str | `positivo` · `neutro` · `negativo` |
| `n_pos_terms` | int | Número de termos positivos encontrados |
| `n_neg_terms` | int | Número de termos negativos encontrados |
| `textblob_polarity` | float | Score TextBlob fallback (nullable) |
| `flag_dividendo` | bool | Presença de termos de dividendo/provento |
| `score_dividendo` | float | Intensidade [0.0, 1.0] |
| `flag_oportunidade` | bool | Presença de termos de oportunidade/compra |
| `score_oportunidade` | float | Intensidade [0.0, 1.0] |
| `flag_risco` | bool | Presença de termos de risco/volatilidade |
| `score_risco` | float | Intensidade [0.0, 1.0] |
| `flag_crise` | bool | Presença de termos de crise/queda |

<br><br>

## [Boilerplates Removidos pela Limpeza]()

<br><br>

```python
_BOILER = [
    'leia mais', 'veja também', 'acesse aqui', 'clique aqui',
    'saiba mais', 'newsletter', 'assine já', 'você também pode'
]
```

<br><br>

## [Relatório de Processamento (`silver_processing_report.json`)]()

<br><br>

```json
{
  "timestamp": "2026-01-15T10:30:00Z",
  "bronze_records_loaded": 1500,
  "gate_1_null_ids": 1498,
  "gate_2_word_count": 1350,
  "gate_3_dedup": 1320,
  "silver_records_final": 1320,
  "has_content_true": 1320,
  "source_type_counts": {"rss": 800, "scraping": 400, "reddit": 120},
  "min_word_count_threshold": 30,
  "spark_version": "3.5.0",
  "random_seed": 42
}
```

<br><br>

## [Ver Também]()

<br><br>

- **[`BRONZE_SCHEMA.md`](BRONZE_SCHEMA.md)** — camada de origem desta transformação
- **[`GOLD_SCHEMA.md`](GOLD_SCHEMA.md)** — próxima camada, consumida a partir deste schema
- **[`SENTIMENT_METHODOLOGY.md`](../metodologia/SENTIMENT_METHODOLOGY.md)** — metodologia completa das 12 colunas de sentimento

<br><br>

---

<br><br>

*Silver Schema v1.0.0 · Investor Intelligence Platform FIIs Brasil*
