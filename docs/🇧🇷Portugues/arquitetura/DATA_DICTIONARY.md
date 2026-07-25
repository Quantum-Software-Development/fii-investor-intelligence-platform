<!-- LANGUAGE BUTTONS -->
**\[[🇧🇷 Português](DATA_DICTIONARY.md)\] \[**[🇬🇧 English](../../🇬🇧English/architecture/DATA_DICTIONARY.md)**\]**

<br><br>

## [Dicionário de Dados — Referência Rápida]()
### Investor Intelligence Platform — FIIs Brasil 🇧🇷

<br><br>

> Este documento é um índice de consulta rápida. Os contratos de schema completos e autoritativos por camada estão em [`BRONZE_SCHEMA.md`](BRONZE_SCHEMA.md), [`SILVER_SCHEMA.md`](SILVER_SCHEMA.md) e [`GOLD_SCHEMA.md`](GOLD_SCHEMA.md) — este dicionário não os duplica, apenas aponta para eles e documenta a taxonomia de termos monitorados, que não tem outro lar no projeto.

<br><br>

## [Índice de Schemas por Camada]()

<br><br>

| Camada | Campos | Documento |
|---|---|---|
| Bronze | 17 campos fixos | [`BRONZE_SCHEMA.md`](BRONZE_SCHEMA.md) |
| Silver | 20 campos base + 12 de sentimento (NB05) | [`SILVER_SCHEMA.md`](SILVER_SCHEMA.md) |
| Gold | 5 subdiretórios, ~15 tabelas | [`GOLD_SCHEMA.md`](GOLD_SCHEMA.md) |

<br><br>

## [Taxonomia NLP — Hashtags Monitoradas]()

<br><br>

Usadas como filtros semânticos, termos de expansão de query no BM25/TF-IDF, e âncoras auxiliares na etapa de coleta (NB01):

<br><br>

```
#FII #FIIs #FundosImobiliarios #RendaPassiva #Dividendos #Investimentos
#MercadoFinanceiro #DividendYield #CarteiraDeInvestimentos #Investidor
#PassiveIncome #BolsaDeValores #B3 #Fundos #Investing
#InvestimentoInteligente #Financeiro #Mercado #Acoes #EducacaoFinanceira
```

<br><br>

> Esta lista complementa, mas não substitui, o vocabulário TOFU usado no MapReduce (ver [`MAPREDUCE_PATTERN.md`](../metodologia/MAPREDUCE_PATTERN.md)) e o léxico de sentimento (ver [`SENTIMENT_METHODOLOGY.md`](../metodologia/SENTIMENT_METHODOLOGY.md)) — são três vocabulários com propósitos distintos: hashtags para filtragem/expansão de busca, termos TOFU para análise de frequência de marketing, léxico de sentimento para polaridade.

<br><br>

## [Ver Também]()

<br><br>

- **[`BRONZE_SCHEMA.md`](BRONZE_SCHEMA.md)**, **[`SILVER_SCHEMA.md`](SILVER_SCHEMA.md)**, **[`GOLD_SCHEMA.md`](GOLD_SCHEMA.md)** — contratos de schema completos
- **[`DATA_LINEAGE.md`](DATA_LINEAGE.md)** — como os dados fluem entre as camadas acima
- **[`MAPREDUCE_PATTERN.md`](../metodologia/MAPREDUCE_PATTERN.md)** — vocabulário TOFU usado na análise de frequência

<br><br>

---

<br><br>

*Data Dictionary v2.0.0 · Investor Intelligence Platform FIIs Brasil*
