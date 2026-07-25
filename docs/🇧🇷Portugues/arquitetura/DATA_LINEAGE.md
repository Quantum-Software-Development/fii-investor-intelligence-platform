<!-- LANGUAGE BUTTONS -->
**\[[🇧🇷 Português](DATA_LINEAGE.md)\] \[**[🇬🇧 English](../../🇬🇧English/architecture/DATA_LINEAGE.md)**\]**

<br><br>

## [Linhagem de Dados]()
### Investor Intelligence Platform — FIIs Brasil 🇧🇷

<br><br>

## [Fluxo de Dados de Ponta a Ponta]()

<br><br>

```mermaid
%%{init:{
'theme':'dark',
'themeVariables':{
'background':'#090d13',
'primaryTextColor':'#F5F7FA',
'lineColor':'#2dd4bf'
}}}%%

graph TD

A1["20 Portais Financeiros<br/>RSS Feeds"]:::setup
A2["Reddit (Fonte #21)<br/>r/investimentos · r/farialimabets<br/>Camada Comportamental"]:::setup

BZ["Bronze Layer<br/>data/external/<br/>Parquet bruto, 17 campos<br/>article_id já atribuído (SHA-256)"]:::bronze

S1["NB02 — Limpeza HTML<br/>Deduplicação · Validação de Schema"]:::silver
SV["Silver Layer<br/>data/silver/<br/>Parquet limpo, 20 campos"]:::silver

N1["NB03 — Word Count<br/>+ NB04 TF-IDF"]:::gold
N2["NB04 — BM25<br/>(ranking por fonte)"]:::gold
N3["NB05 — Sentimento<br/>Léxico PT-BR"]:::gold
N4["NB03 — Negative Context<br/>Detection"]:::gold
T1["NB04 — FAISS<br/>Embeddings semânticos"]:::gold

GL["Gold Layer<br/>data/gold/<br/>Parquet analítico"]:::gold

API["FastAPI<br/>Render · NB07"]:::dash
DASH["Streamlit Dashboard<br/>Streamlit Cloud · NB07"]:::dash
BOT["Chatbot RAG<br/>Groq (primário) → Gemini (fallback)"]:::llm

A1 --> BZ
A2 --> BZ
BZ --> S1 --> SV
SV --> N1 & N2 & N3 & N4 & T1
N1 & N2 & N3 & N4 & T1 --> GL
GL --> API --> DASH --> BOT
GL -.->|fallback local| DASH

classDef setup fill:#0d2137,stroke:#00d2ff,color:#F5F7FA,stroke-width:2.5px;
classDef bronze fill:#2a1512,stroke:#a85a4a,color:#F5F7FA,stroke-width:2.5px;
classDef silver fill:#1b2430,stroke:#b0b7c3,color:#F5F7FA,stroke-width:2.5px;
classDef gold fill:#2a2208,stroke:#e6c35a,color:#F5F7FA,stroke-width:2.5px;
classDef dash fill:#06363d,stroke:#2dd4bf,color:#F5F7FA,stroke-width:2.5px;
classDef llm fill:#231433,stroke:#b56cff,color:#F5F7FA,stroke-width:2.5px;
```

<br><br>

## [Especificações por Camada]()

<br><br>

| Camada | Localização | Formato | Retenção | Git |
|---|---|---|---|---|
| **Bronze** | `data/external/` | Parquet (particionado por fonte) | Duração do projeto | ✅ commitado (dataset frozen) |
| **Silver** | `data/silver/` | Parquet (partição única) | Duração do projeto | ❌ gitignored |
| **Gold** | `data/gold/` | Parquet (um arquivo por tabela) | Por execução de análise | ✅ artefatos de deploy commitados (ver [`DEPLOY_RENDER.md`](../deploy/DEPLOY_RENDER.md)) |

<br><br>

> A política de retenção segue [`LGPD_ALIGNMENT.md`](../governanca/LGPD_ALIGNMENT.md): todas as camadas exceto `data/external/` (frozen) devem ser removidas do armazenamento local ao final do projeto.

<br><br>

## [Linhagem de Transformação]()

<br><br>

[***Bronze (NB01)***]()

<br><br>

`article_id` já é atribuído no momento da ingestão — `SHA-256(url)` — e nunca muda pelas camadas seguintes. Ver [`BRONZE_SCHEMA.md`](BRONZE_SCHEMA.md) para o contrato completo de 17 campos.

<br><br>

[***Bronze → Silver (NB02)***]()

<br><br>

| Transformação | Campo de Entrada | Campo de Saída | Lógica |
|---|---|---|---|
| Limpeza de HTML | `content` | `text_clean` | BeautifulSoup + regex |
| Deduplicação | `article_id` | — | Descarta duplicatas exatas |
| Normalização de data | `published_at` (str) | `published_dt` (timestamp) | PySpark `to_timestamp` |
| Filtro de qualidade | `text_clean` | — | Descarta se `word_count < 30` |
| Word count | `text_clean` | `word_count` | `F.size(F.split(...))` |

<br><br>

[***Silver → Gold (NB03–NB05)***]()

<br><br>

| Tabela de Saída | Colunas de Origem | Algoritmo |
|---|---|---|
| `source_word_count` | `text_clean`, `source_label` | MapReduce RDD |
| `document_relevance` | `text_clean`, `source` | TF-IDF + BM25Okapi + FAISS |
| `articles_sentiment` | `text_clean`, `source` | Léxico FII PT-BR + fallback TextBlob |
| `negative_context` | `text_clean`, `source` | Co-ocorrência em janela ±5 tokens |

<br><br>

## [Trilha de Auditoria]()

<br><br>

- **A camada Bronze nunca é modificada** após a ingestão — registro bruto imutável (regra de freeze do NB01)
- **`article_id`** é determinístico (`SHA-256(url)`) — seguro para joins entre execuções do pipeline
- **`silver_processing_report.json`** e **`api_payload_summary.json`** registram: data de execução, contagens por fonte, versão do pipeline
- **`RANDOM_SEED = 42`** garante que os scores híbridos e a análise de sentimento sejam reprodutíveis entre execuções

<br><br>

## [Ver Também]()

<br><br>

- **[`MEDALLION_OVERVIEW.md`](MEDALLION_OVERVIEW.md)** — visão geral da arquitetura Bronze/Silver/Gold
- **[`BRONZE_SCHEMA.md`](BRONZE_SCHEMA.md)**, **[`SILVER_SCHEMA.md`](SILVER_SCHEMA.md)**, **[`GOLD_SCHEMA.md`](GOLD_SCHEMA.md)** — contratos completos de schema por camada
- **[`DATA_DICTIONARY.md`](DATA_DICTIONARY.md)** — taxonomia de hashtags e termos monitorados

<br><br>

---

<br><br>

*Data Lineage v2.0.0 · Investor Intelligence Platform FIIs Brasil*
