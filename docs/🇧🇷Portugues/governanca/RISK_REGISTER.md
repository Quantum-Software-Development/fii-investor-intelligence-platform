<!-- LANGUAGE BUTTONS -->
**\[[🇧🇷 Português](RISK_REGISTER.md)\] \[**[🇬🇧 English](../../🇬🇧English/governance/RISK_REGISTER.md)**\]**

<br><br>

## [Registro de Riscos]()
### Investor Intelligence Platform — FIIs Brasil 🇧🇷

<br><br>

> Avaliação de riscos para o projeto acadêmico e para o deploy em produção.

<br><br>

## [Matriz de Riscos]()

<br><br>

| ID | Risco | Categoria | Probabilidade | Impacto | Severidade | Mitigação |
|---|---|---|---|---|---|---|
| R01 | Scraping bloqueado durante demonstração | Técnico | Média | Alto | 🔴 Alto | Dataset congelado em `data/external/` |
| R02 | API do Reddit indisponível | Técnico | Alta | Baixo | 🟡 Médio | Reddit é a Camada Comportamental (Fonte #21); o pipeline funciona sem ela, com fallback em 3 níveis |
| R03 | Indisponibilidade do Render (API) | Deploy | Baixa | Alto | 🟡 Médio | Dashboard em modo duplo: fallback para Parquet Gold local |
| R04 | Rate-limit do provedor de LLM excedido | Técnico | Baixa | Médio | 🟢 Baixo | Fallback automático Groq → Gemini (não apenas retry) — ver [`MULTI_LLM_FALLBACK.md`](../arquitetura/MULTI_LLM_FALLBACK.md); disclaimer permanece exibido mesmo em modo demo |
| R05 | Acurácia de sentimento ~75-80% PT-BR | Modelo | Certa | Médio | 🟡 Médio | Léxico FII PT-BR customizado + fallback TextBlob; limitações documentadas em [`SENTIMENT_METHODOLOGY.md`](../metodologia/SENTIMENT_METHODOLOGY.md) |
| R06 | BM25 perde sinônimos semânticos | Modelo | Média | Baixo | 🟢 Baixo | Mitigado pela Camada 3 (FAISS + embeddings) no retrieval híbrido — ver [`FAISS.md`](../metodologia/FAISS.md) |
| R07 | Viés de seleção de fontes | Dados | Média | Médio | 🟡 Médio | 21 fontes curadas e documentadas; viés divulgado em [`RESPONSIBLE_AI.md`](RESPONSIBLE_AI.md) |
| R08 | `GROQ_API_KEY` / `GEMINI_API_KEY` expostas | Segurança | Baixa | Crítico | 🔴 Alto | `st.secrets` (Streamlit) / Environment Variables (Render) + `.gitignore` obrigatório |
| R09 | Deriva temporal (dataset desatualizado) | Dados | Alta | Baixo | 🟢 Baixo | Dataset congelado rotulado com data de coleta; atualização manual via `workflow_dispatch` |
| R10 | Instabilidade do score híbrido entre execuções | Modelo | Média | Baixo | 🟢 Baixo | `RANDOM_SEED=42` + corpus congelado por execução |
| R11 | Má interpretação financeira pelos usuários | Ético | Média | Alto | 🔴 Alto | Disclaimer obrigatório; enquadramento educacional |
| R12 | Exposição de PII em dados coletados | Privacidade | Baixa | Crítico | 🔴 Alto | Apenas dados públicos; campo `author` removível sob demanda — ver [`LGPD_ALIGNMENT.md`](LGPD_ALIGNMENT.md) |
| R13 | Cold start do Render (spin-down) durante avaliação ao vivo | Deploy | Alta | Baixo | 🟢 Baixo | ~30-50s na primeira requisição após inatividade; aceitável para demo acadêmica — ver [`DEPLOY_RENDER.md`](../deploy/DEPLOY_RENDER.md) |

<br><br>

## [Definições de Severidade]()

<br><br>

| Nível | Probabilidade × Impacto |
|---|---|
| 🔴 **Alto** | Requer mitigação imediata |
| 🟡 **Médio** | Gerenciado com controles documentados |
| 🟢 **Baixo** | Risco residual aceitável |

<br><br>

## [R08 — Exposição de Secrets: Mitigação Detalhada]()

<br><br>

```python
# Padrão obrigatório de carregamento (dashboard/chatbot/groq_client.py)
import os, streamlit as st

def get_api_key(name: str) -> str:
    try:
        return st.secrets[name]
    except Exception:
        key = os.getenv(name)
        if not key:
            raise EnvironmentError(f"{name} não configurada")
        return key

groq_key = get_api_key("GROQ_API_KEY")
gemini_key = get_api_key("GEMINI_API_KEY")  # opcional — fallback
```

<br><br>

**Controles:**

<br><br>

- `.streamlit/secrets.toml` no `.gitignore`
- `.env` no `.gitignore`
- `secrets.toml.example` commitado (apenas template)
- No Render: `GROQ_API_KEY` e `GEMINI_API_KEY` configuradas como Environment Variables com `sync: false` no `render.yaml` — nunca commitadas

<br><br>

## [R04 — Rate-Limit de LLM: Por Que Fallback e Não Apenas Retry]()

<br><br>

A mitigação deste risco evoluiu de um simples retry para um **fallback automático entre dois provedores independentes** (Groq → Gemini), porque um retry sozinho não resolve rate-limit sustentado — se o Groq está limitado, tentar de novo no mesmo provedor apenas atrasa a resposta sem eliminar a causa. A arquitetura de fallback elimina o ponto único de falha sem custo adicional (ambos os tiers são gratuitos). Justificativa completa da decisão, incluindo alternativas descartadas (OpenRouter), em [`MULTI_LLM_FALLBACK.md`](../arquitetura/MULTI_LLM_FALLBACK.md).

<br><br>

## [R11 — Má Interpretação Financeira: Salvaguardas Éticas]()

<br><br>

Todos os componentes voltados ao usuário incluem:

<br><br>

1. **Aviso no cabeçalho do dashboard** (Streamlit)
2. **Restrição no system prompt do chatbot** (Groq e Gemini)
3. **Disclaimer por resposta** (anexado automaticamente, independente do motor)
4. **Disclaimer no README** (ponto de entrada do repositório)
5. **Seção de Governança em [`RESPONSIBLE_AI.md`](RESPONSIBLE_AI.md)** (documentação acadêmica)

<br><br>

## [Riscos Abertos (Aceitos)]()

<br><br>

| Risco | Justificativa para Aceitação |
<br>
|---|---|
| Limitações do léxico PT-BR + TextBlob | Nenhum dataset FII rotulado disponível; mitigação em 2 camadas suficiente para o escopo acadêmico |
| Limitações lexicais do BM25 | Mitigado pela Camada 3 (FAISS) do retrieval híbrido, já implementada |
| Desatualização temporal do dataset | Re-executar NB01 para atualizar; dataset congelado é rotulado com data de coleta |

<br><br>

## [Ver Também]()

<br><br>

- **[`RESPONSIBLE_AI.md`](RESPONSIBLE_AI.md)** — princípios de governança que motivam várias das mitigações acima
- **[`LGPD_ALIGNMENT.md`](LGPD_ALIGNMENT.md)** — detalhamento do risco R12
- **[`MULTI_LLM_FALLBACK.md`](../arquitetura/MULTI_LLM_FALLBACK.md)** — detalhamento do risco R04

<br><br>

---

<br><br>

*Risk Register v2.0.0 · Investor Intelligence Platform FIIs Brasil*
