# Data Sources and Collection Methodology

This document describes the official source taxonomy, naming convention, acquisition strategy, scraping terminology, and fallback logic used by the Investor Intelligence Platform for Brazilian Real Estate Investment Funds (FIIs).

The goal of this file is to make the collection layer methodologically transparent. Instead of treating all monitored inputs as a generic text corpus, the project distinguishes between structured editorial feeds, public-portal HTML extraction, and behavioral social-discussion environments.

<br><br>

## Official Source Taxonomy

The platform organizes external inputs into three official source groups:

### 1. Official Editorial RSS Sources

These are financial and investment news publishers whose content is collected through RSS feeds whenever a stable feed is available. RSS is the preferred ingestion method because it provides a lightweight, structured, and operationally efficient way to collect newly published articles with lower parsing complexity and lower fragility than HTML extraction.

<br>

### 2. Official Editorial Scraping Sources

These are editorial portals whose relevant content is collected directly from public HTML pages when a reliable RSS feed is unavailable, incomplete, unstable, too generic, or insufficiently aligned with the FIIs monitoring scope. In repository terminology, these sources are handled through scraping targets rather than feed targets.

<br>

### 3. Official Behavioral Social Source

This group covers social-discussion environments used to observe investor behavior, engagement dynamics, recurring narratives, and sentiment signals. In the current architecture, Reddit functions as the primary behavioral discussion layer that complements the editorial ecosystem.

<br><br>

## Recommended Technical Terminology

Wherever the repository mentions scraping, the preferred technical wording is:

- **Listing-Page HTML Scraping**  
- **Portal-Level Lightweight Scraping**  
- **Rule-Based Public Web Extraction**

These expressions are more precise than simply repeating “web scraping” because they make it clear that the project collects public editorial listing pages and article metadata using deterministic HTML parsing rules, rather than relying primarily on heavy browser automation.


<br><br>

## Collection Strategy by Source Type

<br>

### RSS-first strategy

The platform follows an RSS-first ingestion policy for editorial sources. When a source offers a stable, relevant, and sufficiently granular feed, the RSS endpoint is preferred because it reduces extraction cost, improves ingestion consistency, and simplifies downstream normalization.

<br>

### Scraping as a controlled fallback

When RSS is unavailable or inadequate, the platform uses controlled HTML extraction from public portal pages. This scraping model is not intended to simulate human browsing behavior; instead, it is designed as a focused metadata collection routine that extracts titles, links, timestamps, categories, excerpts, and other observable editorial signals from public pages.

<br>

### Social-source collection

Behavioral platforms are collected through a separate logic path because they represent conversational and community data rather than institutional editorial publication. This distinction is important because it clarifies why Reddit should not be grouped under editorial portal ingestion.



<br><br>

## Official Naming by Source

Below is the recommended official naming convention for the sources already mapped in the project. Methods are marked as planned or to be defined when implementation details are still under construction.

