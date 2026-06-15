"""dashboard/Home.py — Upgraded FII Marketing Intelligence Dashboard. Includes Tabs, Charts, BM25 Search & Chatbot."""
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path
import sys
import os

# Page config
st.set_page_config(
    page_title="Investor Intelligence Hub",
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for Premium Design
st.markdown("""
    <style>
    .main {
        background-color: #0d1117;
        color: #c9d1d9;
    }
    .stMetric {
        background-color: #161b22;
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #30363d;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    div[data-testid="metric-container"] {
        background-color: #161b22;
        border: 1px solid #30363d;
        padding: 5% 5% 5% 10%;
        border-radius: 8px;
        color: #c9d1d9;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: #161b22;
        border: 1px solid #30363d;
        border-radius: 8px 8px 0px 0px;
        padding: 10px 20px;
        color: #8b949e;
        font-weight: 600;
    }
    .stTabs [aria-selected="true"] {
        background-color: #1f6feb !important;
        color: white !important;
        border-color: #1f6feb !important;
    }
    .sentiment-positive {
        color: #2ecc71;
        font-weight: bold;
    }
    .sentiment-negative {
        color: #e74c3c;
        font-weight: bold;
    }
    .sentiment-neutral {
        color: #95a5a6;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# Main Title with gradient/branding
st.markdown("""
    <div style="text-align: center; margin-bottom: 30px;">
        <h1 style="color: #00d2ff; font-family: 'Outfit', sans-serif; font-size: 3rem;">🏢 Investor Intelligence Platform</h1>
        <p style="color: #8b949e; font-size: 1.2rem;">Plataforma de Inteligência de Marketing & Análise de Comportamento para FIIs Brasil</p>
    </div>
""", unsafe_allow_html=True)

# Append search path to import search_functions
PROJECT_ROOT = Path(__file__).parent.parent
sys.path.append(str(PROJECT_ROOT / "data" / "gold" / "tfidf_bm25"))

# Sidebar Info
st.sidebar.image("https://img.icons8.com/color/144/real-estate.png", width=100)
st.sidebar.markdown("### 📊 FIIs Intelligence")
st.sidebar.info(
    "Esta plataforma consolida dados de **21 fontes** (RSS, Portais de Scraping, Reddit) "
    "e aplica processamento distribuído com **PySpark (Medallion Architecture)** e NLP "
    "para extrair sentimentos e relevância estruturada (TF-IDF/BM25)."
)

# API Key config in sidebar
st.sidebar.markdown("---")
st.sidebar.markdown("### 🔑 Configuração API Groq")
groq_api_key_input = st.sidebar.text_input(
    "GROQ API Key",
    type="password",
    value=os.getenv("GROQ_API_KEY", ""),
    help="Opcional: insira sua chave API do Groq para conversar com o assistente IA. Se já estiver no .env, será preenchida automaticamente."
)

GOLD = PROJECT_ROOT / "data" / "gold" / "dashboard"
SILVER = PROJECT_ROOT / "data" / "silver"

# Load Datasets
@st.cache_data
def load_all_datasets():
    articles = pd.read_parquet(GOLD / "dashboard_articles.parquet")
    fii_signals = pd.read_parquet(GOLD / "dashboard_fii_signals.parquet")
    source_stats = pd.read_parquet(GOLD / "dashboard_source_stats.parquet")
    funnel_stats = pd.read_parquet(GOLD / "dashboard_funnel_stats.parquet")
    word_cloud = pd.read_parquet(GOLD / "dashboard_word_cloud.parquet")
    
    # Load silver_enriched to get text_clean
    silver_enriched = pd.read_parquet(SILVER / "silver_enriched.parquet")
    # Merge text_clean to articles
    articles = pd.merge(articles, silver_enriched[['article_id', 'text_clean']], on='article_id', how='left')
    
    return articles, fii_signals, source_stats, funnel_stats, word_cloud

try:
    articles_df, fii_signals_df, source_stats_df, funnel_stats_df, word_cloud_df = load_all_datasets()
    data_loaded = True
except Exception as e:
    st.error(f"❌ Erro ao carregar os dados: {e}")
    st.warning("Execute os notebooks NB00-NB07 para gerar todos os arquivos parquet necessários.")
    data_loaded = False

if data_loaded:
    # Set up Tabs
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "🏠 Visão Geral",
        "🏢 Inteligência por FII",
        "🔍 Motor de Busca Híbrido",
        "📊 Análise Textual & Funil",
        "💬 Assistente Market IA"
    ])
    
    # ==========================================
    # TAB 1: VISÃO GERAL
    # ==========================================
    with tab1:
        st.subheader("Painel de Visão Geral")
        
        # Metric Cards
        col_m1, col_m2, col_m3, col_m4 = st.columns(4)
        with col_m1:
            st.metric("Total de Artigos", f"{len(articles_df)}")
        with col_m2:
            st.metric("FIIs Monitorados", f"{len(fii_signals_df)}")
        with col_m3:
            avg_polarity = articles_df["polarity_score"].mean()
            sentiment_emoji = "🟢" if avg_polarity > 0.05 else "🔴" if avg_polarity < -0.05 else "⚪"
            st.metric("Sentimento Médio", f"{avg_polarity:.3f} {sentiment_emoji}")
        with col_m4:
            st.metric("Fontes Monitoradas", f"{len(source_stats_df)}")
            
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Charts Columns
        col_c1, col_c2 = st.columns(2)
        
        with col_c1:
            st.markdown("#### Distribuição de Sentimento")
            sd = articles_df["sentiment_label"].value_counts()
            colors_sent = {"positivo": "#2ecc71", "neutro": "#95a5a6", "negativo": "#e74c3c"}
            fig_pie = go.Figure(go.Pie(
                labels=sd.index.tolist(),
                values=sd.values.tolist(),
                marker_colors=[colors_sent.get(l, "#7f8c8d") for l in sd.index],
                hole=0.4,
                textinfo='percent+label'
            ))
            fig_pie.update_layout(template="plotly_dark", height=320, margin=dict(t=10, b=10, l=10, r=10), paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
            st.plotly_chart(fig_pie, use_container_width=True)
            
        with col_c2:
            st.markdown("#### Artigos por Fonte (Top 10)")
            top_sources = source_stats_df.nlargest(10, "total_articles")
            fig_bar = px.bar(
                top_sources,
                x="total_articles",
                y="source_label",
                orientation='h',
                labels={"total_articles": "Número de Artigos", "source_label": "Fonte"},
                color_discrete_sequence=["#00d2ff"]
            )
            fig_bar.update_layout(template="plotly_dark", height=320, margin=dict(t=10, b=10, l=10, r=10), paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
            fig_bar.update_yaxes(autorange="reversed")
            st.plotly_chart(fig_bar, use_container_width=True)
            
        st.markdown("---")
        st.markdown("#### 📅 Artigos Recentes Monitorados")
        
        # Table view filter/controls
        source_filter = st.multiselect("Filtrar por Fonte:", options=articles_df["source_label"].unique())
        sent_filter = st.multiselect("Filtrar por Sentimento:", options=articles_df["sentiment_label"].unique())
        
        filtered_articles = articles_df.copy()
        if source_filter:
            filtered_articles = filtered_articles[filtered_articles["source_label"].isin(source_filter)]
        if sent_filter:
            filtered_articles = filtered_articles[filtered_articles["sentiment_label"].isin(sent_filter)]
            
        # Display selected columns
        display_cols = ["title", "source_label", "published_at", "sentiment_label", "polarity_score", "word_count", "url"]
        st.dataframe(
            filtered_articles[display_cols].sort_values(by="published_at", ascending=False).head(50),
            column_config={
                "title": st.column_config.TextColumn("Título"),
                "source_label": st.column_config.TextColumn("Fonte"),
                "published_at": st.column_config.TextColumn("Data"),
                "sentiment_label": st.column_config.TextColumn("Sentimento"),
                "polarity_score": st.column_config.NumberColumn("Score Pol."),
                "word_count": st.column_config.NumberColumn("Palavras"),
                "url": st.column_config.LinkColumn("Link Fonte")
            },
            use_container_width=True,
            hide_index=True
        )

    # ==========================================
    # TAB 2: INTELIGÊNCIA POR FII
    # ==========================================
    with tab2:
        st.subheader("Inteligência e Sinais de Sentimento por FII")
        
        # Select ticker
        selected_ticker = st.selectbox("Selecione um FII:", options=fii_signals_df["ticker"].unique())
        
        fii_row = fii_signals_df[fii_signals_df["ticker"] == selected_ticker].iloc[0]
        
        col_f1, col_f2 = st.columns([1, 2])
        
        with col_f1:
            st.markdown(f"### 🏢 {fii_row['ticker']} - {fii_row['full_name']}")
            st.markdown(f"**Segmento:** `{fii_row['segment']}`")
            
            st.markdown("---")
            # Metrics
            st.markdown(f"💬 **Menções no Corpus:** `{fii_row['mentions']}`")
            
            avg_sent = fii_row['sentiment_avg']
            sent_label = "Positivo" if avg_sent > 0.05 else "Negativo" if avg_sent < -0.05 else "Neutro"
            sent_color = "positive" if avg_sent > 0.05 else "negative" if avg_sent < -0.05 else "neutral"
            st.markdown(f"🎭 **Sentimento Médio:** <span class='sentiment-{sent_color}'>{avg_sent:.3f} ({sent_label})</span>", unsafe_allow_html=True)
            
            st.markdown(f"📈 **Score de Oportunidade:** `{fii_row['opportunity_score']:.2f}`")
            st.markdown(f"⚠️ **Score de Risco:** `{fii_row['risk_score']:.2f}`")
            st.markdown(f"🏆 **Marketing Intelligence (MI) Score:** `{fii_row['mi_score']:.3f}`")
            
            st.markdown("---")
            st.markdown("🔔 **Alertas e Sinais de Fundamentos:**")
            col_a1, col_a2 = st.columns(2)
            with col_a1:
                st.write(f"💰 Dividendos: `{fii_row['n_dividendo']}`")
                st.write(f"🔍 Oportunidades: `{fii_row['n_oportunidade']}`")
                st.write(f"🏢 Vacância: `{fii_row['n_vacancia']}`")
            with col_a2:
                st.write(f"🛑 Risco: `{fii_row['n_risco']}`")
                st.write(f"💥 Crise: `{fii_row['n_crise']}`")
                st.write(f"💸 Inadimplência: `{fii_row['n_inadimplencia']}`")
                
        with col_f2:
            st.markdown("#### Matriz Risco × Oportunidade por FII")
            # Highlight selected ticker
            fig_scatter = px.scatter(
                fii_signals_df,
                x="risk_score",
                y="opportunity_score",
                hover_name="ticker",
                size="mentions",
                color="segment",
                labels={"risk_score": "Score de Risco", "opportunity_score": "Score de Oportunidade", "mentions": "Menções"},
                title="Posicionamento dos FIIs"
            )
            # Add highlight marker for selected FII
            fig_scatter.add_trace(go.Scatter(
                x=[fii_row["risk_score"]],
                y=[fii_row["opportunity_score"]],
                mode="markers+text",
                marker=dict(color="red", size=20, line=dict(color="white", width=2)),
                text=[fii_row["ticker"]],
                textposition="top center",
                name="FII Selecionado",
                showlegend=True
            ))
            fig_scatter.update_layout(template="plotly_dark", height=400, paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
            st.plotly_chart(fig_scatter, use_container_width=True)
            
        st.markdown("---")
        st.markdown(f"#### 📰 Artigos mais Relevantes sobre {selected_ticker}")
        
        # Find articles mentioning the ticker
        ticker_articles = articles_df[
            articles_df["title"].str.contains(selected_ticker, case=False, na=False) |
            articles_df["text_clean"].str.contains(selected_ticker, case=False, na=False)
        ]
        
        if not ticker_articles.empty:
            st.dataframe(
                ticker_articles[["title", "source_label", "published_at", "sentiment_label", "mi_article_score", "url"]]
                .sort_values(by="mi_article_score", ascending=False).head(10),
                column_config={
                    "title": st.column_config.TextColumn("Título"),
                    "source_label": st.column_config.TextColumn("Fonte"),
                    "published_at": st.column_config.TextColumn("Data"),
                    "sentiment_label": st.column_config.TextColumn("Sentimento"),
                    "mi_article_score": st.column_config.NumberColumn("Score de MI"),
                    "url": st.column_config.LinkColumn("Link")
                },
                use_container_width=True,
                hide_index=True
            )
        else:
            st.write(f"Nenhum artigo encontrado mencionando especificamente {selected_ticker}.")

    # ==========================================
    # TAB 3: MOTOR DE BUSCA
    # ==========================================
    with tab3:
        st.subheader("Motor de Busca Semântica e Relevância Híbrida")
        st.write(
            "Pesquise termos ou tickers para classificar e recuperar os artigos mais relevantes "
            "com base no índice TF-IDF e BM25 construído na Gold layer."
        )
        
        # Search controls
        col_sb1, col_sb2 = st.columns([3, 1])
        with col_sb1:
            search_query = st.text_input("Digite sua pesquisa:", placeholder="Ex: dividend yield HGLG11, crise imobiliária, vacância em shoppings")
        with col_sb2:
            search_method = st.selectbox("Método de busca:", ["Híbrido (BM25 + TF-IDF)", "BM25 (Okapi)", "TF-IDF (Cosine)"])
            
        if search_query:
            try:
                import search_functions
                
                # Dynamic hybrid implementation or standard search functions call
                if search_method == "BM25 (Okapi)":
                    res = search_functions.search_bm25(search_query, top_k=15)
                    res = res.rename(columns={"score_bm25": "score"})
                elif search_method == "TF-IDF (Cosine)":
                    res = search_functions.search_tfidf(search_query, top_k=15)
                    res = res.rename(columns={"score_tfidf": "score"})
                else: # Hybrid
                    # Get top docs from both
                    bm25_res = search_functions.search_bm25(search_query, top_k=100)
                    tfidf_res = search_functions.search_tfidf(search_query, top_k=100)
                    
                    merged = pd.merge(bm25_res, tfidf_res, on=['article_id', 'doc_index'], how='outer')
                    merged['score_bm25'] = merged['score_bm25'].fillna(0)
                    merged['score_tfidf'] = merged['score_tfidf'].fillna(0)
                    
                    max_bm = merged['score_bm25'].max()
                    max_tf = merged['score_tfidf'].max()
                    
                    bm_norm = merged['score_bm25'] / (max_bm if max_bm > 0 else 1)
                    tf_norm = merged['score_tfidf'] / (max_tf if max_tf > 0 else 1)
                    
                    merged['score'] = 0.6 * bm_norm + 0.4 * tf_norm
                    res = merged.sort_values(by='score', ascending=False).head(15)
                
                if not res.empty:
                    # Merge metadata
                    res_merged = pd.merge(res, articles_df, on='article_id', how='inner')
                    
                    st.write(f"### Encontrados {len(res_merged)} resultados:")
                    for idx, row in res_merged.iterrows():
                        sent_label = row["sentiment_label"]
                        sent_color = "positive" if sent_label == "positivo" else "negative" if sent_label == "negativo" else "neutral"
                        
                        score_percentage = min(100, int(row["score"] * 100)) if search_method == "Híbrido (BM25 + TF-IDF)" else int((row["score"] / res["score"].max()) * 100)
                        
                        with st.container():
                            st.markdown(f"#### [{row['title']}]({row['url']})")
                            st.markdown(
                                f"**Fonte:** {row['source_label']} | **Publicado em:** {row['published_at']} | "
                                f"**Sentimento:** <span class='sentiment-{sent_color}'>{sent_label} ({row['polarity_score']:.2f})</span> | "
                                f"**Score de Relevância:** `{row['score']:.4f}`",
                                unsafe_allow_html=True
                            )
                            # Progress bar for relevance score
                            st.progress(score_percentage / 100.0)
                            
                            # Content preview
                            preview = row["text_clean"][:300] + "..." if len(row["text_clean"]) > 300 else row["text_clean"]
                            st.write(f"*{preview}*")
                            st.markdown("<hr style='border: 0.5px solid #30363d;'>", unsafe_allow_html=True)
                else:
                    st.warning("Nenhum resultado encontrado para a sua busca.")
            except Exception as e:
                st.error(f"Erro ao executar busca: {e}")
                import traceback
                st.code(traceback.format_exc())

    # ==========================================
    # TAB 4: ANÁLISE TEXTUAL & FUNIL
    # ==========================================
    with tab4:
        st.subheader("Análise Qualitativa, Word Cloud e Estatísticas do Funil de Marketing")
        
        col_t1, col_t2 = st.columns(2)
        
        with col_t1:
            st.markdown("#### Distribuição por Funil (TOFU / MOFU / BOFU)")
            st.write(
                "Estatísticas dos artigos classificados nos estágios do funil: "
                "TOFU (Descoberta), MOFU (Consideração) e BOFU (Decisão de Compra)."
            )
            
            # Plotly Funnel Chart
            fig_funnel = go.Figure(go.Funnel(
                y=funnel_stats_df["stage"],
                x=funnel_stats_df["n_docs"],
                textinfo="value+percent initial",
                marker={"color": ["#00d2ff", "#a8e6cf", "#ff6b6b"]}
            ))
            fig_funnel.update_layout(template="plotly_dark", height=320, paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
            st.plotly_chart(fig_funnel, use_container_width=True)
            
            # Dataframe summary
            st.dataframe(
                funnel_stats_df,
                column_config={
                    "stage": st.column_config.TextColumn("Estágio do Funil"),
                    "n_queries": st.column_config.NumberColumn("Termos de Busca"),
                    "n_docs": st.column_config.NumberColumn("Quantidade de Docs"),
                    "avg_score": st.column_config.NumberColumn("Média de Relevância"),
                    "avg_polarity": st.column_config.NumberColumn("Média Pol."),
                    "n_positivo": st.column_config.NumberColumn("Positivos"),
                    "n_negativo": st.column_config.NumberColumn("Negativos"),
                    "n_dividendo": st.column_config.NumberColumn("Flags Dividendo"),
                    "n_risco": st.column_config.NumberColumn("Flags Risco")
                },
                hide_index=True,
                use_container_width=True
            )
            
        with col_t2:
            st.markdown("#### Palavras mais Frequentes (Frequência Gold)")
            
            # Search within word cloud
            word_query = st.text_input("Filtrar palavra no vocabulário:", placeholder="Ex: dividendos, shoppings, fii")
            
            wc_filtered = word_cloud_df.copy()
            if word_query:
                wc_filtered = wc_filtered[wc_filtered["term"].str.contains(word_query, case=False, na=False)]
                
            top_words = wc_filtered.head(30)
            
            # Bar chart
            fig_words = px.bar(
                top_words,
                x="count",
                y="term",
                orientation='h',
                color="is_tofu",
                color_discrete_map={True: "#a8e6cf", False: "#00d2ff"},
                labels={"count": "Frequência", "term": "Palavra", "is_tofu": "Termo TOFU"},
                title="Top Palavras Recorrentes"
            )
            fig_words.update_layout(template="plotly_dark", height=380, paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
            fig_words.update_yaxes(autorange="reversed")
            st.plotly_chart(fig_words, use_container_width=True)

    # ==========================================
    # TAB 5: ASSISTENTE IA
    # ==========================================
    with tab5:
        st.subheader("💬 Assistente IA de Inteligência de Mercado FII")
        st.write(
            "Converse com nosso assistente inteligente alimentado pela API do Groq (Llama 3.1 8B). "
            "Ele usará o contexto de artigos recuperados dinamicamente baseados na sua pergunta (RAG) para responder."
        )
        
        # Check API Key availability
        active_key = groq_api_key_input or os.getenv("GROQ_API_KEY", "")
        
        if not active_key:
            st.warning("⚠️ GROQ API Key não encontrada! Por favor, insira sua chave API na barra lateral (Sidebar) para ativar o Chatbot.")
        else:
            # Initialize Chat
            if "messages" not in st.session_state:
                st.session_state.messages = []
                
            # Show historical messages
            for message in st.session_state.messages:
                with st.chat_message(message["role"]):
                    st.markdown(message["content"])
                    
            # User input
            if prompt := st.chat_input("Pergunte algo (ex: Quais os riscos atuais para o segmento de shoppings?):"):
                # Display user message
                with st.chat_message("user"):
                    st.markdown(prompt)
                st.session_state.messages.append({"role": "user", "content": prompt})
                
                # Fetch context using search functions
                context_articles = ""
                try:
                    import search_functions
                    # Get top 3 related articles
                    r_search = search_functions.search_bm25(prompt, top_k=3)
                    if not r_search.empty:
                        # Join with text_clean
                        matched_docs = pd.merge(r_search, articles_df, on='article_id', how='inner')
                        context_pieces = []
                        for idx, row_match in matched_docs.iterrows():
                            context_pieces.append(
                                f"Artigo: {row_match['title']} (Fonte: {row_match['source_label']}, "
                                f"Data: {row_match['published_at']}, Sentimento: {row_match['sentiment_label']})\n"
                                f"Texto: {row_match['text_clean'][:500]}..."
                            )
                        context_articles = "\n\n".join(context_pieces)
                except Exception as e:
                    context_articles = "Erro ao carregar contexto de busca."
                    
                # Call Groq
                with st.chat_message("assistant"):
                    message_placeholder = st.empty()
                    message_placeholder.markdown("*Processando e analisando dados...*")
                    
                    try:
                        import dashboard.chatbot.groq_client as groq_client
                        
                        # Generate answer
                        response = groq_client.chat(prompt, context=context_articles, custom_api_key=active_key)
                        message_placeholder.markdown(response)
                        st.session_state.messages.append({"role": "assistant", "content": response})
                    except Exception as e:
                        message_placeholder.error(f"Erro ao chamar API do Groq: {e}")
                        
else:
    st.info("Aguardando carregamento correto dos datasets...")
