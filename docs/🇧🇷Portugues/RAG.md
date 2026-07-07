# 🤖 RAG (Retrieval-Augmented Generation)

## 📌 Visão Geral

**RAG (Retrieval-Augmented Generation)** é uma arquitetura que combina **recuperação de informação (retrieval)** com **modelos de linguagem (LLMs)** para gerar respostas mais precisas, contextualizadas e confiáveis.<br><br>

Diferente de modelos isolados, o RAG consulta dados externos antes de responder, reduzindo erros e alucinações.<br><br>

<br><br>

## 🧠 Papel no Pipeline

No projeto, o RAG é a camada final responsável por:<br><br>

* Transformar dados em respostas interpretáveis<br>
* Utilizar contexto recuperado (Hybrid Retrieval)<br>
* Gerar insights acionáveis<br><br>

<br><br>

## 🏗️ Pipeline do RAG

<br><br>

```mermaid 
graph TD
    A["User Query"] --> B["Hybrid Retrieval (BM25 + FAISS)"]
    B --> C["Top-K Documents"]
    C --> D["Context Injection"]
    D --> E["LLM Processing"]
    E --> F["Generated Answer"]
```

<br><br>

## ⚙️ Como Funciona

### 1. Query do Usuário

* O usuário faz uma pergunta<br>
* Exemplo: “Quais FIIs estão com risco de vacância?”<br><br>

<br><br>

### 2. Recuperação de Contexto

* Hybrid Retrieval (BM25 + FAISS)<br>
* Seleção dos documentos mais relevantes<br><br>

<br><br>

### 3. Injeção de Contexto

* Os documentos são inseridos no prompt do modelo<br>
* Criação de contexto estruturado<br><br>


<br><br>

### 4. Geração da Resposta

* O LLM gera a resposta com base no contexto<br>
* Resultado mais preciso e fundamentado<br><br>

<br><br>

## 🔗 Integração com Outras Técnicas

* **FAISS** → busca semântica<br>
* **BM25 / TF-IDF** → precisão lexical<br>
* **Embeddings** → representação de significado<br>
* **Hybrid Retrieval** → combinação otimizada<br><br>

<br><br>

## 🧠 Aplicação no Projeto (FIIs)

* Análise de notícias financeiras<br>
* Detecção de risco (vacância, inadimplência)<br>
* Geração de insights de investimento<br>
* Suporte à decisão estratégica<br><br>

<br><br>

## 🚀 Vantagens

* Redução de alucinações<br>
* Maior precisão<br>
* Respostas explicáveis<br>
* Integração com dados reais<br><br>

<br><br>

## ⚠️ Limitações

* Dependência da qualidade do retrieval<br>
* Custo computacional maior<br>
* Necessidade de engenharia de prompt<br><br>

<br><br>

## 📚 Referência

Ver:<br>
`docs/Conceptual Foundations.md`<br><br>

<br><br>

## 🧾 Conclusão

O RAG transforma o sistema em uma **plataforma de inteligência**, onde dados são convertidos em conhecimento acionável.<br><br>


