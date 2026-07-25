<!-- LANGUAGE BUTTONS -->
**\[[🇧🇷 Português](DEPLOY_RENDER.md)\] \[**[🇬🇧 English](../../🇬🇧English/deploy/DEPLOY_RENDER.md)**\]**

<br><br>

## [Deploy da API no Render — Guia Passo a Passo]()
### Investor Intelligence Platform — FIIs Brasil 🇧🇷

<br><br>

## [Pré-requisitos]()

<br><br>

- [ ] Conta no [Render](https://render.com) (free tier funciona)
- [ ] Repositório Git com o projeto (GitHub/GitLab)
- [ ] **`data/gold/` commitado ao repositório** — ver seção crítica abaixo
- [ ] `GROQ_API_KEY` ([console.groq.com](https://console.groq.com)) — motor primário do chatbot
- [ ] `GEMINI_API_KEY` ([aistudio.google.com](https://aistudio.google.com) → *Get API key*) — motor de fallback, opcional mas recomendado

<br><br>

## [⚠️ Decisão Arquitetural Crítica: Dados Gold no Repositório]()

<br><br>

O Render é **stateless** — cada deploy provisiona um container limpo, sem acesso aos arquivos gerados localmente pelos seus notebooks Jupyter. A API só consegue servir `/articles`, `/fii/{ticker}`, `/sources`, `/query` e `/summary` se os artefatos abaixo estiverem **commitados no Git**:

<br><br>

```
data/gold/dashboard/dashboard_articles.parquet
data/gold/dashboard/dashboard_fii_signals.parquet
data/gold/dashboard/dashboard_source_stats.parquet
data/gold/dashboard/dashboard_funnel_stats.parquet
data/gold/dashboard/dashboard_word_cloud.parquet
data/gold/dashboard/api_payload_summary.json
data/gold/tfidf_bm25/tfidf_vectorizer.pkl
data/gold/tfidf_bm25/tfidf_matrix.npz
data/gold/tfidf_bm25/bm25_index.pkl
data/gold/tfidf_bm25/doc_index_map.parquet
```

<br><br>

**Por que isso é academicamente aceitável:** o corpus FII deste projeto (500–5.000 artigos) gera Parquet de poucos MB — muito abaixo do limite de 100MB do GitHub por arquivo. Esta é a mesma lógica do "dataset frozen" já documentada na regra de freeze do Bronze (NB01): **dados versionados como artefato, não como código gerado em runtime**.

<br><br>

```bash
# Garanta que .gitignore NÃO está excluindo data/gold/
git add -f data/gold/dashboard/*.parquet data/gold/dashboard/*.json
git add -f data/gold/tfidf_bm25/*.pkl data/gold/tfidf_bm25/*.npz data/gold/tfidf_bm25/*.parquet
git commit -m "chore: commit Gold artifacts for Render deployment"
git push
```

<br><br>

> Se `embeddings.npy` + `faiss_index.faiss` (Camada 3) também devem ir para produção, commite-os igualmente — mas isso só importa se `ENABLE_SEMANTIC_SEARCH=true`.

<br><br>

## [Arquivos deste Pacote de Deploy]()

<br><br>

| Arquivo | Onde colocar no repo | Função |
|---|---|---|
| `api/app.py` | `api/app.py` (substitui o gerado pelo NB00) | API FastAPI com CORS, feature flags, `/health` rico |
| `dashboard/chatbot/groq_client.py` | `dashboard/chatbot/groq_client.py` | RAG com flag `ENABLE_SEMANTIC_SEARCH` explícita |
| `render.yaml` | raiz do projeto | Blueprint de deploy automatizado do Render |
| `requirements-api.txt` | raiz do projeto | Dependências **leves** — só o necessário para servir |
| `.env.example` | raiz do projeto (substitui o existente) | Documenta as novas variáveis de produção |

<br><br>

## [Passo 1 — Decidir sobre a Camada 3 (FAISS)]()

<br><br>

| Plano Render | RAM | `ENABLE_SEMANTIC_SEARCH` recomendado |
|---|---|---|
| **Free** | 512 MB | `false` — torch+sentence-transformers arriscam OOM |
| **Starter** ($7/mês) | 2 GB | Viável `true`, mas teste antes |
| **Standard+** | 4 GB+ | `true` sem ressalvas |

<br><br>

Para a entrega acadêmica no tier free, **mantenha `false`**. A API funciona plenamente em modo `hybrid_v1` (TF-IDF 40% + BM25 60%) — só perde a camada semântica, não a funcionalidade.

<br><br>

## [Passo 2 — Deploy via Blueprint (`render.yaml`)]()

<br><br>

1. Acesse [dashboard.render.com](https://dashboard.render.com) → **New** → **Blueprint**
2. Conecte o repositório GitHub do projeto
3. Render detecta `render.yaml` automaticamente e propõe o serviço `fii-intelligence-api`
4. Clique em **Apply**

<br><br>

[***Configurar os Secrets `GROQ_API_KEY` e `GEMINI_API_KEY`***]()

<br><br>

O `render.yaml` marca ambas as chaves com `sync: false` — isso significa que o Render **não** vai pedir os valores no Blueprint; você precisa definir os dois manualmente:

<br><br>

1. No serviço criado → **Environment** → **Add Environment Variable**
2. Key: `GROQ_API_KEY` · Value: sua chave real do Groq
3. **Add Environment Variable** de novo → Key: `GEMINI_API_KEY` · Value: sua chave do Gemini
4. **Save Changes** (isso aciona um redeploy automático)

<br><br>

> `GEMINI_API_KEY` é opcional, mas recomendado — sem ela, o chatbot funciona normalmente via Groq, só não tem para onde cair se o Groq sofrer rate-limit (HTTP 429) durante uso intenso. Ver [`MULTI_LLM_FALLBACK.md`](../arquitetura/MULTI_LLM_FALLBACK.md) para a justificativa completa dessa decisão.

<br><br>

## [Passo 3 — Deploy Manual (Alternativa sem Blueprint)]()

<br><br>

Se preferir não usar `render.yaml`:

<br><br>

1. **New** → **Web Service** → conecte o repositório
2. **Build Command:**
   ```
   pip install --upgrade pip && pip install -r requirements-api.txt
   ```
3. **Start Command:**
   ```
   uvicorn api.app:app --host 0.0.0.0 --port $PORT
   ```
4. **Environment Variables:**

   | Key | Value |
   |---|---|
   | `PYTHON_VERSION` | `3.11.9` |
   | `ENABLE_SEMANTIC_SEARCH` | `false` |
   | `ALLOWED_ORIGINS` | `*` (trocar depois pela URL do Streamlit Cloud) |
   | `GROQ_API_KEY` | _sua chave_ |
   | `GEMINI_API_KEY` | _sua chave_ (fallback — opcional, mas recomendado) |
   | `LOG_LEVEL` | `INFO` |

5. **Health Check Path:** `/health`
6. Create Web Service

<br><br>

## [Passo 4 — Validar o Deploy]()

<br><br>

Após o build (3–6 min na primeira vez), acesse a URL gerada (`https://fii-intelligence-api.onrender.com`):

<br><br>

```bash
curl https://fii-intelligence-api.onrender.com/health
```

<br><br>

Resposta esperada:

<br><br>

```json
{
  "status": "ok",
  "version": "1.0.0",
  "docs": "/docs",
  "semantic_search_enabled": false,
  "faiss_index_present": false,
  "data_available": true,
  "groq_configured": true,
  "gemini_configured": true
}
```

<br><br>

| Campo | Se `false`/incorreto | Ação |
|---|---|---|
| `data_available` | `false` | `data/gold/dashboard/` não foi commitado — revisar Passo "Decisão Arquitetural" |
| `groq_configured` | `false` | `GROQ_API_KEY` não foi salva no Environment do Render |
| `gemini_configured` | `false` | `GEMINI_API_KEY` não foi salva — chatbot funciona via Groq, mas sem fallback |
| `semantic_search_enabled` | inesperado | Conferir variável `ENABLE_SEMANTIC_SEARCH` no Environment |

<br><br>

Teste os demais endpoints:

<br><br>

```bash
curl https://fii-intelligence-api.onrender.com/articles?limit=5
curl https://fii-intelligence-api.onrender.com/fii/HGLG11
curl https://fii-intelligence-api.onrender.com/sources
curl -X POST "https://fii-intelligence-api.onrender.com/query?question=Qual+FII+paga+mais+dividendo"
```

<br><br>

Swagger UI interativo: `https://fii-intelligence-api.onrender.com/docs`

<br><br>

## [Limitações Conhecidas do Tier Free]()

<br><br>

| Limitação | Impacto | Mitigação |
|---|---|---|
| **Spin-down após 15min inativo** | Primeira requisição após inatividade demora ~30-50s (cold start) | Aceitável para demo acadêmica; em produção real, usar plano pago ou um ping externo |
| **512 MB RAM** | Sem margem para Camada 3 (FAISS+torch) | `ENABLE_SEMANTIC_SEARCH=false` (padrão já configurado) |
| **750h/mês grátis** | Suficiente para 1 serviço 24/7 | Sem ação necessária para este projeto |

<br><br>

## [Próximo Passo]()

<br><br>

Com a API validada e publicada, o próximo passo da Fase 2 é apontar o dashboard Streamlit para consumir esta API via HTTP (em vez de ler os Parquet locais diretamente), e então publicá-lo no Streamlit Community Cloud — usando a mesma URL desta API como variável de ambiente (`API_BASE_URL`). Ver [`DEPLOY_STREAMLIT.md`](DEPLOY_STREAMLIT.md).

<br><br>

---

<br><br>

*Deploy Render v1.0.0 · Investor Intelligence Platform FIIs Brasil*
