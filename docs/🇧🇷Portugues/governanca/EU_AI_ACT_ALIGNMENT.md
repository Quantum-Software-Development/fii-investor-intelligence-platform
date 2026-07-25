<!-- LANGUAGE BUTTONS -->
**\[[🇧🇷 Português](EU_AI_ACT_ALIGNMENT.md)\] \[**[🇬🇧 English](../../🇬🇧English/governance/EU_AI_ACT_ALIGNMENT.md)**\]**

<br><br>

## [EU AI Act — Alinhamento e Classificação]()
### Investor Intelligence Platform — FIIs Brasil 🇧🇷

<br><br>

**Regulamento (UE) 2024/1689 do Parlamento Europeu e do Conselho**

<br><br>

## [Classificação do Sistema]()

<br><br>

**Categoria de risco: MÍNIMO (Art. 6º — Sistemas não de alto risco)**

<br><br>

| Critério de Alto Risco | Aplicável? | Justificativa |
|---|---|---|
| Infraestrutura crítica | ❌ | Sistema analítico acadêmico |
| Decisões de crédito ou financiamento | ❌ | Não emite decisões de crédito |
| Emprego e gestão de trabalhadores | ❌ | Fora do escopo |
| Serviços públicos essenciais | ❌ | Fora do escopo |
| Aplicação da lei | ❌ | Fora do escopo |
| Migração e controle de fronteiras | ❌ | Fora do escopo |
| Administração da justiça | ❌ | Fora do escopo |
| Biometria e reconhecimento facial | ❌ | Não coletado |

<br><br>

**Classificação final:** Sistema de IA de **risco mínimo** — plataforma analítica e informacional.

<br><br>

## [Obrigações Aplicáveis a Sistemas de Risco Mínimo]()

<br><br>

Embora sem obrigações compulsórias para risco mínimo, adotamos voluntariamente boas práticas:

<br><br>

| Prática Voluntária | Implementação |
|---|---|
| Transparência para usuários | Disclaimer em todos os outputs do chatbot, independente do motor (Groq ou Gemini) |
| Documentação técnica | Este documento + [`RESPONSIBLE_AI.md`](RESPONSIBLE_AI.md) + [`CRISP_DM_MAPPING.md`](../metodologia/CRISP_DM_MAPPING.md) |
| Supervisão humana | Pipeline manual — nenhuma ação autônoma |
| Gestão de qualidade | Quality gates NB02 + logging estruturado |
| Data lineage | `source`, `ingestion_method`, `article_id` preservados |

<br><br>

## [Disclaimer Obrigatório no Chatbot (Art. 52, EU AI Act)]()

<br><br>

Todo output do chatbot — gerado pelo motor primário Groq ou pelo motor de fallback Gemini — inclui:

<br><br>

```python
DISCLAIMER = (
    "Esta análise é gerada por IA com base em dados públicos. "
    "Não constitui recomendação de investimento. "
    "Consulte um assessor financeiro certificado antes de tomar decisões."
)
```

<br><br>

> O disclaimer é injetado programaticamente na camada de serviço, não depende de nenhum dos dois LLMs "lembrar" de incluí-lo — ver [`MULTI_LLM_FALLBACK.md`](../arquitetura/MULTI_LLM_FALLBACK.md).

<br><br>

## [Uso Geral vs Uso Específico]()

<br><br>

**Este sistema NÃO é um GPAI (General Purpose AI Model)** conforme Art. 3(63):

<br><br>

- Não é um modelo de fundação (foundation model)
- Não é distribuído comercialmente para múltiplos propósitos
- É uma pipeline analítica especializada com domínio e propósito definidos
- Os LLMs consumidos (Groq, Gemini) são utilizados via API de terceiros, como componente de uma pipeline RAG com escopo restrito — não como modelo de propósito geral oferecido pela plataforma

<br><br>

## [Documentação Técnica (Art. 11 — Voluntária)]()

<br><br>

| Documento | Localização |
|---|---|
| Descrição do sistema | [`DOCUMENTO_OFICIAL.md`](../documento_oficial/DOCUMENTO_OFICIAL.md) |
| Metodologia CRISP-DM | [`CRISP_DM_MAPPING.md`](../metodologia/CRISP_DM_MAPPING.md) |
| Schema de dados | [`BRONZE_SCHEMA.md`](../arquitetura/BRONZE_SCHEMA.md) + [`SILVER_SCHEMA.md`](../arquitetura/SILVER_SCHEMA.md) + [`GOLD_SCHEMA.md`](../arquitetura/GOLD_SCHEMA.md) |
| Linhagem de dados | [`DATA_LINEAGE.md`](../arquitetura/DATA_LINEAGE.md) |
| Métricas de qualidade | `data/silver/silver_processing_report.json` |
| Léxico de sentimento | [`SENTIMENT_METHODOLOGY.md`](../metodologia/SENTIMENT_METHODOLOGY.md) |
| Fundação BM25 / TF-IDF / FAISS | [`BM25_FOUNDATION.md`](../metodologia/BM25_FOUNDATION.md), [`TFIDF_FOUNDATION.md`](../metodologia/TFIDF_FOUNDATION.md), [`FAISS.md`](../metodologia/FAISS.md) |
| Alinhamento LGPD | [`LGPD_ALIGNMENT.md`](LGPD_ALIGNMENT.md) |
| IA Responsável | [`RESPONSIBLE_AI.md`](RESPONSIBLE_AI.md) |
| Registro de riscos | [`RISK_REGISTER.md`](RISK_REGISTER.md) |

<br><br>

---

<br><br>

*EU AI Act Alignment v1.0.0 · Investor Intelligence Platform FIIs Brasil*
