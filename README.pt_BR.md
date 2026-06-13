
<!-- ======================================= ⚡️ Start DEFAULT HEADER ===========================================  -->

<!-- ========= START LANGUAGE BUTTON ========= -->
**[[🇧🇷 Português](README.pt_BR.md)] [**[🇬🇧 English](README.md)**]**

<br><br>
<!-- ========= END LANGUAGE BUTTON ========= -->

<!-- ========= START REPO TITLE ========= -->










<br><br>
<br><br>
<br><br>
<br><br>
<br><br>
<br><br>
<br><br>
<br><br>


## [Arquitetura e Pipeline]()

### ***Visão Macro+++

<br><br>

```mermaid
flowchart LR

    classDef source fill:#0f172a,stroke:#22d3ee,color:#ffffff,stroke-width:2px;
    classDef bronze fill:#1e293b,stroke:#22d3ee,color:#ffffff,stroke-width:2px;
    classDef silver fill:#334155,stroke:#22d3ee,color:#ffffff,stroke-width:2px;
    classDef gold fill:#475569,stroke:#22d3ee,color:#ffffff,stroke-width:2px;
    classDef serving fill:#0f172a,stroke:#06b6d4,color:#ffffff,stroke-width:3px;

    A["📡 21 Fontes Monitoradas<br/>6 RSS + 4 RSS Supl.<br/>10 Portais + Reddit"]

    subgraph Bronze["🥉 Bronze Layer"]
        B["Raw External Data<br/>Schema 17 campos<br/>SHA-256 article_id<br/>Parquet Snappy"]
    end

    subgraph Silver["🥈 Silver Layer"]
        C["Data Cleaning<br/>Quality Gates"]
        D["NB03<br/>MapReduce"]
        E["NB04<br/>TF-IDF + BM25"]
        F["NB05<br/>Sentiment Analysis"]
    end

    subgraph Gold["🥇 Gold Layer"]
        G["MI Signals<br/>Top Articles<br/>Marketing Funnel"]
    end

    subgraph Dashboard["📊 Dashboard Datasets"]
        H["Analytics Views<br/>KPIs & Insights"]
    end

    subgraph Serving["🚀 Serving Layer"]
        I["FastAPI"]
        J["Streamlit"]
        K["Groq Chatbot<br/>Llama 3.1"]
    end

    A --> B
    B --> C
    C --> D
    C --> E
    C --> F

    D --> G
    E --> G
    F --> G

    G --> H

    H --> I
    H --> J

    I --> K
    J --> K

    class A source
    class B bronze
    class C,D,E,F silver
    class G gold
    class H,I,J,K serving

    linkStyle default stroke:#22d3ee,stroke-width:2px
```

<br><br>


## [Official Data Collection — 21 Monitored Sources]()

<br><br>


| #  | Portal/Fonte                                   | Tipo                    | Método principal                    | Fallback     | URL base / endpoint de referência        |
| -- | ---------------------------------------------- | ----------------------- | ----------------------------------- | ------------ | ---------------------------------------- |
| 1  | InfoMoney                                      | Editorial               | RSS primário                        | —            | infomoney.com.br/feed/                   |
| 2  | Empiricus                                      | Editorial               | RSS primário                        | Scraping     | empiricus.com.br/feed/                   |
| 3  | Money Times                                    | Editorial               | RSS primário                        | —            | moneytimes.com.br/feed/                  |
| 4  | Seu Dinheiro                                   | Editorial               | RSS primário                        | —            | seudinheiro.com/feed/                    |
| 5  | Exame Invest                                   | Editorial               | RSS primário                        | —            | exame.com/feed/                          |
| 6  | CNN Brasil Business                            | Editorial               | RSS primário                        | —            | cnnbrasil.com.br/feed/                   |
| 7  | Suno Research                                  | Editorial               | RSS suplementar                     | —            | sunoresearch.com.br/feed/                |
| 8  | E-Investidor Estadão                           | Editorial               | RSS suplementar                     | —            | einvestidor.estadao.com.br/feed          |
| 9  | NeoFeed                                        | Editorial               | RSS suplementar                     | —            | neofeed.com.br/feed/                     |
| 10 | Toro Investimentos                             | Editorial               | RSS suplementar                     | Scraping     | blog.toroinvestimentos.com.br/feed/      |
| 11 | Funds Explorer                                 | Portal                  | Scraping                            | —            | fundsexplorer.com.br/ranking             |
| 12 | Status Invest                                  | Portal                  | Scraping                            | —            | statusinvest.com.br/fundos-imobiliarios  |
| 13 | Clube FII                                      | Portal                  | Scraping                            | —            | clubefii.com.br                          |
| 14 | FIIs.com.br                                    | Portal                  | Scraping                            | —            | fiis.com.br                              |
| 15 | Portal do FII                                  | Portal                  | Scraping                            | RSS fallback | portaldofii.com.br                       |
| 16 | Investidor10                                   | Portal                  | Scraping                            | —            | investidor10.com.br/fiis/                |
| 17 | Eu Quero Investir                              | Portal                  | Scraping                            | —            | euqueroinvestir.com/fundos-imobiliarios/ |
| 18 | Bora Investir (B3)                             | Portal                  | Scraping                            | —            | borainvestir.b3.com.br                   |
| 19 | XP Conteúdos                                   | Portal                  | Scraping                            | —            | conteudos.xpi.com.br                     |
| 20 | Investing Brasil                               | Portal                  | Scraping                            | —            | br.investing.com/news/stock-market-news  |
| 21 | Reddit (`r/investimentos` e `r/farialimabets`) | Social / comportamental | PRAW → API pública → frozen parquet | 3 níveis     | reddit.com / JSON público / PRAW         |


<br><br>
