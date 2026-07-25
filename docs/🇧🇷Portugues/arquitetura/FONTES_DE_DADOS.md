<!-- LANGUAGE BUTTONS -->
**\[[🇧🇷 Português](FONTES_DE_DADOS.md)\] \[**[🇬🇧 English](../../🇬🇧English/architecture/DATA_SOURCES.md)**\]**

<br><br>

## [Fontes de Dados e Metodologia de Coleta]()
### Investor Intelligence Platform — FIIs Brasil 🇧🇷

<br><br>

> ⚠️ **Correção de consistência:** uma versão anterior deste documento ainda listava explicações individuais para **Valor Investe** e **The Cap**, mesmo que ambas tenham sido substituídas no início do projeto (Valor Investe → Empiricus; The Cap → Portal do FII) e a tabela de taxonomia principal abaixo já refletisse a lista final de 21 fontes. Esta versão remove as entradas obsoletas e adiciona as explicações que faltavam para Empiricus e Portal do FII.

<br><br>

Este documento descreve a taxonomia oficial de fontes, a convenção de nomenclatura, a estratégia de aquisição, a terminologia de scraping e a lógica de fallback usadas pela plataforma para coletar dados sobre Fundos de Investimento Imobiliário (FIIs) brasileiros.

<br><br>

O objetivo deste arquivo é tornar a camada de coleta metodologicamente transparente. Em vez de tratar todos os inputs monitorados como um corpus de texto genérico, o projeto distingue entre feeds editoriais estruturados, extração de HTML de portais públicos, e ambientes de discussão social comportamental.

<br><br>

## [Taxonomia Oficial de Fontes]()

<br><br>

A plataforma organiza os inputs externos em três grupos oficiais de fonte:

<br><br>

[***1. Fontes Editoriais Oficiais via RSS***]()

<br><br>

Publicadores de notícias financeiras e de investimento cujo conteúdo é coletado via feeds RSS sempre que um feed estável está disponível. RSS é o método de ingestão preferido porque oferece uma forma leve, estruturada e operacionalmente eficiente de coletar artigos recém-publicados, com menor complexidade de parsing e menor fragilidade do que extração de HTML.

<br><br>

[***2. Fontes Editoriais Oficiais via Scraping***]()

<br><br>

Portais editoriais cujo conteúdo relevante é coletado diretamente de páginas HTML públicas quando um feed RSS confiável está indisponível, incompleto, instável, genérico demais, ou insuficientemente alinhado ao escopo de monitoramento de FIIs. Na terminologia do repositório, essas fontes são tratadas via scraping targets, não feed targets.

<br><br>

[***3. Fonte Social Comportamental Oficial***]()

<br><br>

Ambientes de discussão social usados para observar comportamento do investidor, dinâmicas de engajamento, narrativas recorrentes e sinais de sentimento. Na arquitetura atual, o Reddit funciona como a camada comportamental primária que complementa o ecossistema editorial — ver [`MULTI_LLM_FALLBACK.md`](MULTI_LLM_FALLBACK.md) para o padrão análogo de camadas de fallback aplicado à lógica de coleta desta fonte.

<br><br>

## [Terminologia Técnica Recomendada]()

<br><br>

Sempre que o repositório mencionar scraping, a redação técnica preferida é:

<br><br>

- **Listing-Page HTML Scraping**
- **Portal-Level Lightweight Scraping**
- **Rule-Based Public Web Extraction**

<br><br>

Essas expressões são mais precisas do que simplesmente repetir "web scraping" porque deixam claro que o projeto coleta páginas de listagem editorial pública e metadados de artigos usando regras determinísticas de parsing de HTML, em vez de depender primariamente de automação pesada de navegador.

<br><br>

## [Estratégia de Coleta por Tipo de Fonte]()

<br><br>

[***Estratégia RSS-First***]()

<br><br>

A plataforma segue uma política de ingestão RSS-first para fontes editoriais. Quando uma fonte oferece um feed estável, relevante e suficientemente granular, o endpoint RSS é preferido porque reduz o custo de extração, melhora a consistência de ingestão e simplifica a normalização downstream.

<br><br>

