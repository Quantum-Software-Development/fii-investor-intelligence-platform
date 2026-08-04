## [Desenho da Pesquisa]()

<br><br>

**Investor Intelligence Platform - FIIs Brasil 🇧🇷**
*Fundamentação metodológica do projeto acadêmico*

<br><br>

### [***Pergunta de Pesquisa***]()

> *Quais canais digitais (portais financeiros e plataformas sociais) apresentam a maior concentração de investidores qualificados em FIIs, e qual é o perfil de sentimento dominante de cada canal?*

<br><br>

**Subperguntas**:
1. Quais portais produzem o conteúdo sobre FIIs tecnicamente mais rico? (BM25)
2. Qual é a distribuição de sentimento entre as fontes? (Análise de Sentimento)
3. Quais fontes mencionam termos relacionados a FIIs em contextos predominantemente negativos? (Detecção de Contexto Negativo)
4. Quais clusters de discussão caracterizam o comportamento do investidor em cada canal? (Topic Modeling)

<br><br>

---

<br><br>

## [Tipo de Pesquisa]()

<br><br>

| Dimensão | Classificação |
|-----------|---------------|
| **Natureza** | Pesquisa aplicada |
| **Abordagem** | Quantitativa + computacional |
| **Estratégia** | Analytics descritivo |
| **Horizonte** | Transversal (janela de 6 meses) |
| **Tipo de dado** | Secundário (texto publicamente disponível) |

<br><br>

---

<br><br>

## [Escolhas Metodológicas]()

<br><br>

### [***Por que BM25 (e não Embeddings Neurais)?***]()

<br><br>

| Critério | BM25 | BERT/Embeddings |
|-----------|------|-----------------|
| Interpretabilidade | ✅ Total | ❌ Caixa-preta |
| Não requer dados de treino | ✅ Sim | ❌ Requer dados rotulados |
| Custo computacional | ✅ Baixo | ❌ Alto |
| Suporte a PT-BR | ✅ Agnóstico de idioma | ⚠️ Requer modelo PT-BR |
| Conformidade XAI | ✅ Nativa | ❌ Requer explicação post-hoc |
| Defensabilidade acadêmica | ✅ Estabelecida (Robertson 2009) | ✅ Estado da arte |

<br><br>

**Decisão**: BM25 é preferido para a V1 (escopo acadêmico) devido à interpretabilidade e alinhamento com XAI. Retrieval neural é item do roadmap V2.

<br><br>

### [***Por que TextBlob + Léxico (e não FinBERT)?***]()

- Nenhum modelo FinBERT em **PT-BR** publicamente disponível no início do projeto
- TextBlob fornece uma baseline reproduzível e determinística
- O léxico adiciona especificidade de domínio sem necessidade de dados de treino
- Acurácia de ~75–80% é suficiente para decisões de marketing **em nível de canal**
- Fine-tuning de FinBERT sobre corpus FII PT-BR é item da V2

<br><br>

### [***Por que LDA (e não BERTopic)?***]()

- LDA é interpretável e determinístico (`random_state=42`)
- BERTopic requer modelo de embedding grande (overhead computacional)
- Modelo de 5 tópicos é suficiente para segmentação de comportamento do investidor
- Transparência acadêmica favorece métodos estabelecidos

<br><br>

---

<br><br>

## [Desenho do Corpus]()

<br><br>

| Dimensão | Decisão |
|-----------|---------|
| **Fontes** | 20 portais financeiros curados |
| **Janela temporal** | 6 meses (recente, relevante) |
| **Idioma** | PT-BR exclusivamente |
| **Camada Comportamental** | Reddit obrigatório (Fonte #21) — `r/investimentos` · `r/farialimabets` |
| **Tamanho mínimo do artigo** | 20 palavras / 100 caracteres |
| **Filtro FII** | Título ou corpo deve conter termos relacionados a FII |

<br><br>

### [***Limitações do Corpus***]()

1. **Viés de seleção**: 20 portais ≠ universo completo de discussão sobre FIIs
2. **Limitação temporal**: janela de 6 meses pode não capturar tendências de longo prazo
3. **Idioma**: apenas PT-BR; exclui análise de FII em língua inglesa
4. **Plataforma**: exclui Twitter/X, Telegram, YouTube, LinkedIn

<br><br>

---

<br><br>

## [Estratégia de Validação]()

<br><br>

| Componente | Método de Validação |
|-----------|------------------|
| Rankings BM25 | Revisão humana das top-5 fontes |
| Sentimento | Amostra de 50 artigos revisada manualmente |
| Labels de tópicos | Interpretação especialista dos termos principais |
| Contexto negativo | Verificação pontual de pares fonte-termo sinalizados |

<br><br>

---

<br><br>

## [Contribuição Acadêmica]()

<br><br>

1. **Metodológica**: Demonstra a aplicação de BM25 para inteligência de canais de marketing em um domínio financeiro especializado
2. **Aplicada**: Fornece um framework reproduzível de suporte à decisão de marketing para FIIs
3. **Governança**: Demonstra Responsible AI e CRISP-DM em um contexto real de NLP
4. **Educacional**: Aplica princípios de Humanistic AI em um contexto fintech

<br><br>

---

<br><br>

## [Referências]()

<br><br>

- Robertson, S. E., & Zaragoza, H. (2009). The Probabilistic Relevance Framework: BM25 and Beyond. *Foundations and Trends in IR*, 3(4), 333–389.
- Chapman, P., et al. (2000). *CRISP-DM 1.0: Step-by-step data mining guide*. SPSS.
- Mitchell, M., et al. (2019). Model Cards for Model Reporting. *ACM FAccT*.
- Blei, D., Ng, A., & Jordan, M. (2003). Latent Dirichlet Allocation. *JMLR*, 3, 993–1022.

<br><br>

---

<br><br>

*Última atualização: 2026-05-26 | Versão: 2.1*
