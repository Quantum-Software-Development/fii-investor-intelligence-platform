# [Framework Analítico — Dos Dados à Decisão]()
### 🇧🇷 ***Da Frequência ao Significado: Inteligência para Tomada de Decisão em FIIs Brasileiros***

<br>

A plataforma transforma progressivamente informações financeiras brutas em inteligência estratégica acionável por meio de múltiplas camadas analíticas. Em vez de depender de uma única técnica de análise, cada etapa se apoia na anterior, enriquecendo as informações e reduzindo a incerteza até que os dados brutos se tornem suporte à decisão baseado em evidências.

<br><br>

## [TL;DR]()

Um [**pipeline de PLN + Recuperação de Informação**]() que transforma informações não estruturadas do mercado brasileiro de Fundos de Investimento Imobiliário (FIIs) em inteligência acionável.

Ao combinar [**Big Data, Recuperação de Informação, IA Semântica e Geração Aumentada por Recuperação (RAG)**](), a plataforma converte conteúdos financeiros fragmentados, discussões entre investidores e narrativas de mercado em insights estruturados que apoiam análises estratégicas e a tomada de decisão.

<br>

## [Stack]()

* [**MapReduce →**]() descoberta de padrões em larga escala e processamento distribuído
* [**TF-IDF →**]() importância dos termos e especificidade da informação
* [**BM25 →**]() ranqueamento por relevância contextual
* [**FAISS + Embeddings →**]() recuperação semântica e representação de significado
* [**RAG →**]() geração de respostas fundamentadas em evidências
* [**Análise de Sentimento Contextual →**]() interpretação de riscos e análise comportamental

<br>

## [Impacto]()

[*]() Análise do comportamento dos investidores <br>
[*]() Otimização da relevância do conteúdo <br>
[*]() Geração de inteligência de mercado <br>
[*]() Suporte à tomada de decisões estratégicas <br>
[*]() Avaliação da percepção de mercado e dos riscos

<br><br>

## [Da Frequência ao Significado: Inteligência Acionável para o Mercado de FIIs ]()

Este projeto combina **Big Data**, **Recuperação de Informação** e **Inteligência Artificial Semântica** para transformar informações financeiras fragmentadas, conversas entre investidores e conteúdos de mercado em sinais estratégicos acionáveis, revelando:

[*]() comportamento dos investidores <br>
[*]() relevância do conteúdo <br>
[*]() relações semânticas <br>
[*]() percepção de mercado <br>
[*]() oportunidades estratégicas

<br>

A jornada analítica segue um pipeline progressivo de inteligência:

<br>

> Frequência → Relevância → Significado → Decisão

<br>

Em vez de se limitar à simples contagem de palavras, a plataforma constrói progressivamente uma compreensão contextual capaz de apoiar decisões estratégicas explicáveis e fundamentadas em evidências.

<br><br>

### [Evolução Analítica]()

A plataforma aplica múltiplas camadas de inteligência, cada uma contribuindo com uma capacidade analítica distinta.

<br>

| [Camada]() | [Objetivo]() |
| ------ | --------- |
| [Big Data]() | Processar grandes volumes de informações financeiras |
| [Recuperação de Informação]() | Identificar o conteúdo mais relevante |
| [IA Semântica]() | Compreender o significado além das palavras exatas |
| [Inteligência para Decisão]() | Transformar insights em ações estratégicas |

<br><br>

## [Metodologia]()

<br>

## 1. [MapReduce — Descobrindo a Atenção Coletiva]()

O MapReduce analisa o corpus em larga escala para identificar:

* os tópicos mais frequentemente discutidos
* a terminologia financeira predominante
* padrões emergentes de discussão
* as áreas que atraem a maior atenção dos investidores

<br>

### [***Exemplo:***]()

<br>

```text
dividendos         15.420 ocorrências
fundo              38.900 ocorrências
mercado            31.200 ocorrências
investimento       28.500 ocorrências
vacância            6.300 ocorrências
```

<br>

### [***Insight***]()

<br>

A alta frequência de **"dividendos"** indica um forte interesse dos investidores.

No entanto, a frequência, por si só, não mede o valor informacional.

**Frequência ≠ Importância**

Um termo que aparece com muita frequência não é necessariamente o mais informativo nem o mais relevante para a tomada de decisão.

Essa limitação motiva a próxima camada analítica, que avalia o quão distintivo cada termo realmente é em todo o corpus.

<br><br>

## 2. [TF-IDF — Medindo o Valor Informacional]()

Enquanto o MapReduce identifica o que é discutido com maior frequência, o TF-IDF determina quais termos realmente diferenciam um documento de outro.

Em vez de se concentrar apenas na contagem de ocorrências, o TF-IDF mede a especificidade informacional de cada termo dentro de todo o corpus.

<br>

### [***Exemplo:***]()

<br>

### Artigo:

<br>

> "O XPTO11 aumenta os dividendos após o crescimento da receita imobiliária."

<br>

### [***Análise:***]()

<br>

```text
dividendos                   → importância média
renda mensal                 → alta importância
XPTO11                       → alta importância
distribuição extraordinária  → importância muito alta
```

<br>

### [***Insight***]()

<br>

Um termo pode ser altamente relevante dentro de um documento sem necessariamente ser único em toda a coleção.

O TF-IDF, portanto, destaca o vocabulário que melhor caracteriza cada documento individualmente.

No entanto, identificar termos informativos representa apenas parte do problema.

A próxima camada analítica determina **quais documentos são, de fato, os mais relevantes para a intenção de busca do usuário**, introduzindo a relevância contextual por meio de ranqueamento.

<br><br>

## 3. [BM25 — Ranqueamento por Relevância Contextual]()

Embora o TF-IDF identifique os termos que melhor caracterizam documentos individuais, ele não determina qual documento responde de forma mais eficaz à consulta do usuário.

O BM25 resolve essa limitação ao introduzir um modelo de ranqueamento que considera tanto as propriedades estatísticas do corpus quanto o contexto da busca. Em vez de simplesmente contar ocorrências de termos, o BM25 avalia o quão bem cada documento atende à necessidade de informação do usuário.

O ranqueamento é calculado considerando:

[*]() frequência do termo <br>
[*]() frequência inversa do documento (IDF) <br>
[*]() normalização do comprimento do documento <br>
[*]() intenção de busca

<br>

### [***Exemplo:***]()

<br>

### Consulta:

<br>

> "FIIs com dividendos mensais consistentes"

<br>

### Comparação:

<br>

```text
Documento A:

"XPTO11 mantém distribuições mensais de dividendos estáveis há 24 meses consecutivos."

Pontuação BM25 → 8,7


Documento B:

"O mercado imobiliário continua se recuperando com novas oportunidades de investimento."

Pontuação BM25 → 2,1
```

<br>

### [***Insight***]()

<br>

O BM25 identifica o documento que mais se aproxima da intenção de busca do usuário, em vez de simplesmente selecionar aquele que contém o maior número de termos correspondentes.

Isso melhora substancialmente a qualidade da recuperação de informações ao equilibrar frequência, raridade e relevância contextual.

No entanto, o BM25 continua sendo, fundamentalmente, um modelo de recuperação lexical.

Se dois documentos descrevem o mesmo conceito utilizando vocabulários diferentes, informações relevantes ainda podem ser ignoradas.

A próxima camada analítica supera essa limitação por meio de representações semânticas capazes de compreender o significado, e não apenas as palavras exatas.

<br><br>

# 4. [FAISS + Embeddings — Compreendendo o Significado Além das Palavras]()
