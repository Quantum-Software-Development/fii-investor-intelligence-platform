# BM25 (Best Matching 25) — Technical Foundation and Importance in the Market Intelligence Project for FIIs



## 1. Introduction

In the context of Artificial Intelligence projects applied to textual analysis, identifying the most relevant content represents a central challenge, especially when there is a large volume of unstructured data from multiple digital sources. In this Market Intelligence project for Real Estate Investment Funds (FIIs), it became necessary to establish a mechanism capable of identifying, classifying, and prioritizing the most relevant information sources for digital marketing, investor behavior analysis, and competitive intelligence purposes.

In this scenario, the **BM25 (Best Matching 25)** algorithm was adopted, one of the most consolidated methods in the field of **Information Retrieval (IR)**, widely used in search engines, document systems, and textual retrieval platforms.

BM25 was chosen for offering an important combination of:

- **Analytical precision**;
- **Interpretability of results**;
- **Low computational cost**;
- **Explanatory capability (Explainable AI – XAI)**;
- **Academic suitability for Data Science and NLP projects**.

Its application allows ranking documents, news, posts, and digital sources according to their relevance to a set of strategic terms in the FII market.

<br><br>

## 2. What is BM25?

**BM25 (Best Matching 25)** is a probabilistic textual ranking algorithm belonging to the field of Information Retrieval.

Its main objective is to determine **how relevant a document is to a query** made by the user.

Unlike simple approaches based solely on word counting, BM25 considers multiple statistical factors, such as:

- term frequency in the document;
- term rarity in the collection;
- document size;
- saturation of word repetition.

In practice, this means that the algorithm can distinguish between:

- a genuinely relevant article about FIIs;
- an article that only superficially mentions keywords from the sector.

For example:

Specialized news containing terms such as:

> dividend yield, vacancy, P/VP, real estate funds, active management, passive income

tends to receive a higher score compared to generic content about investments.

<br><br>

## 3. Why was BM25 chosen for this project?

The central objective of this project is to identify **which digital channels offer the most informational value about FIIs**, assisting marketing strategies, competitive analysis, and understanding investor behavior.

In this scenario, BM25 is particularly important because it allows:

<br><

### 3.1 Intelligent Source Ranking

The algorithm allows identifying which financial portals produce content most aligned with the FII universe.

Examples of monitored sources:

- InfoMoney
- Suno Research
- Funds Explorer
- Clube FII
- Status Invest
- Investidor10
- Valor Investe
- Bora Investir (B3)
- Money Times
- Reddit (social monitoring)

Instead of subjectively assuming which sources are better, the project uses quantitative evidence.

<br>

### 3.2 Explainable AI (XAI)

One of the most relevant reasons for adopting BM25 was its high interpretability.

Unlike models considered *black-box*, BM25 allows explaining:

> “Why was a certain source ranked above others?”

This strengthens the principles of:

- Responsible AI;
- Trustworthy AI;
- algorithmic transparency;
- AI governance.

Interpretable example:

**Funds Explorer received a high score because:**

- “Dividend Yield” appeared 18 times;
- “Vacancy” appeared 12 times;
- “P/VP” appeared 9 times;
- “Management” appeared 14 times.

Thus, the ranking ceases to be arbitrary and becomes technically justifiable.

<br>

### 3.3 Suitability for Academic Scope

BM25 offers important advantages in academic projects:

- relatively simple implementation;
- strong scientific backing;
- low computational cost;
- easy methodological documentation;
- reproducible results.

Furthermore, its use demonstrates mastery of classic **Natural Language Processing (NLP)** and **Information Retrieval** techniques, adding technical depth to the project.

<br><br>

## 4. How does BM25 work?

BM25 measures the relevance of a document considering four main components.

<br>

### 4.1 Term Frequency (TF)

The more often a term appears in a document, the greater its relevance tends to be.

Example:

An article containing multiple occurrences of:

- FII
- dividend yield
- vacancy
- P/VP

It has greater informational potential on the topic.

However, BM25 avoids overvaluing excessive repetitions.

<br>

### 4.2 Inverse Document Frequency (IDF)

Not every word is equally relevant.

Extremely common words have less weight.

Example:

Words like:

- investment
- market
- financial

appear in almost all texts.

However, specific terms such as:

- vacancy;
- dividend yield;
- P/VP;
- corporate slab;
- real estate fund;

have greater discriminatory power.

BM25 assigns greater weight to rare and specialized terms.

<br>

### 4.3 Normalization by document length

Very long documents naturally tend to have more words.

Without normalization, extensive texts would be unfairly favored.

BM25 corrects this problem by proportionally penalizing excessively long documents.

This ensures greater statistical fairness in ranking.

<br>

### 4.4 Repetition saturation

Repeating a word indefinitely does not infinitely increase relevance.

Example:

An article mentioning “FII” 100 times is not necessarily better than another mentioning it 15 times in a highly relevant context.