[***Scraping como Fallback Controlado***]()

<br><br>

Quando o RSS está indisponível ou inadequado, a plataforma usa extração de HTML controlada de páginas públicas de portais. Este modelo de scraping não pretende simular comportamento humano de navegação; em vez disso, é projetado como uma rotina focada de coleta de metadados, que extrai títulos, links, timestamps, categorias, resumos e outros sinais editoriais observáveis de páginas públicas.

<br><br>

[***Coleta de Fonte Social***]()

<br><br>

Plataformas comportamentais são coletadas por um caminho de lógica separado porque representam dados conversacionais e de comunidade, não publicação editorial institucional. Essa distinção importa porque esclarece por que o Reddit não deve ser agrupado sob a ingestão de portais editoriais.

<br><br>

## [Nomenclatura Oficial por Fonte]()

<br><br>

| # | Fonte | Categoria | Método Primário | Fallback | Endpoint |
|---|---|---|---|---|---|
| 1 | InfoMoney | Editorial | RSS | — | infomoney.com.br/feed/ |
| 2 | Empiricus | Editorial | RSS | Scraping | empiricus.com.br/feed/ |
| 3 | Money Times | Editorial | RSS | — | moneytimes.com.br/feed/ |
| 4 | Seu Dinheiro | Editorial | RSS | — | seudinheiro.com/feed/ |
| 5 | Exame Invest | Editorial | RSS | — | exame.com/feed/ |
| 6 | CNN Brasil Business | Editorial | RSS | — | cnnbrasil.com.br/feed/ |
| 7 | Suno Research | Editorial | RSS (secundário) | Scraping | sunoresearch.com.br/feed/ |
| 8 | E-Investidor Estadão | Editorial | RSS (secundário) | Scraping | einvestidor.estadao.com.br/feed |
| 9 | NeoFeed | Editorial | RSS (secundário) | Scraping | neofeed.com.br/feed/ |
| 10 | Toro Investimentos | Editorial | RSS | Scraping | blog.toroinvestimentos.com.br/feed/ |
| 11 | Funds Explorer | Portal | Scraping | — | fundsexplorer.com.br |
| 12 | Status Invest | Portal | Scraping | — | statusinvest.com.br |
| 13 | Clube FII | Portal | Scraping | — | clubefii.com.br |
| 14 | FIIs.com.br | Portal | Scraping | — | fiis.com.br |
| 15 | Portal do FII | Portal | Scraping | RSS | portaldofii.com.br |
| 16 | Investidor10 | Portal | Scraping | — | investidor10.com.br |
| 17 | Eu Quero Investir | Portal | Scraping | — | euqueroinvestir.com |
| 18 | Bora Investir (B3) | Institucional | Scraping | — | borainvestir.b3.com.br |
| 19 | XP Conteúdos | Institucional | Scraping | — | conteudos.xpi.com.br |
| 20 | Investing Brasil | Portal | Scraping | — | br.investing.com |
| 21 | Reddit / Google News | Social / Comportamental | PRAW (quando disponível) | Google News RSS | `r/investimentos` · `r/farialimabets` · news.google.com |

<br><br>

## [Explicação Fonte a Fonte]()

<br><br>

[***InfoMoney***]()

<br><br>

Nome oficial: **Official Editorial RSS Source — InfoMoney**. Publicador editorial de notícias financeiras ingerido via RSS. Pertence à camada de ingestão estruturada de baixo atrito e faz parte da base primária de monitoramento editorial da plataforma.

<br><br>

[***Empiricus***]()

<br><br>

Nome oficial: **Official Editorial RSS Source — Empiricus**. Método recomendado: RSS primeiro, scraping como fallback. Publicador especializado em pesquisa de investimentos e conteúdo financeiro; substituiu a Valor Investe no início do projeto como fonte com cobertura mais consistente e específica sobre FIIs.

<br><br>

[***Suno Research***]()

<br><br>

Nome oficial: **Official Editorial Source — Suno Research**. Método recomendado: RSS primeiro, scraping como fallback. Publicador especializado em pesquisa de investimentos cujo método preferido é ingestão via feed quando o feed é estável, escopado e operacionalmente útil. Se o feed se tornar inconsistente, a plataforma cai para portal-level lightweight scraping.

