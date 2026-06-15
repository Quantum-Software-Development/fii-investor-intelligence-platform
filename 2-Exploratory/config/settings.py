"""
config/settings.py — Single Source of Truth
Investor Intelligence Platform — FIIs Brasil
Gerado por NB00. NÃO edite manualmente — re-execute NB00 para regenerar.
"""
from pathlib import Path
import os

# ─── Reprodutibilidade ────────────────────────────────────────────────────────
RANDOM_SEED = 42

# ─── Raiz do projeto ──────────────────────────────────────────────────────────
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# ─── Caminhos Medallion ───────────────────────────────────────────────────────
DATA_DIR     = PROJECT_ROOT / "data"
EXTERNAL_DIR = DATA_DIR / "external"       # Bronze (frozen raw data)
BRONZE_DIR   = DATA_DIR / "bronze"         # Bronze (processed)
SILVER_DIR   = DATA_DIR / "silver"         # Silver (clean)
GOLD_DIR     = DATA_DIR / "gold"           # Gold (analytics)
LOGS_DIR     = PROJECT_ROOT / "logs"
CONFIG_DIR   = PROJECT_ROOT / "config"
SRC_DIR      = PROJECT_ROOT / "src"

# ─── Spark ────────────────────────────────────────────────────────────────────
SPARK_APP_NAME      = "FIIIntelligencePlatform"
SPARK_DRIVER_MEMORY = "4g"
SPARK_SHUFFLE_PARTS = "4"

# ─── HTTP client ──────────────────────────────────────────────────────────────
REQUEST_TIMEOUT  = 20      # seconds
MAX_RETRIES      = 3
RETRY_BACKOFF    = 2       # exponential base (2^attempt seconds)
RATE_LIMIT_DELAY = 1.0     # seconds between requests

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/118.0",
]

# ─── RSS Feeds primários (6 feeds — settings.py) ─────────────────────────────
# NB01 adiciona outros 4 SUPPLEMENTAL_RSS_FEEDS + 10 PORTAL_TARGETS = 21 total
RSS_FEEDS = [
    "https://www.infomoney.com.br/feed/",          # 1. InfoMoney
    "https://empiricus.com.br/feed/",              # 2. Empiricus
    "https://www.moneytimes.com.br/feed/",         # 3. Money Times
    "https://www.seudinheiro.com/feed/",           # 4. Seu Dinheiro
    "https://exame.com/feed/",                     # 5. Exame Invest
    "https://www.cnnbrasil.com.br/feed/",          # 6. CNN Brasil Business
]

# ─── FII Filter Terms ─────────────────────────────────────────────────────────
FII_FILTER_TERMS = [
    "fii", "fundo imobiliário", "fundo imobiliario",
    "fiis", "fundos imobiliários", "fundos imobiliarios",
    "reit", "dividendo", "dividendos", "provento", "proventos",
    "vacância", "vacancia", "cotista", "cotistas",
    "yield", "p/vp", "tijolo", "papel", "logística", "logistica",
    "shopping", "laje corporativa", "galpão", "galpao",
    "fundo de investimento imobiliário",
    "fundo de investimento imobiliario",
]

# ─── Reddit ───────────────────────────────────────────────────────────────────
REDDIT_CLIENT_ID     = os.getenv("REDDIT_CLIENT_ID", "")
REDDIT_CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET", "")
REDDIT_USER_AGENT    = os.getenv(
    "REDDIT_USER_AGENT",
    "FIIIntelligencePlatform/1.0 (academic; PUC-SP FACEI)",
)
REDDIT_SUBREDDITS    = ["investimentos", "farialimabets"]
REDDIT_API_AVAILABLE = bool(REDDIT_CLIENT_ID and REDDIT_CLIENT_SECRET)
