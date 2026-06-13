
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



# 🏗️ Arquitetura & Pipeline de Dados

<br><br>

## ⚡ 1. Visão Geral do Sistema

O sistema foi projetado como um **pipeline multicamadas de inteligência de dados**, transformando conteúdo financeiro não estruturado em insights acionáveis e respostas impulsionadas por IA.

<br>

```mermaid
flowchart LR

    classDef source fill:#0f172a,stroke:#22d3ee,color:#ffffff,stroke-width:2px;
    classDef bronze fill:#1e293b,stroke:#22d3ee,color:#ffffff,stroke-width:2px;
    classDef silver fill:#334155,stroke:#22d3ee,color:#ffffff,stroke-width:2px;
    classDef gold fill:#475569,stroke:#22d3ee,color:#ffffff,stroke-width:2px;
    classDef serving fill:#0f172a,stroke:#06b6d4,color:#ffffff,stroke-width:3px;

    A["📡 21 Fontes Monitoradas<br/>6 RSS Primários + 4 RSS de Backup<br/>10 Portais Web + Reddit"]

    subgraph Bronze["🥉 Camada Bronze — Ingestão Bruta"]
        B["Dados Externos Brutos<br/>Schema Padronizado de 17 Campos<br/>article_id com SHA-256<br/>Armazenado em Parquet (Snappy)"]
    end

    subgraph Silver["🥈 Camada Silver — Processamento & NLP"]
        C["Limpeza e Validação de Dados<br/>Quality Gates"]
        D["NB03 — Processamento MapReduce"]
        E["NB04 — Indexação TF-IDF & BM25"]
        F["NB05 — Análise de Sentimento"]
    end

    subgraph Gold["🥇 Camada Gold — Inteligência"]
        G["Sinais de Inteligência de Mercado<br/>Artigos Mais Relevantes<br/>Recursos do Funil de Marketing"]
    end

    subgraph Dashboard["📊 Camada Analítica"]
        H["Visões de Dados Curadas<br/>KPIs & Insights"]
    end

    subgraph Serving["🚀 Camada de Servição"]
        I["FastAPI (Camada de API)"]
        J["Streamlit (Interface do Dashboard)"]
        K["Interface LLM<br/>Groq + Llama 3.1"]
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
````

<br><br>

## 2. [Fontes de Dados — 21 Canais Monitorados]()

O sistema ingere continuamente dados de um conjunto diversificado de **fontes editoriais, institucionais e comportamentais**, garantindo tanto profundidade informacional quanto cobertura de sentimento.

<br><br>


| #  | [Fonte]()                                     | [Categoria]()  | [Método Principal]() | [Fallback]() | [Endpoint]()                        |
| -- | --------------------------------------------- | -------------- | -------------------- | ------------ | ----------------------------------- |
| 1  | [InfoMoney]()                                 | Editorial      | RSS                  | —            | infomoney.com.br/feed/              |
| 2  | [Empiricus]()                                 | Editorial      | RSS                  | Scraping     | empiricus.com.br/feed/              |
| 3  | [Money Times]()                               | Editorial      | RSS                  | —            | moneytimes.com.br/feed/             |
| 4  | [Seu Dinheiro]()                              | Editorial      | RSS                  | —            | seudinheiro.com/feed/               |
| 5  | [Exame Invest]()                              | Editorial      | RSS                  | —            | exame.com/feed/                     |
| 6  | [CNN Brasil Business]()                       | Editorial      | RSS                  | —            | cnnbrasil.com.br/feed/              |
| 7  | [Suno Research]()                             | Editorial      | RSS (Secundário)     | —            | sunoresearch.com.br/feed/           |
| 8  | [E-Investidor]()                              | Editorial      | RSS (Secundário)     | —            | einvestidor.estadao.com.br/feed     |
| 9  | [NeoFeed]()                                   | Editorial      | RSS (Secundário)     | —            | neofeed.com.br/feed/                |
| 10 | [Toro Investimentos]()                        | Editorial      | RSS                  | Scraping     | blog.toroinvestimentos.com.br/feed/ |
| 11 | [Funds Explorer]()                            | Portal         | Scraping             | —            | fundsexplorer.com.br                |
| 12 | [Status Invest]()                             | Portal         | Scraping             | —            | statusinvest.com.br                 |
| 13 | [Clube FII]()                                 | Portal         | Scraping             | —            | clubefii.com.br                     |
| 14 | [FIIs.com.br]()                               | Portal         | Scraping             | —            | fiis.com.br                         |
| 15 | [Portal do FII]()                             | Portal         | Scraping             | RSS          | portaldofii.com.br                  |
| 16 | [Investidor10]()                              | Portal         | Scraping             | —            | investidor10.com.br                 |
| 17 | [Eu Quero Investir]()                         | Portal         | Scraping             | —            | euqueroinvestir.com                 |
| 18 | [Bora Investir (B3)]()                        | Institucional  | Scraping             | —            | borainvestir.b3.com.br              |
| 19 | [XP Conteúdos]()                              | Institucional  | Scraping             | —            | conteudos.xpi.com.br                |
| 20 | [Investing Brasil]()                          | Portal         | Scraping             | —            | br.investing.com                    |
| 21 | [Reddit (r/investimentos, r/farialimabets)]() | Comportamental | API (PRAW)           | Backup JSON  | reddit.com                          |

<br><br>

## 3. [Arquitetura de Servição — FastAPI + RAG]()

O sistema expõe inteligência por meio de uma arquitetura **Retrieval-Augmented Generation (RAG)**.

```text
Pipeline de Dados → Banco Vetorial → FastAPI → LLM → Usuário
```

<br><br>

## 4. [Estrutura do Projeto]()

```text
app/
├── main.py
├── api/
│   └── routes.py
├── services/
│   ├── retrieval.py
│   ├── embeddings.py
│   ├── llm.py
├── models/
│   └── schemas.py
├── db/
│   └── vector_store.py
├── core/
│   └── config.py
```

<br><br>

## 5. [Camada de API (FastAPI)]()

<br>

## 6. [Endpoint Principal — Consulta Semântica]()

<br>

## 7. [Camada de Recuperação (RAG)]()

<br>

## 8. [Camada de Embeddings]()

<br>

## 9. [Banco Vetorial (FAISS)]()

<br>

## 10. [Camada de Geração LLM]()

<br>

## 11. [Fluxo End-to-End]()

<br>

| [Camada]()    | [Função]()                           |
| ------------- | ------------------------------------ |
| 🥉 [Bronze]() | Ingestão e armazenamento bruto       |
| 🥈 [Silver]() | Limpeza de dados e processamento NLP |
| 🥇 [Gold]()   | Geração e classificação de sinais    |
| [RAG]()       | Recuperação semântica                |
| [FastAPI]()   | Interface da API                     |
| [LLM]()       | Raciocínio em linguagem natural      |

<br><br>

## 12. [Exemplo de Consulta]()

<br>

```json
{
  "question": "Qual é o sentimento atual dos investidores em relação aos FIIs logísticos?"
}
```

<br>

➠ [**Resposta:**]()

```json
{
  "answer": "Dados recentes indicam um sentimento moderadamente positivo impulsionado por rendimentos estáveis de dividendos e taxas de ocupação."
}
```

<br>

## [Nota Final]()

Esta arquitetura transforma um pipeline de dados tradicional em um **sistema full-stack de inteligência artificial**, permitindo:

[*]() busca semântica <br>
[*]() sentimento do investidor <br>
[*]() insights em tempo real <br>
[*]() interação em linguagem natural

<br><br>