| Internal role        | Official name for README                             | Collection method                                   | Technical note                                                                      |
|----------------------|------------------------------------------------------|-----------------------------------------------------|-------------------------------------------------------------------------------------|
| InfoMoney            | Official Editorial RSS Source — InfoMoney           | RSS (planned)                                       | Financial-news publisher; preferred via structured feed ingestion                  |
| Suno Research        | Official Editorial Source — Suno Research           | RSS if validated; Scraping fallback (planned)       | Specialized investment research; prefer feed when stable and scoped                |
| Investidor10         | Official Editorial Scraping Source — Investidor10   | Scraping (planned)                                  | Structured investment-information portal; listing-page HTML extraction             |
| Funds Explorer       | Official Editorial Scraping Source — Funds Explorer | Scraping (planned)                                  | Specialized FII portal; portal-level HTML extraction                               |
| Clube FII            | Official Editorial Scraping Source — Clube FII      | Scraping (planned)                                  | Sector portal; rule-based public web extraction                                    |
| Status Invest        | Official Editorial Scraping Source — Status Invest  | Scraping (planned)                                  | Portal with structured pages; listing-page HTML scraping                           |
| FIIs.com.br          | Official Editorial Scraping Source — FIIs.com.br    | Scraping (planned)                                  | Niche FII portal; public editorial/content extraction                              |
| Money Times          | Official Editorial RSS Source — Money Times         | RSS (planned)                                       | Market and investment news; structured feed ingestion                              |
| Seu Dinheiro         | Official Editorial RSS Source — Seu Dinheiro        | RSS (planned)                                       | Investment-oriented publisher; RSS-based editorial monitoring                      |
| Exame Invest         | Official Editorial RSS Source — Exame Invest        | RSS (planned)                                       | Financial and business content ingestion via RSS                                   |
| Bora Investir (B3)   | Official Editorial Scraping Source — Bora Investir B3| Scraping by default; RSS if scoped (planned)       | Prefer scraping when corporate feeds are too broad                                 |
| E-Investidor Estadão | Official Editorial RSS Source — E-Investidor Estadão | RSS if validated; Scraping fallback (planned)       | Validate feed relevance and stability                                              |
| Valor Investe        | Official Editorial RSS Source — Valor Investe       | RSS (planned)                                       | Investment journalism outlet; structured investment news feed                      |
| NeoFeed              | Official Editorial RSS Source — NeoFeed             | RSS if validated; Scraping fallback (planned)       | Business and tech coverage; prefer feed, keep HTML fallback                        |
| The Cap              | Official Editorial Scraping Source — The Cap        | Scraping (planned)                                  | Editorial portal; listing/article metadata extraction                              |
| Eu Quero Investir    | Official Editorial Scraping Source — Eu Quero Investir | Scraping (planned)                               | Editorial web source; portal-level HTML extraction                                 |
| Toro Investimentos   | Official Editorial Source — Toro Investimentos      | To be defined                                       | Included in fixed scope; acquisition method to be documented                       |
| Investing Brasil     | Official Editorial Source — Investing Brasil        | To be defined                                       | Included in fixed scope; acquisition method to be documented                       |
| CNN Brasil Business  | Official Editorial RSS Source — CNN Brasil Business | RSS (planned)                                       | Macroeconomic and business coverage; feed-based news ingestion                     |
| XP Conteúdos         | Official Editorial Source — XP Conteúdos            | To be defined                                       | Included in fixed scope; acquisition method to be documented                       |
| Reddit               | Official Behavioral Social Source — Reddit          | API/dataset pipeline (planned)                      | Social-discussion layer (r/investimentos, r/farialimabets); behavioral data        |


<br><br>

## Source-by-Source Explanation

### InfoMoney
Official name: **Official Editorial RSS Source — InfoMoney**.  
This source should be described as an editorial financial-news publisher ingested through RSS. It belongs to the low-friction structured ingestion layer and should be referenced as part of the platform's primary editorial monitoring base

<br>

### Suno Research
Official name: **Official Editorial Source — Suno Research**.  
Recommended method: RSS first, scraping fallback. This source should be described as a specialized investment-research publisher whose preferred method is feed ingestion when the feed is stable, scoped, and operationally useful. If the feed becomes inconsistent, the platform should fall back to portal-level lightweight scraping.

<br>

### Investidor10
Official name: **Official Editorial Scraping Source — Investidor10**.  
Recommended method: scraping. This source is well described as a structured investment-information portal monitored through lightweight HTML parsing and targeted metadata capture.

<br>

### Funds Explorer
Official name: **Official Editorial Scraping Source — Funds Explorer**.  
Recommended method: scraping. This source should be described as a specialized FII portal collected through listing-page HTML scraping. The wording should emphasize targeted extraction of public editorial or portal content relevant to FIIs, rather than generic browser automation

<br>

### Clube FII
Official name: **Official Editorial Scraping Source — Clube FII**.  
Recommended method: scraping. This source fits the portal-level lightweight scraping model because it is a specialized domain source where relevant content can be captured through deterministic parsing of public pages.

<br>

### Status Invest
Official name: **Official Editorial Scraping Source — Status Invest**.  
Recommended method: scraping. This source should be described as being collected through rule-based public web extraction from structured portal pages, especially where page layouts make metadata extraction practical and repeatable.

<br>

### FIIs.com.br
Official name: **Official Editorial Scraping Source — FIIs.com.br**.  
Recommended method: scraping. This source can be described as a niche sector portal incorporated through public HTML extraction focused on FII-relevant content blocks.

<br>

### Money Times
Official name: **Official Editorial RSS Source — Money Times**.  
Recommended method: RSS. This source should be positioned as an RSS-based editorial source focused on market, investment, and business content.

<br>

