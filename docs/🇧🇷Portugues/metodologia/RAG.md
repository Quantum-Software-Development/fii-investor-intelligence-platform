<!-- LANGUAGE BUTTONS -->
**\[[🇧🇷 Português](RAG.md)\] \[**[🇬🇧 English](../../🇬🇧English/methodology/RAG.md)**\]**

<br><br>

## [🤖 RAG (Retrieval-Augmented Generation)]()
### Investor Intelligence Platform — FIIs Brasil 🇧🇷

<br><br>

## [📌 Visão Geral]()

<br><br>

**RAG (Retrieval-Augmented Generation)** é uma arquitetura que combina **recuperação de informação (retrieval)** com **modelos de linguagem (LLMs)** para gerar respostas mais precisas, contextualizadas e confiáveis.

<br><br>

Diferente de modelos isolados, o RAG consulta dados externos antes de responder, reduzindo erros e alucinações.

<br><br>

## [🧠 Papel no Pipeline]()

<br><br>

No projeto, o RAG é a camada final responsável por:

<br><br>

- Transformar dados em respostas interpretáveis
- Utilizar contexto recuperado (Hybrid Retrieval)
- Gerar insights acionáveis

<br><br>

## [🏗️ Pipeline do RAG]()

<br><br>

```mermaid
%%{init:{
'theme':'dark',
'themeVariables':{
'background':'#090d13',
'primaryTextColor':'#F5F7FA',
'lineColor':'#2dd4bf'
}}}%%

graph TD

A["User Query"]:::setup

B["Hybrid Retrieval<br/>BM25 + FAISS"]:::gold

C["Top-K Documents"]:::silver

D["Context Injection"]:::dash

E["LLM<br/>Groq + Gemini"]:::llm

F["Generated Answer"]:::primary

A --> B --> C --> D --> E --> F

classDef setup fill:#0d2137,stroke:#00d2ff,color:#F5F7FA,stroke-width:2.5px;
classDef bronze fill:#2a1512,stroke:#a85a4a,color:#F5F7FA,stroke-width:2.5px;
classDef silver fill:#1b2430,stroke:#b0b7c3,color:#F5F7FA,stroke-width:2.5px;
classDef gold fill:#2a2208,stroke:#e6c35a,color:#F5F7FA,stroke-width:2.5px;
classDef dash fill:#06363d,stroke:#2dd4bf,color:#F5F7FA,stroke-width:2.5px;
classDef llm fill:#231433,stroke:#b56cff,color:#F5F7FA,stroke-width:2.5px;
classDef primary fill:#14331d,stroke:#2ecc71,color:#F5F7FA,stroke-width:2.5px;
```

<br><br>

## [⚙️ Como Funciona]()

<br><br>

[***1. Query do Usuário***]()

<br><br>

- O usuário faz uma pergunta
- Exemplo: "Quais FIIs estão com risco de vacância?"

<br><br>

[***2. Recuperação de Contexto***]()

<br><br>

- Hybrid Retrieval (BM25 + FAISS)
- Seleção dos documentos mais relevantes

<br><br>

[***3. Injeção de Contexto***]()

<br><br>

- Os documentos são inseridos no prompt do modelo
- Criação de contexto estruturado

<br><br>

[***4. Geração da Resposta***]()

<br><br>

- O LLM gera a resposta com base no contexto
- Resultado mais preciso e fundamentado

<br><br>

## [🔗 Integração com Outras Técnicas]()

<br><br>

- **FAISS** → busca semântica
- **BM25 / TF-IDF** → precisão lexical
- **Embeddings** → representação de significado
- **Hybrid Retrieval** → combinação otimizada

<br><br>

## [🧠 Aplicação no Projeto (FIIs)]()

<br><br>

- Análise de notícias financeiras
- Detecção de risco (vacância, inadimplência)
- Geração de insights de investimento
- Suporte à decisão estratégica

<br><br>

## [🚀 Vantagens]()

<br><br>

- Redução de alucinações
- Maior precisão
- Respostas explicáveis
- Integração com dados reais

<br><br>

## [⚠️ Limitações]()

<br><br>

- Dependência da qualidade do retrieval
- Custo computacional maior
- Necessidade de engenharia de prompt

<br><br>

## [📚 Referência]()

<br><br>

Ver: `docs/Conceptual Foundations.md`

<br><br>

## [🧾 Conclusão]()

<br><br>

O RAG transforma o sistema em uma **plataforma de inteligência**, onde dados são convertidos em conhecimento acionável.

<br><br>

---

<br><br>

*RAG (Retrieval-Augmented Generation) v1.0.0 · Investor Intelligence Platform FIIs Brasil*
