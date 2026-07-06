# 📘 Complete Execution and Deployment Manual
## Investor Intelligence Platform — Brazilian REITs (FIIs) 🇧🇷

**For whom:** anyone who needs to run this project — from someone who has never
opened a terminal to an experienced data engineer who just wants the right command.
Sections marked "🎓 Explained" are for beginners; experienced users can skip straight
to the code blocks.

> **What changed in this version (v2.0.0):**
> - Groq model migrated: `llama-3.1-8b-instant` → **`openai/gpt-oss-20b`**
>   (deprecation email received June 2026, decommission date August 16, 2026)
> - 4 runtime bugs found during real end-to-end execution and fixed (details in
>   Troubleshooting section)
> - GEMINI_API_KEY added as automatic fallback when Groq hits rate limits
> - Section 6.0 added: which `requirements*.txt` to use in each scenario

---

## 📋 Table of Contents

1. [TL;DR — For Those Who Already Know](#1-tldr--for-those-who-already-know)
2. [System Architecture Overview](#2-system-architecture-overview)
3. [Part 1 — Setting Up the Local Environment](#3-part-1--setting-up-the-local-environment)
4. [Part 2 — Running the Notebooks (NB00→NB07)](#4-part-2--running-the-notebooks-nb00nb07)
5. [Part 3 — Testing Locally (API + Dashboard)](#5-part-3--testing-locally-api--dashboard)
6. [Part 4 — Production Deployment](#6-part-4--production-deployment)
7. [Part 5 — Automation and Data Refresh](#7-part-5--automation-and-data-refresh)
8. [Part 6 — Consolidated Troubleshooting](#8-part-6--consolidated-troubleshooting)
9. [Command Cheat Sheet](#9-command-cheat-sheet)

---

## 1. TL;DR — For Those Who Already Know

```bash
# Environment
python3.11 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# Full pipeline (mandatory order)
jupyter nbconvert --to notebook --execute --inplace notebooks/NB0{0,1,2,3,4,5,6,7}_*.ipynb

# Pre-flight check before committing
python scripts/preflight_check.py

# Commit Gold artifacts (Render + Streamlit Cloud are stateless — they need this)
git add -f data/gold/ data/external/ data/silver/
git commit -m "data refresh" && git push

# Local — API
uvicorn api.app:app --reload --port 8000

# Local — Dashboard (reads local Parquet, no API_BASE_URL set)
streamlit run dashboard/Home.py

# Production — Dashboard consuming the deployed API
API_BASE_URL="https://YOUR-API.onrender.com" streamlit run dashboard/Home.py
```

**LLM model (updated):** `openai/gpt-oss-20b` on Groq (primary), with automatic
fallback to Gemini 2.5 Flash (`gemini-2.5-flash`) if Groq hits a rate limit or
is temporarily unavailable.

**Deploy:** Render via `render.yaml` (Blueprint) → Streamlit Cloud pointing
`API_BASE_URL` in Secrets → update `ALLOWED_ORIGINS` in Render with the final
Streamlit URL. Data refresh is **manual**, via GitHub Actions
`workflow_dispatch` (the "Run workflow" button). Details in Part 7.

---

## 2. System Architecture Overview

### 🎓 Explained

Think of this project as a production line in 3 stages:

1. **Data factory** (8 Jupyter notebooks, NB00→NB07) — runs on your machine (or
   GitHub Actions), processes news articles and generates ready-to-use files.
2. **Warehouse** (folders `data/gold/`, inside the Git repository itself) —
   where the ready files are stored.
3. **Storefront** (API on Render + Dashboard on Streamlit Cloud) — where external
   users see the results without needing to know how to run Python.

```
┌─────────────────────────────────────────────────────────────┐
│  YOUR MACHINE (or GitHub Actions)                           │
│  Jupyter: NB00 → NB01 → ... → NB07                          │
│  Generates: data/gold/*.parquet, *.pkl, *.npz, *.faiss       │
└───────────────────────┬─────────────────────────────────────┘
                        │ git push
                        ▼
┌─────────────────────────────────────────────────────────────┐
│  GITHUB (repository)                                         │
│  Stores the code AND Gold data (committed)                   │
└───────────┬───────────────────────────────┬─────────────────┘
            │ auto-deploy                  │ auto-deploy
            ▼                              ▼
┌───────────────────────┐      ┌───────────────────────────┐
│  RENDER               │      │  STREAMLIT COMMUNITY CLOUD │
│  api/app.py            │◄────│  dashboard/Home.py         │
│  Reads data/gold/       │ HTTP│  Calls the API via requests │
└───────────────────────┘      └───────────────────────────┘
```

**Key point that often confuses people:** the notebooks **do not run** inside
Render or Streamlit Cloud. Those two platforms only **serve** what has already
been processed and stored in Git. The processing is done by you, on your machine
(or via GitHub Actions, in Part 7).

---

## 3. Part 1 — Setting Up the Local Environment

### 3.1 — What You Need to Install

| Tool | What for | Minimum version |
|---|---|---|
| Python | Running notebooks, API, and dashboard | 3.10+ (3.11 recommended) |
| Java (JDK) | PySpark depends on this internally | 11+ (21 also works — confirmed in testing) |
| Git | Cloning the repository, committing | any recent version |

### 🎓 Explained: What is a "terminal"?

A terminal (or "command prompt", "shell", "console") is a text window where you
type commands instead of clicking icons.

- **Windows:** open "PowerShell" (search in the Windows taskbar).
- **Mac:** open the "Terminal" app (Spotlight → type "Terminal").
- **Linux:** usually `Ctrl+Alt+T`.

### 3.2 — Checking What's Already Installed

```bash
python3 --version   # should show 3.10 or higher
java -version        # should show 11 or higher
git --version        # any version
```

**Installing Java:**
- Windows: download "Temurin 11" at [adoptium.net](https://adoptium.net/)
- Mac: `brew install openjdk@11`
- Linux: `sudo apt install openjdk-11-jdk`

### 3.3 — Cloning the Project

```bash
git clone https://github.com/Quantum-Software-Development/5-cybersecurity-social-engineering-fii-marketing-intelligence-platform
cd 5-cybersecurity-social-engineering-fii-marketing-intelligence-platform
```

### 3.4 — Creating the Virtual Environment

### 🎓 Explained: Why a "virtual environment"?

A virtual environment is an isolated "box" just for this project's Python
libraries — so they don't conflict with other versions installed on your computer.

```bash
# Create the environment (once only)
python3 -m venv .venv

# Activate the environment (every time you work on the project)
source .venv/bin/activate        # Linux/Mac
.venv\Scripts\activate           # Windows (PowerShell or CMD)
```

When activated, the beginning of the terminal line changes to show `(.venv)` —
that's how you know you're "inside the right box".

> ⚠️ You need to **reactivate** the virtual environment every time you open a new
> terminal. If commands start giving "module not found" errors, the first step is
> to check that `(.venv)` appears at the beginning of the line.

### 3.5 — Installing Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

> **⚠️ Runtime note (found during real end-to-end testing):**
> On modern Linux systems (Ubuntu 22.04+, Debian 12+) that protect the system
> Python (PEP 668 — "externally managed environment"), a plain `pip install`
> will fail with an `ExternallyManagedEnvironment` error. **The fix is already
> inside the notebooks** (NB00 tries without the flag first, catches the
> `CalledProcessError`, then automatically retries with `--break-system-packages`).
> If you're running pip directly at the terminal and hit this error, add the flag:
> ```bash
> pip install --break-system-packages -r requirements.txt
> ```
> This is not a bug in the project — it's an OS-level protection added in
> Python 3.11+ on Debian-based distros.

This will take 2–8 minutes on the first run. The largest packages are:
- `pyspark` (~300 MB)
- `torch` (embedded in `sentence-transformers`, ~500 MB)
- `sentence-transformers` + `faiss-cpu` (~120 MB model download at first use)

> **Note on FAISS and sentence-transformers (Layer 3 — Semantic Search):**
> These are optional. If the model download fails (firewall, offline, Hugging Face
> Hub temporarily unavailable), NB04 automatically degrades to hybrid v1
> (TF-IDF 40% + BM25 60%) without breaking the pipeline. The notebooks detect
> the failure and print a clear warning message.

### 3.6 — Configuring Environment Variables (.env)

```bash
cp .env.example .env
```

Open the `.env` file in any text editor and fill in:

| Variable | Required? | Where to get it |
|---|---|---|
| `GROQ_API_KEY` | No (but without it the chatbot falls through to Gemini, then demo mode) | [console.groq.com](https://console.groq.com) — free, no credit card |
| `GEMINI_API_KEY` | No (but without it there's no fallback if Groq hits rate limits) | [aistudio.google.com](https://aistudio.google.com) → *Get API key* — free, no credit card |
| `REDDIT_CLIENT_ID` / `SECRET` | No (NB01 has automatic fallback to Google News RSS) | [reddit.com/prefs/apps](https://www.reddit.com/prefs/apps) |

### 🎓 Explained: Why two LLM keys?

The chatbot tries Groq first (lower latency, ~0.3s per response). If Groq
returns an error or hits its rate limit (30 requests/minute on the free tier),
it automatically falls back to Gemini — the user sees a small informational note
in the response footer, but the experience doesn't break. Both are free, both
have stable free tiers, neither requires a credit card. If neither key is
configured, the chatbot runs in demo mode (shows the retrieved context without
generating text).

> 🔒 **Never** share or commit the `.env` file — it's already protected by
> `.gitignore`. Always use `.env.example` as the public template.

---

## 4. Part 2 — Running the Notebooks (NB00→NB07)

### 🎓 Explained: Why does order matter?

Each notebook **reads the result** of the previous one. NB04 doesn't work
without the Silver data that NB02 generated; NB07 doesn't work without results
from NB03, NB04, NB05, and NB06. It's like assembling furniture following the
manual — skipping a step blocks the next one.

### 4.1 — Opening Jupyter

```bash
jupyter lab notebooks/
```

This opens a tab in your browser with the list of notebooks. Double-click
`NB00_setup.ipynb` to open the first one.

### 🎓 Explained: How to run a notebook

Inside Jupyter, each notebook is divided into "cells". To run a cell: click it
and press `Shift + Enter` (moves to the next one automatically). To run **all
cells at once**, use the menu **Run → Run All Cells**.

### 4.2 — Execution Table (mandatory order)

| # | Notebook | What it does | Estimated duration | Watch out for |
|---|---|---|---|---|
| 1 | `NB00_setup.ipynb` | Installs dependencies, creates `config/settings.py`, `api/app.py`, `dashboard/Home.py`, `groq_client.py` | ~2–5 min | First run downloads packages — may take longer. If `pip install` fails on Linux with an "externally managed" error, see Section 3.5 |
| 2 | `NB01_bronze_ingestion.ipynb` | Live collection from 21 sources (RSS + scraping + Google News) | ~15–30 min | Depends on your internet speed; some sources may fail (normal — 3-level fallback in place for each source) |
| 3 | `NB02_bronze_to_silver.ipynb` | Cleans and normalizes the collected text | ~5 min | Requires Bronze data from NB01. Produces 20 columns (not 22 — documentation corrected after real execution) |
| 4 | `NB03_word_count_mapreduce.ipynb` | Word count via PySpark (MapReduce) | ~5 min | — |
| 5 | `NB04_tfidf_bm25.ipynb` | Builds 3 retrieval indexes (TF-IDF, BM25, FAISS) | ~10–20 min | First run downloads the embedding model (~120 MB). If the download fails (firewall/offline), the notebook **automatically continues in hybrid v1 mode** (TF-IDF + BM25 only) — this is expected behavior, not a failure |
| 6 | `NB05_contextual_sentiment.ipynb` | Calculates sentiment via custom FII PT-BR lexicon | ~10 min | — |
| 7 | `NB06_marketing_intelligence.ipynb` | Generates per-FII metrics (MI Score) | ~15 min | — |
| 8 | `NB07_dashboard_dataset.ipynb` | Consolidates everything for the dashboard/API | ~5 min | Last step — generates the files that production will serve |

**Total estimated time:** 1h to 1h30 on the first complete execution.

### 4.3 — How to Know if a Notebook Ran Correctly

At the end of each notebook there is a validation cell that prints something like:

```
OK  dashboard_articles.parquet
OK  dashboard_fii_signals.parquet
...
🎉 8/8 checks — NB0X COMPLETE
```

If `XX` (error) appears instead of `OK`, **do not advance** to the next notebook
— first resolve the problem (see Part 8, Troubleshooting).

### 4.4 — Running from the Command Line (without opening Jupyter visually)

Useful if you already trust the pipeline and just want to reprocess quickly:

```bash
for nb in notebooks/NB0{0,1,2,3,4,5,6,7}_*.ipynb; do
  echo "Running $nb..."
  jupyter nbconvert --to notebook --execute --inplace "$nb"
done
```

---

## 5. Part 3 — Testing Locally (API + Dashboard)

### 5.1 — Running the API Locally

```bash
uvicorn api.app:app --reload --port 8000
```

Open in your browser: [http://localhost:8000/docs](http://localhost:8000/docs) —
this is the **Swagger UI**, an automatic page listing all endpoints where you can
test them by clicking, without writing any code.

**Key endpoints:**

| Endpoint | Method | What it returns |
|---|---|---|
| `/health` | GET | System status: `data_available`, `groq_configured`, `gemini_configured`, `semantic_search_enabled` |
| `/articles` | GET | List of articles with sentiment scores and hybrid relevance |
| `/fii/{ticker}` | GET | Signals for a specific FII (e.g. `/fii/HGLG11`) |
| `/sources` | GET | Source statistics ranked by MI score |
| `/query` | POST | RAG response (retrieval + generation via Groq → Gemini fallback) |
| `/summary` | GET | Full pipeline summary JSON |

### 5.2 — Running the Dashboard Locally

In **another** terminal (leave the API running in the first one):

```bash
source .venv/bin/activate   # if not already activated in this terminal
streamlit run dashboard/Home.py
```

Opens automatically at [http://localhost:8501](http://localhost:8501).

By default (no `API_BASE_URL` set), the dashboard reads Parquet files directly
from `data/gold/` — it doesn't even need the API running for this.

### 5.3 — Testing the Dashboard Consuming the Local API

```bash
API_BASE_URL="http://localhost:8000" streamlit run dashboard/Home.py
```

This simulates exactly the production behavior, but everything on your machine
— useful for catching issues before deploying for real.

---

## 6. Part 4 — Production Deployment

> This section summarizes the two dedicated guides: `DEPLOY_RENDER.md` (API) and
> `DEPLOY_STREAMLIT.md` (Dashboard). Read them for the complete step-by-step.

### 6.0 — Which `requirements*.txt` to Use in Each Scenario

This project has **4 dependency files** — one for each execution environment:

```
fii-intelligence-platform/
├── requirements.txt              ← Notebooks (local, full, ~57 packages)
├── requirements-dev.txt          ← + Jupyter/tests (add to the above)
├── requirements-api.txt          ← API deploy on Render (~12 packages)
└── dashboard/
    ├── Home.py
    └── requirements.txt          ← Dashboard deploy on Streamlit Cloud (~7 packages)
```

| Scenario | Command |
|---|---|
| Run notebooks NB00–NB07 | `pip install -r requirements.txt` |
| Develop + test + lint | `pip install -r requirements.txt -r requirements-dev.txt` |
| API deploy (Render) | Automatic — `render.yaml` already points to `requirements-api.txt` |
| Dashboard deploy (Streamlit Cloud) | Automatic — Streamlit Cloud detects `dashboard/requirements.txt` by itself |

> See `docs/architecture/REQUIREMENTS_GUIA.md` for the full explanation of why
> the dashboard has its own separate `requirements.txt` (hint: Streamlit Cloud
> looks in the entrypoint's own folder first, before the repo root).

### 6.1 — Why Order Matters: API First, Dashboard Second

The production dashboard needs an already-working API URL to point to
(`API_BASE_URL`). Doing it backwards means configuring the dashboard twice.

### 6.2 — Checklist Before Any Deploy

```bash
python scripts/preflight_check.py
```

This script automatically checks:
- All required Gold files exist
- They are **committed to Git** (not blocked by `.gitignore`)
- `.env` is NOT being versioned by accident
- **`GROQ_API_KEY` is set** (warns if not — chatbot falls back to Gemini)
- **`GEMINI_API_KEY` is set** (warns if not — no fallback available)
- File sizes are within GitHub's 100MB limit per file

Resolve every item marked `FAIL` before continuing.

### 6.3 — Committing Gold Artifacts

```bash
git add -f data/gold/dashboard/*.parquet data/gold/dashboard/*.json
git add -f data/gold/tfidf_bm25/*.pkl data/gold/tfidf_bm25/*.npz data/gold/tfidf_bm25/*.parquet
git commit -m "chore: Gold artifacts for deploy"
git push
```

### 6.4 — API Deploy (Render)

Summary (full details in `DEPLOY_RENDER.md`):

1. Create account at [render.com](https://render.com)
2. **New → Blueprint** → connect repository → Render detects `render.yaml`
3. Manually configure secrets `GROQ_API_KEY` **and** `GEMINI_API_KEY` (they don't
   go through the Blueprint — must be set in Environment Variables manually)
4. Wait for build (~3–6 min) and test: `curl https://YOUR-API.onrender.com/health`

Expected `/health` response:
```json
{
  "status": "ok",
  "groq_configured": true,
  "gemini_configured": true,
  "data_available": true,
  "semantic_search_enabled": false
}
```

### 6.5 — Dashboard Deploy (Streamlit Cloud)

Summary (full details in `DEPLOY_STREAMLIT.md`):

1. Create account at [share.streamlit.io](https://share.streamlit.io)
2. **New app** → repository → main file `dashboard/Home.py`
3. In **Secrets**, add:
   ```toml
   API_BASE_URL = "https://YOUR-API.onrender.com"
   ```
4. Deploy (~2–5 min) and check the 🟢 indicator in the dashboard sidebar

### 6.6 — Closing the CORS Loop

Go back to Render and update:
```
ALLOWED_ORIGINS=https://YOUR-APP.streamlit.app
```

---

## 7. Part 5 — Automation and Data Refresh

### 7.1 — How It Works Today

The trigger is **manual** (`workflow_dispatch`) — not scheduled. Data is
refreshed only when someone clicks "Run workflow" in the GitHub Actions tab.

```
You click "Run workflow" on GitHub Actions
        ↓
GitHub Actions runs NB00 → NB07 (on GitHub's servers, not your machine)
        ↓
New Gold is automatically committed to the repository
        ↓
Render detects the push → automatically redeploys the API
Streamlit Cloud detects the push → automatically redeploys the dashboard
        ↓
Dashboard and API now serve the new data
```

### How to trigger manually

1. Go to the **Actions** tab in your GitHub repository
2. Click **"Atualizar Dados FII (Manual)"** in the workflow list
3. Click the **"Run workflow"** button (top right)
4. (Optional) write a reason in the text field
5. Click **"Run workflow"** again to confirm

Runtime: 20–45 minutes (the longest part is NB01 collecting from live sources).

### 7.2 — Why No Automatic Scheduling (Cron)

| Reason | Explanation |
|---|---|
| NB01 is structurally fragile for unsupervised runs | Live scraping across 20+ sites — any of them can change layout, go offline, or block requests on a specific day |
| Silent failure is worse than visible failure | If a cron runs at 3am and partially fails, the dashboard silently serves broken data until someone notices manually |
| Control over refresh timing | For an academic presentation, you want to be able to refresh minutes before — not depend on a fixed schedule that may or may not have run recently |

### 7.3 — How to Enable Scheduled Refresh (if you want it later)

After running the manual workflow a few times and confirming it's stable, edit
`.github/workflows/atualizar_dados.yml` and add:

```yaml
on:
  workflow_dispatch:
    inputs:
      motivo:
        description: "Reason for refresh"
        required: false
  schedule:
    - cron: "0 6 * * *"   # every day at 06:00 UTC (03:00 Brasília time)
```

**Cron syntax reference:**

| Schedule | Expression |
|---|---|
| Every day at 6am UTC | `0 6 * * *` |
| Every 6 hours | `0 */6 * * *` |
| Every Monday at 8am UTC | `0 8 * * 1` |
| Twice a day (6am + 6pm UTC) | `0 6,18 * * *` |

> ⚠️ GitHub Actions uses UTC. Brasília is UTC-3. For 6am Brasília time outside
> daylight saving, use `cron: "0 9 * * *"`.

---

## 8. Part 6 — Consolidated Troubleshooting

This section includes the standard issues **plus 4 bugs found during real
end-to-end execution testing** — all of which have already been fixed in the
delivered notebooks.

| Symptom | Where | Probable cause | Solution |
|---|---|---|---|
| `ModuleNotFoundError` | Any notebook | Virtual environment not activated, or `pip install` not run | `source .venv/bin/activate` and repeat `pip install -r requirements.txt` |
| `ExternallyManagedEnvironment` error during `pip install` | Terminal / NB00 | PEP 668 protection on modern Linux (Ubuntu 22.04+, Debian 12+) — OS prevents pip from writing to system Python | Add `--break-system-packages` flag: `pip install --break-system-packages -r requirements.txt`. NB00 already handles this automatically inside the notebook |
| `AttributeError: module 'rank_bm25' has no attribute '__version__'` | NB04 | The `rank_bm25` package doesn't expose `__version__` | Already fixed in delivered NB04 (uses `importlib.metadata.version('rank-bm25')` with fallback). If you see this, update to the latest notebook version |
| FAISS/SentenceTransformer model download fails with `OSError` or connection error | NB04 (Seção 8) | Firewall, offline environment, or Hugging Face Hub temporarily unavailable | Already fixed: NB04 wraps the model load in `try/except Exception`, sets `emb_model = None`, and prints a clear warning. Pipeline continues in hybrid v1 mode (TF-IDF 40% + BM25 60%) |
| `ValueError: Trace type 'pie' is not compatible with subplot type 'xy'` | NB05 or NB07 | Plotly `make_subplots` needs explicit `specs` to mix pie charts with cartesian grids | Already fixed in delivered NB05 and NB07 (`specs=[[{"type": "domain"}, ...]]`). If you see this, update to the latest notebook versions |
| `java: command not found` | NB00-NB07 (any with Spark) | Java not installed | See Section 3.2 |
| Notebook hangs at "Running" forever | NB01 | A source is taking too long to respond | Wait — there's a 20s timeout per source; or interrupt and re-run |
| `FileNotFoundError: silver_articles.parquet` | NB03, NB04, NB05 | NB02 was not executed, or failed | Go back and re-execute NB02 |
| API returns 404 on `/articles` | Local API test | NB07 was not executed, or `data/gold/dashboard/` is empty | Execute NB07 |
| Render shows "Application failed to respond" | Render deploy | `data/gold/` was not committed to Git | Run `python scripts/preflight_check.py` and fix the `FAIL` items |
| Dashboard shows 🔴 "API unavailable" on Streamlit Cloud | Streamlit deploy | Render in cold-start (spin-down after inactivity), or wrong `API_BASE_URL` in Secrets | Wait 30–50s and reload; check the URL in Secrets |
| CORS error in browser console | Dashboard in production | `ALLOWED_ORIGINS` on Render does not include the Streamlit URL | Update the variable on Render (Section 6.6) |
| `faiss-cpu` fails to install | `pip install -r requirements.txt` | Usually missing C++ compiler (rare, more common on older Windows) | Use `pip install faiss-cpu --only-binary :all:` or WSL2 on Windows |
| GitHub Actions fails on NB01 step | Manual workflow | A source blocked requests from GitHub's server IP (different from yours) | Normal and expected occasionally — the pipeline has fallback (Google News RSS) and continues with the remaining sources |
| Chatbot shows `[DEMO MODE]` in the response | Dashboard / API `/query` | Neither `GROQ_API_KEY` nor `GEMINI_API_KEY` is configured | Set at least one of them. If both are set and still getting demo mode, check that the keys are valid and not expired |
| Chatbot note: "Response generated via Gemini — automatic fallback" | Dashboard / API `/query` | Groq hit its rate limit (30 RPM on free tier) — Gemini stepped in | Expected behavior, not an error. Groq rate window resets per minute. If happening frequently, slow down query rate |

---

## 9. Command Cheat Sheet

```bash
# ── Environment (full notebooks) ──────────────────────────
python3 -m venv .venv
source .venv/bin/activate              # Linux/Mac
.venv\Scripts\activate                 # Windows
pip install -r requirements.txt
cp .env.example .env
# fill in GROQ_API_KEY and GEMINI_API_KEY in .env

# ── Lightweight environments (API or Dashboard only) ───────
pip install -r requirements-api.txt         # API in isolation
pip install -r dashboard/requirements.txt   # Dashboard in isolation

# ── Notebooks ─────────────────────────────────────────────
jupyter lab notebooks/            # visual interface
# run each one in order: NB00 → NB01 → ... → NB07

# ── Validation before deploy ──────────────────────────────
python scripts/preflight_check.py

# ── Local: API ────────────────────────────────────────────
uvicorn api.app:app --reload --port 8000
curl http://localhost:8000/health

# ── Local: Dashboard ──────────────────────────────────────
streamlit run dashboard/Home.py                                       # local mode (Parquet)
API_BASE_URL="http://localhost:8000" streamlit run dashboard/Home.py  # API mode

# ── Git: committing Gold artifacts ────────────────────────
git add -f data/gold/ data/external/ data/silver/
git commit -m "data refresh"
git push

# ── Production: testing endpoints ─────────────────────────
curl https://YOUR-API.onrender.com/health
curl https://YOUR-API.onrender.com/articles?limit=5
curl -X POST "https://YOUR-API.onrender.com/query?question=Which+FII+pays+the+most+dividends"

# ── Automation: trigger manual data refresh ────────────────
# via GitHub interface — Actions tab → Run workflow
# or via GitHub CLI (if installed):
gh workflow run "Atualizar Dados FII (Manual)" -f motivo="Pre-presentation refresh"
```

---

*Complete Execution and Deployment Manual v2.0.0 · Investor Intelligence Platform — FIIs Brasil*
*PUC-SP FACEI · Updated: Groq model migration (`openai/gpt-oss-20b`) + 4 runtime bug fixes from real end-to-end execution*
