
# ⚡ FAISS — Motor de Busca por Similaridade Semântica

## 1. 📌 Visão Geral

**FAISS (Facebook AI Similarity Search)** é uma biblioteca de alto desempenho projetada para busca eficiente por similaridade em representações vetoriais densas.

Neste projeto, o FAISS atua como o **motor de recuperação semântica**, permitindo que o sistema vá além da correspondência por palavras-chave e opere com base em **relações de significado**.

<br><br>

## 2. 🎯 Papel na Arquitetura

O FAISS é responsável por:

* Indexar embeddings vetoriais gerados a partir de textos financeiros
* Realizar buscas rápidas por vizinhos mais próximos
* Recuperar documentos semanticamente semelhantes

> Permite encontrar **informações relevantes mesmo sem termos exatos presentes**.

<br><br>


## 3. 🧠 Papel Conceitual

O FAISS opera em um **espaço vetorial de alta dimensão**, onde:

* Cada documento → torna-se um vetor
* A distância entre vetores → representa similaridade semântica

> Quanto mais próximos os vetores, mais semelhantes são seus significados.

<br><br>


## 4. ⚙️ Como Funciona

### Etapa 1 — Texto → Embeddings

O texto financeiro é transformado em vetores usando modelos como:

* SentenceTransformer
* Encoders baseados em BERT

<br><br>


### Etapa 2 — Indexação

O FAISS armazena vetores em estruturas otimizadas:

* Índices Flat (busca exata)
* IVF (Inverted File Index)
* HNSW (grafos hierárquicos)

<br><br>


### Etapa 3 — Busca por Similaridade

Dada uma query vetorial, o FAISS:

1. Calcula a distância (ex.: similaridade cosseno ou L2)
2. Recupera os vizinhos mais próximos
3. Retorna os documentos mais relevantes

<br><br>


## 5. 🔍 Tipos de Similaridade

O FAISS suporta múlticas métricas:

| Métrica                 | Descrição                        |
| ----------------------- | -------------------------------- |
| Distância L2            | Distância euclidiana             |
| Produto Interno         | Similaridade por produto escalar |
| Similaridade de Cosseno | Similaridade angular             |

<br><br>


## 6. 🚀 Por que o FAISS é Crítico neste Projeto

Métodos tradicionais (TF-IDF, BM25):

* Dependem de correspondência exata de palavras
* Falham com paráfrases ou significados implícitos

O FAISS permite:

* Compreensão semântica
* Recuperação sensível ao contexto
* Descoberta de sinais implícitos

> Isso é essencial para analisar **sentimento de investidores e narrativas de mercado**.

<br><br>


## 7. 🔗 Integração com Outros Componentes

O FAISS não atua isoladamente — ele complementa outras técnicas:

| Componente | Papel                      | Relação com FAISS          |
| ---------- | -------------------------- | -------------------------- |
| MapReduce  | Preparação de dados        | Fornece texto limpo        |
| TF-IDF     | Relevância de termos       | Base lexical               |
| BM25       | Precisão por palavra-chave | Captura menções explícitas |
| Embeddings | Geração vetorial           | Entrada do FAISS           |
| RAG        | Geração de insights        | Usa resultados do FAISS    |

<br><br>


## 8. 🧠 Aplicação em FIIs

No contexto dos FIIs brasileiros, o FAISS permite:

* Detectar **discussões indiretas** sobre fundos
* Identificar **tendências de sentimento de mercado**
* Recuperar **narrativas financeiras contextualmente semelhantes**

Exemplo:

Query:

```text id="br1"
"Fundos logísticos sob pressão"
```

O FAISS pode recuperar:

* Discussões sobre HGLG11 mesmo sem citação direta
* Notícias sobre vacância logística
* Mudanças de sentimento no setor

<br><br>


## 9. 🔁 FAISS dentro do RAG

O FAISS é um componente central do pipeline **RAG (Retrieval-Augmented Generation)**:

```text id="br2"
Consulta → Embedding → Busca FAISS → Contexto Recuperado → LLM → Resposta
```

<br><br>


## 10. 🧩 Pontos Fortes

* Alta escalabilidade (milhões de vetores)
* Busca extremamente rápida
* Funciona com dados de alta dimensionalidade
* Permite recuperação semântica

<br><br>


## 11. ⚠️ Limitações

* Depende de embeddings de alta qualidade
* Busca aproximada pode reduzir precisão
* Baixa interpretabilidade (vetores como “caixa-preta”)

<br><br>


## 12. 🔮 Insight Conceitual

O FAISS transforma a recuperação de informação de:

* Correspondência por palavras → **Navegação por significado**
* Busca estática → **Exploração semântica**

> Permite que o sistema opere em um **espaço de significados, não apenas de palavras**.

<br><br>


## 13. 🔗 Relação com Fundamentos Conceituais

Para aprofundamento teórico:

📄 `docs/Conceptual Foundations.md`

<br><br>


## 🧠 Insight Final

O FAISS não é apenas uma ferramenta de busca — é o **principal habilitador da inteligência semântica** do sistema.

Quando combinado com:

* Embeddings → representação
* BM25 → precisão
* RAG → raciocínio

> O FAISS se torna a **ponte entre linguagem e significado** em sistemas de inteligência financeira.