BM25 applies a saturation mechanism that limits artificial gains.

<br><br>

## 5. Mathematical Formula of BM25

BM25 is defined by the following equation:

\[
BM25(D,Q)=\sum_{i=1}^{n} IDF(q_i)\cdot
\frac{f(q_i,D)(k_1+1)}
{f(q_i,D)+k_1\left(1-b+b\cdot\frac{|D|}{avgdl}\right)}
\]

Where:

| Variable | Meaning |
|----------|-------------|
| \( D \) | Document analyzed |
| \( Q \) | Query |
| \( q_i \) | Query term |
| \( f(q_i,D) \) | Term frequency in the document |
| \( IDF(q_i) \) | Inverse document frequency |
| \( |D| \) | Document length |
| \( avgdl \) | Average document length |
| \( k_1 \) | Saturation control |
| \( b \) | Length penalization control |

Commonly used values:

- `k1 = 1.2 to 2.0`
- `b = 0.75`

<br><br>

## 6. Example Applied to the FII Project

Consider the following strategic query used to identify relevant content:

```text
"P/VP dividend yield vacancy management"
```

<br>

### Portal A — Funds Explorer

Occurrences:

- P/VP → 12
- dividend yield → 18
- vacancy → 14
- management → 11

Result:

**BM25 Score = 8.7**

<br>

### Portal B — Generic Financial Portal

Occurrences:

- P/VP → 1
- dividend yield → 0
- vacancy → 0
- management → 2

Result:

**BM25 Score = 1.2**

<br><br>

Interpretation:

**Portal A** demonstrates greater specialization in FII content, becoming more relevant for marketing strategies and competitive intelligence.

<br><br>

## 7. BM25 vs TF-IDF vs Embeddings

| Criterion | TF-IDF | BM25 | Embeddings |
|-----------|---------|------|-------------|
| Interpretability | High | Very High | Low |
| Explainability | Medium | High | Low |
| Semantics | Low | Low | High |
| Complexity | Low | Medium | High |
| Computational Cost | Low | Low | High |
| Academic Suitability | Good | Excellent | High |
| Transparency | Medium | Excellent | Low |

### Methodological justification

BM25 was preferred because:

1. overcomes TF-IDF limitations;
2. maintains high explainability;
3. is statistically robust;
4. does not depend on complex infrastructure;
5. favors governance and Responsible AI.

The use of semantic embeddings and vectorial models (*RAG*) was considered out of the current scope due to greater computational complexity and lower interpretability.

<br><br>

## 8. Relationship with Responsible AI and Explainable AI (XAI)

The use of BM25 strengthens the principles of **Responsible AI**, as it promotes:

### Transparency
The ranking process can be mathematically explained.

### Fairness
All sources are evaluated using the same statistical criterion.

### Accountability
System decisions can be audited.

### Reproducibility
Results can be reproduced in different executions.

### Explainability
The system can justify:

> “Why was this source considered relevant?”

This characteristic makes the model suitable for academic and corporate contexts.

<br><br>

## 9. Limitations of BM25

Although robust, BM25 has limitations.

### Limited semantics

The algorithm primarily works with lexical matching.

Example:

“Dividends” and “proventos” (earnings) may represent similar concepts, but are not necessarily treated as equivalents.

### Lack of deep context

BM25 does not understand irony, intent, or financial nuances.

### Dependence on textual quality

Poorly written content can affect performance.

<br><br>

## 10. Future Improvements

Future evolutions of the project include:

- Hybrid BM25 + Embeddings;
- Financial fine-tuning with BERT;
- contextual semantic search;
- true RAG with vector database;
- specific models for financial Portuguese.

<br><br>

## 11. Conclusion

BM25 proved to be a methodologically sound choice for this Market Intelligence project applied to the Real Estate Investment Funds (FIIs) ecosystem.

Its adoption allowed:

- ranking financial sources;
- identifying more relevant content;
- justifying algorithmic decisions;
- strengthening Explainable AI;
- ensuring transparency and governance.

Furthermore, its combination of statistical robustness, interpretability, and computational simplicity makes it highly suitable for academic and corporate applications involving Information Retrieval and Natural Language Processing.

<br><br>

## Bibliographic References (ABNT NBR 6023:2018)

MANNING, Christopher D.; RAGHAVAN, Prabhakar; SCHÜTZE, Hinrich. *Introduction to Information Retrieval*. Cambridge: Cambridge University Press, 2008.

ROBERTSON, Stephen E.; WALKER, Steve; JONES, Susan; HANCOCK-BEAULIEU, Micheline; GATFORD, Mike. Okapi at TREC-3. In: *Text REtrieval Conference (TREC-3)*. Gaithersburg: NIST, 1995.

ROBERTSON, Stephen; ZARAGOZA, Hugo. The probabilistic relevance framework: BM25 and beyond. *Foundations and Trends in Information Retrieval*, Delft, v. 3, n. 4, p. 333–389, 2009.