### Seu Dinheiro
Official name: **Official Editorial RSS Source — Seu Dinheiro**.  
Recommended method: RSS. This source is best documented as an investment-oriented publisher collected through RSS.

<br>

### Exame Invest
Official name: **Official Editorial RSS Source — Exame Invest**.  
Recommended method: RSS. This source expands the business and capital-markets perspective of the repository and should be framed as a structured editorial source with broader financial and economic relevance.

<br>

### Bora Investir (B3)
Official name: **Official Editorial Scraping Source — Bora Investir B3**.  
Recommended method: scraping by default, RSS only when editorial scope is confirmed. A corporate or institutional RSS endpoint may exist, but if that feed is broader than the portal's editorial investment content, scraping the portal itself is the more precise acquisition strategy.

### E-Investidor Estadão
Official name: **Official Editorial RSS Source — E-Investidor Estadão**.  
Recommended method: RSS first, scraping fallback. This source should be described as an editorial investment publication for which feed ingestion is preferred whenever the endpoint is relevant, stable, and sufficiently granular for the project's needs.

<br>

### Valor Investe
Official name: **Official Editorial RSS Source — Valor Investe**.  
Recommended method: RSS. This source represents a traditional investment journalism outlet collected through feed-based ingestion.

<br>

### NeoFeed
Official name: **Official Editorial RSS Source — NeoFeed**.  
Recommended method: RSS first, scraping fallback. It can be positioned as an editorial-business source that should enter through RSS when validated, but remain eligible for portal scraping if operational conditions require it.

<br>

### The Cap
Official name: **Official Editorial Scraping Source — The Cap**.  
Recommended method: scraping. This source should be documented as an editorial portal collected through listing-page scraping or article-metadata extraction, depending on the specific page structure exposed publicly.

<br>

### Eu Quero Investir
Official name: **Official Editorial Scraping Source — Eu Quero Investir**.  
Recommended method: scraping. This is an editorial web source collected through portal-level HTML extraction when direct RSS coverage is not part of the ingestion architecture.

<br>

### Toro Investimentos
Official name: **Official Editorial Source — Toro Investimentos**.  
Method: to be defined. This source is part of the fixed scope; its concrete acquisition strategy should be documented as the pipeline evolves.

<br>

### Investing Brasil
Official name: **Official Editorial Source — Investing Brasil**.  
Method: to be defined. This source is included in the fixed scope and should have its method (RSS or scraping) explicitly defined in future updates.

<br>

### CNN Brasil Business
Official name: **Official Editorial RSS Source — CNN Brasil Business**.  
Recommended method: RSS. This source contributes macroeconomic and business coverage through feed-driven ingestion and is useful for contextualizing FIIs conversations within broader market sentiment.

<br>

### XP Conteúdos
Official name: **Official Editorial Source — XP Conteúdos**.  
Method: to be defined. This is a scoped editorial source whose ingestion method will be documented alongside implementation.

<br>

### Reddit
Official name: **Official Behavioral Social Source — Reddit**.  
Recommended method: behavioral/social ingestion pipeline. This source should be explained separately from editorial media because its function is to capture social discussion, engagement patterns, investor narratives, and community sentiment rather than formal journalistic publication. Current focus: r/investimentos and r/farialimabets.

<br><br>

## Scraping Technique Explanation 

When RSS feeds are unavailable, incomplete, unstable, or editorially misaligned with the FIIs monitoring scope, the platform uses **Listing-Page HTML Scraping** (also referred to as **Portal-Level Lightweight Scraping**), a rule-based public-web extraction approach designed to collect article metadata and observable editorial signals from publicly accessible pages. This method prioritizes deterministic parsing, low operational complexity, and maintainable acquisition logic over heavy browser automation.

<br><br>

## Fallback Logic

1. **Primary method: RSS ingestion** whenever a stable and relevant feed is available.  
2. **Secondary method: Listing-Page HTML Scraping** when RSS is unavailable, unstable, too broad, or insufficient for editorial monitoring needs.  
3. **Source-specific retry and parser tolerance** for transient failures, layout shifts, and incomplete metadata.  
4. **Normalization and deduplication layer** to avoid duplicate articles across feeds, portals, and social sources.  
5. **Frozen or controlled fallback datasets** for social or external platforms when live collection is rate-limited, unavailable, or intentionally disabled during academic or local execution.