<br><br>

[***Investidor10***]()

<br><br>

Nome oficial: **Official Editorial Scraping Source — Investidor10**. Método recomendado: scraping. Portal estruturado de informação de investimentos, monitorado via parsing HTML leve e captura direcionada de metadados.

<br><br>

[***Funds Explorer***]()

<br><br>

Nome oficial: **Official Editorial Scraping Source — Funds Explorer**. Método recomendado: scraping. Portal especializado em FIIs coletado via listing-page HTML scraping — extração direcionada de conteúdo editorial/de portal relevante a FIIs, não automação genérica de navegador.

<br><br>

[***Clube FII***]()

<br><br>

Nome oficial: **Official Editorial Scraping Source — Clube FII**. Método recomendado: scraping. Encaixa-se no modelo portal-level lightweight scraping — uma fonte de domínio especializado onde conteúdo relevante pode ser capturado via parsing determinístico de páginas públicas.

<br><br>

[***Status Invest***]()

<br><br>

Nome oficial: **Official Editorial Scraping Source — Status Invest**. Método recomendado: scraping. Coletado via rule-based public web extraction de páginas estruturadas de portal, especialmente onde os layouts de página tornam a extração de metadados prática e repetível.

<br><br>

[***FIIs.com.br***]()

<br><br>

Nome oficial: **Official Editorial Scraping Source — FIIs.com.br**. Método recomendado: scraping. Portal de nicho setorial incorporado via extração pública de HTML focada em blocos de conteúdo relevantes a FIIs.

<br><br>

[***Money Times***]()

<br><br>

Nome oficial: **Official Editorial RSS Source — Money Times**. Método recomendado: RSS. Fonte editorial baseada em RSS focada em conteúdo de mercado, investimento e negócios.

<br><br>

[***Seu Dinheiro***]()

<br><br>

Nome oficial: **Official Editorial RSS Source — Seu Dinheiro**. Método recomendado: RSS. Publicador voltado a investimentos coletado via RSS.

<br><br>

[***Exame Invest***]()

<br><br>

Nome oficial: **Official Editorial RSS Source — Exame Invest**. Método recomendado: RSS. Expande a perspectiva de negócios e mercado de capitais do repositório — fonte editorial estruturada com relevância financeira e econômica mais ampla.

<br><br>

[***Bora Investir (B3)***]()

<br><br>

Nome oficial: **Official Editorial Scraping Source — Bora Investir B3**. Método recomendado: scraping. Pode existir um endpoint RSS corporativo/institucional, mas como seria mais amplo que o conteúdo editorial de investimento do portal, fazer scraping do próprio portal é a estratégia de aquisição mais precisa.

<br><br>

[***E-Investidor Estadão***]()

<br><br>

Nome oficial: **Official Editorial RSS Source — E-Investidor Estadão**. Método recomendado: RSS primeiro, scraping como fallback. Publicação editorial de investimentos para a qual a ingestão via feed é preferida sempre que o endpoint for relevante, estável e suficientemente granular para as necessidades do projeto.

<br><br>

[***NeoFeed***]()

<br><br>

Nome oficial: **Official Editorial RSS Source — NeoFeed**. Método recomendado: RSS primeiro, scraping como fallback. Fonte editorial de negócios que entra via RSS quando validado, mas permanece elegível para scraping de portal se condições operacionais exigirem.

<br><br>

[***Portal do FII***]()

<br><br>

Nome oficial: **Official Editorial Scraping Source — Portal do FII**. Método recomendado: scraping primeiro, RSS como fallback. Portal editorial especializado em FIIs; substituiu The Cap no início do projeto como fonte com alinhamento temático mais estreito ao escopo de monitoramento de FIIs.

<br><br>

[***Eu Quero Investir***]()

<br><br>

Nome oficial: **Official Editorial Scraping Source — Eu Quero Investir**. Método recomendado: scraping. Fonte editorial web coletada via extração HTML de nível de portal, já que cobertura RSS direta não faz parte de sua arquitetura de ingestão.

<br><br>

[***Toro Investimentos***]()

<br><br>

Nome oficial: **Official Editorial Source — Toro Investimentos**. Método recomendado: RSS primeiro, scraping como fallback. Blog editorial de uma plataforma de investimentos cujo feed é o ponto de entrada preferido, com scraping de portal como fallback controlado quando o feed está instável.

<br><br>

[***Investing Brasil***]()

<br><br>

Nome oficial: **Official Editorial Scraping Source — Investing Brasil**. Método recomendado: scraping. Vertical editorial focada no Brasil de um portal global de notícias financeiras, coletada via listing-page scraping dada a ausência de um feed RSS escopado para conteúdo relevante a FIIs.

<br><br>

[***CNN Brasil Business***]()

<br><br>

Nome oficial: **Official Editorial RSS Source — CNN Brasil Business**. Método recomendado: RSS. Contribui com cobertura macroeconômica e de negócios via ingestão orientada a feed — útil para contextualizar conversas sobre FIIs dentro do sentimento de mercado mais amplo.

<br><br>

[***XP Conteúdos***]()

<br><br>

Nome oficial: **Official Editorial Scraping Source — XP Conteúdos**. Método recomendado: scraping. Hub de conteúdo institucional coletado via extração HTML de nível de portal, dada a ausência de um feed RSS público escopado.

<br><br>

[***Reddit***]()

<br><br>

Nome oficial: **Official Behavioral Social Source — Reddit**. Método recomendado: pipeline de ingestão comportamental/social. Explicado separadamente da mídia editorial porque sua função é capturar discussão social, padrões de engajamento, narrativas de investidores e sentimento de comunidade, não publicação jornalística formal. Foco atual: `r/investimentos` e `r/farialimabets`, com fallback em 3 níveis (PRAW → Google News RSS → parquet congelado) — ver [`BRONZE_SCHEMA.md`](BRONZE_SCHEMA.md) para os valores de `ingestion_method` que isso produz.

<br><br>

## [Explicação da Técnica de Scraping]()

<br><br>

Quando feeds RSS estão indisponíveis, incompletos, instáveis, ou editorialmente desalinhados do escopo de monitoramento de FIIs, a plataforma usa **Listing-Page HTML Scraping** (também chamado **Portal-Level Lightweight Scraping**) — uma abordagem de extração pública baseada em regras, projetada para coletar metadados de artigos e sinais editoriais observáveis de páginas publicamente acessíveis. Este método prioriza parsing determinístico, baixa complexidade operacional e lógica de aquisição sustentável, em vez de automação pesada de navegador.

<br><br>

## [Lógica de Fallback]()

<br><br>

1. **Método primário: ingestão RSS**, sempre que um feed estável e relevante está disponível.
2. **Método secundário: Listing-Page HTML Scraping**, quando o RSS está indisponível, instável, amplo demais, ou insuficiente para as necessidades de monitoramento editorial.
3. **Retry específico por fonte e tolerância de parser** para falhas transitórias, mudanças de layout, e metadados incompletos.
4. **Camada de normalização e deduplicação** para evitar artigos duplicados entre feeds, portais e fontes sociais (ver [`BRONZE_SCHEMA.md`](BRONZE_SCHEMA.md) para deduplicação via `content_hash`).
5. **Datasets de fallback congelados ou controlados** para plataformas sociais ou externas quando a coleta ao vivo está com rate-limit, indisponível, ou intencionalmente desligada durante execução acadêmica ou local.

<br><br>

## [Ver Também]()

<br><br>

- **[`DOCUMENTO_OFICIAL.md`](../documento_oficial/DOCUMENTO_OFICIAL.md)**, seção 8 — tabela-resumo condensada das 21 fontes
- **[`BRONZE_SCHEMA.md`](BRONZE_SCHEMA.md)** — os campos `source`, `source_type` e `ingestion_method` que esses métodos produzem
- **[`DATA_LINEAGE.md`](DATA_LINEAGE.md)** — onde esta camada de coleta se encaixa no fluxo de dados de ponta a ponta

<br><br>

---

<br><br>

*Fontes de Dados e Metodologia de Coleta v1.1.0 · Investor Intelligence Platform FIIs Brasil*
