# ]BM25 (Best Matching 25) — Fundamentação Técnica e Importância no Projeto de Inteligência de Mercado para FIIs]()



## 1. Introdução

No contexto de projetos de Inteligência Artificial aplicada à análise textual, a identificação de conteúdos mais relevantes representa um desafio central, especialmente quando existe grande volume de dados não estruturados provenientes de múltiplas fontes digitais. Neste projeto de Inteligência de Mercado para Fundos de Investimento Imobiliário (FIIs), tornou-se necessário estabelecer um mecanismo capaz de identificar, classificar e priorizar fontes de informação mais relevantes para fins de marketing digital, análise de comportamento do investidor e inteligência competitiva.

Nesse cenário, foi adotado o algoritmo **BM25 (Best Matching 25)**, um dos métodos mais consolidados da área de **Recuperação de Informação (Information Retrieval – IR)**, amplamente utilizado em mecanismos de busca, sistemas documentais e plataformas de recuperação textual.

O BM25 foi escolhido por oferecer uma combinação importante entre:

- **Precisão analítica**;
- **Interpretabilidade dos resultados**;
- **Baixo custo computacional**;
- **Capacidade explicativa (Explainable AI – XAI)**;
- **Adequação acadêmica para projetos de Ciência de Dados e NLP**.

Sua aplicação permite ranquear documentos, notícias, postagens e fontes digitais conforme sua relevância em relação a um conjunto de termos estratégicos do mercado de FIIs.

<br><br>

## 2. O que é BM25?

O **BM25 (Best Matching 25)** é um algoritmo probabilístico de ranqueamento textual pertencente ao campo da Recuperação de Informação.

Seu principal objetivo é determinar **quão relevante um documento é para uma consulta (query)** realizada pelo usuário.

Diferentemente de abordagens simples baseadas apenas na contagem de palavras, o BM25 considera múltiplos fatores estatísticos, como:

- frequência do termo no documento;
- raridade do termo na coleção;
- tamanho do documento;
- saturação da repetição de palavras.

Na prática, isso significa que o algoritmo consegue distinguir entre:

- um artigo genuinamente relevante sobre FIIs;
- um artigo que apenas menciona superficialmente palavras-chave do setor.

Por exemplo:

Uma notícia especializada contendo termos como:

> dividend yield, vacância, P/VP, fundos imobiliários, gestão ativa, renda passiva

tende a receber pontuação superior em relação a conteúdos genéricos sobre investimentos.

<br><br>

## 3. Por que o BM25 foi escolhido neste projeto?

O objetivo central deste projeto consiste em identificar **quais canais digitais apresentam maior valor informacional sobre FIIs**, auxiliando estratégias de marketing, análise competitiva e entendimento do comportamento do investidor.

Nesse cenário, o BM25 é particularmente importante porque permite:

<br><

### 3.1 Ranqueamento Inteligente de Fontes

O algoritmo permite identificar quais portais financeiros produzem conteúdo mais alinhado ao universo dos FIIs.

Exemplos de fontes monitoradas:

- InfoMoney
- Suno Research
- Funds Explorer
- Clube FII
- Status Invest
- Investidor10
- Valor Investe
- Bora Investir (B3)
- Money Times
- Reddit (monitoramento social)

Em vez de assumir subjetivamente quais fontes são melhores, o projeto utiliza evidências quantitativas.

<br>

### 3.2 Explainable AI (IA Explicável)

Uma das razões mais relevantes para adoção do BM25 foi sua alta interpretabilidade.

Diferentemente de modelos considerados *black-box* (caixa-preta), o BM25 permite explicar:

> “Por que determinada fonte foi ranqueada acima das demais?”

Isso fortalece princípios de:

- Responsible AI;
- Trustworthy AI;
- transparência algorítmica;
- governança de IA.

Exemplo interpretável:

**Funds Explorer recebeu pontuação elevada porque:**

- “Dividend Yield” apareceu 18 vezes;
- “Vacância” apareceu 12 vezes;
- “P/VP” apareceu 9 vezes;
- “Gestão” apareceu 14 vezes.

Assim, o ranqueamento deixa de ser arbitrário e torna-se tecnicamente justificável.

<br>

### 3.3 Adequação ao Escopo Acadêmico

O BM25 apresenta vantagens importantes em projetos acadêmicos:

- implementação relativamente simples;
- forte respaldo científico;
- baixo custo computacional;
- fácil documentação metodológica;
- resultados reproduzíveis.

Além disso, sua utilização demonstra domínio de técnicas clássicas de **Natural Language Processing (NLP)** e **Information Retrieval**, agregando profundidade técnica ao projeto.

<br><br>

## 4. Como o BM25 funciona?

O BM25 mede a relevância de um documento considerando quatro componentes principais.

<br>

### 4.1 Frequência do termo (TF)

Quanto mais vezes um termo aparece em um documento, maior tende a ser sua relevância.

Exemplo:

Um artigo contendo múltiplas ocorrências de:

- FII
- dividend yield
- vacância
- P/VP

possui maior potencial informacional sobre o tema.

No entanto, o BM25 evita supervalorizar repetições excessivas.

<br>

### 4.2 Frequência inversa do documento (IDF)

Nem toda palavra é igualmente relevante.

Palavras extremamente comuns possuem menor peso.

Exemplo:

Palavras como:

- investimento
- mercado
- financeiro

aparecem em quase todos os textos.

Já termos específicos como:

- vacância;
- dividend yield;
- P/VP;
- laje corporativa;
- fundo imobiliário;

possuem maior poder discriminatório.

O BM25 atribui maior peso aos termos raros e especializados.

<br>

### 4.3 Normalização pelo tamanho do documento

Documentos muito longos tendem naturalmente a possuir mais palavras.

Sem normalização, textos extensos seriam favorecidos injustamente.

O BM25 corrige esse problema penalizando proporcionalmente documentos excessivamente longos.

Isso garante maior justiça estatística no ranqueamento.

<br>

### 4.4 Saturação da repetição

Repetir uma palavra indefinidamente não aumenta infinitamente a relevância.

Exemplo:

Um artigo mencionando “FII” 100 vezes não necessariamente é melhor do que outro mencionando 15 vezes em contexto altamente relevante.

O BM25 aplica um mecanismo de saturação que limita ganhos artificiais.

<br><br>

## 5. Fórmula Matemática do BM25

O BM25 é definido pela seguinte equação:

\[
BM25(D,Q)=\sum_{i=1}^{n} IDF(q_i)\cdot
\frac{f(q_i,D)(k_1+1)}
{f(q_i,D)+k_1\left(1-b+b\cdot\frac{|D|}{avgdl}\right)}
\]

Onde:

| Variável | Significado |
|----------|-------------|
| \( D \) | Documento analisado |
| \( Q \) | Consulta (*query*) |
| \( q_i \) | Termo da consulta |
| \( f(q_i,D) \) | Frequência do termo no documento |
| \( IDF(q_i) \) | Frequência inversa do documento |
| \( |D| \) | Tamanho do documento |
| \( avgdl \) | Tamanho médio dos documentos |
| \( k_1 \) | Controle de saturação |
| \( b \) | Controle de penalização por tamanho |

Valores geralmente utilizados:

- `k1 = 1.2 a 2.0`
- `b = 0.75`

<br><br>

## 6. Exemplo Aplicado ao Projeto de FIIs

Considere a seguinte consulta estratégica utilizada para identificar conteúdo relevante:

```text
"P/VP dividend yield vacância gestão"
```

<br>

### Portal A — Funds Explorer

Ocorrências:

- P/VP → 12
- dividend yield → 18
- vacância → 14
- gestão → 11

Resultado:

**BM25 Score = 8.7**

<br>

### Portal B — Portal Financeiro Genérico

Ocorrências:

- P/VP → 1
- dividend yield → 0
- vacância → 0
- gestão → 2

Resultado:

**BM25 Score = 1.2**

<br><br>

Interpretação:

O **Portal A** demonstra maior especialização em conteúdo sobre FIIs, tornando-se mais relevante para estratégias de marketing e inteligência competitiva.

<br><br>

## 7. BM25 vs TF-IDF vs Embeddings

| Critério | TF-IDF | BM25 | Embeddings |
|-----------|---------|------|-------------|
| Interpretabilidade | Alta | Muito Alta | Baixa |
| Explicabilidade | Média | Alta | Baixa |
| Semântica | Baixa | Baixa | Alta |
| Complexidade | Baixa | Média | Alta |
| Custo Computacional | Baixo | Baixo | Alto |
| Adequação Acadêmica | Boa | Excelente | Alta |
| Transparência | Média | Excelente | Baixa |

### Justificativa metodológica

O BM25 foi preferido porque:

1. supera limitações do TF-IDF;
2. mantém alta explicabilidade;
3. é estatisticamente robusto;
4. não depende de infraestrutura complexa;
5. favorece governança e Responsible AI.

O uso de embeddings semânticos e modelos vetoriais (*RAG*) foi considerado fora do escopo atual devido à maior complexidade computacional e menor interpretabilidade.

<br><br>

## 8. Relação com Responsible AI e Explainable AI (XAI)

O uso do BM25 fortalece os princípios de **Responsible AI**, pois:

### Transparência
O processo de ranqueamento pode ser explicado matematicamente.

### Fairness
Todas as fontes são avaliadas usando o mesmo critério estatístico.

### Accountability
As decisões do sistema podem ser auditadas.

### Reprodutibilidade
Os resultados podem ser reproduzidos em diferentes execuções.

### Explainability
O sistema consegue justificar:

> “Por que esta fonte foi considerada relevante?”

Essa característica torna o modelo adequado para contextos acadêmicos e corporativos.

<br><br>

## 9. Limitações do BM25

Embora robusto, o BM25 possui limitações.

### Semântica limitada

O algoritmo trabalha principalmente com correspondência lexical.

Exemplo:

“Dividendos” e “proventos” podem representar conceitos semelhantes, mas não necessariamente são tratados como equivalentes.

### Falta de contexto profundo

O BM25 não compreende ironia, intenção ou nuances financeiras.

### Dependência da qualidade textual

Conteúdos mal escritos podem afetar o desempenho.

<br><br>

## 10. Melhorias Futuras

Futuras evoluções do projeto incluem:

- BM25 + Embeddings híbridos;
- Fine-tuning financeiro com BERT;
- busca semântica contextual;
- RAG verdadeiro com banco vetorial;
- modelos específicos para português financeiro.

<br><br>

## 11. Conclusão

O BM25 mostrou-se uma escolha metodologicamente sólida para este projeto de Inteligência de Mercado aplicado ao ecossistema de Fundos de Investimento Imobiliário (FIIs).

Sua adoção permitiu:

- ranquear fontes financeiras;
- identificar conteúdos mais relevantes;
- justificar decisões algorítmicas;
- fortalecer Explainable AI;
- garantir transparência e governança.

Além disso, sua combinação entre robustez estatística, interpretabilidade e simplicidade computacional o torna altamente adequado para aplicações acadêmicas e corporativas envolvendo Recuperação de Informação e Processamento de Linguagem Natural.

<br><br>

## Referências Bibliográficas (ABNT NBR 6023:2018)

MANNING, Christopher D.; RAGHAVAN, Prabhakar; SCHÜTZE, Hinrich. *Introduction to Information Retrieval*. Cambridge: Cambridge University Press, 2008.

ROBERTSON, Stephen E.; WALKER, Steve; JONES, Susan; HANCOCK-BEAULIEU, Micheline; GATFORD, Mike. Okapi at TREC-3. In: *Text REtrieval Conference (TREC-3)*. Gaithersburg: NIST, 1995.

ROBERTSON, Stephen; ZARAGOZA, Hugo. The probabilistic relevance framework: BM25 and beyond. *Foundations and Trends in Information Retrieval*, Delft, v. 3, n. 4, p. 333–389, 2009.

RUSSELL, Stuart; NORVIG, Peter. *Artificial Intelligence: A Modern Approach*. 4. ed. Harlow: Pearson, 2021.

GOODFELLOW, Ian; BENGIO, Yoshua; COURVILLE, Aaron. *Deep Learning*. Cambridge: MIT Press, 2016.

BAROCAS, Solon; SELBST, Andrew D. Big data’s disparate impact. *California Law Review*, Berkeley, v. 104, n. 3, p. 671–732, 2016.

EUROPEAN COMMISSION. *Ethics Guidelines for Trustworthy AI*. Brussels: High-Level Expert Group on Artificial Intelligence, 2019.

MOLNAR, Christoph. *Interpretable Machine Learning*. 2. ed. [S.l.]: Lulu.com, 2022.

JURAFSKY, Daniel; MARTIN, James H. *Speech and Language Processing*. 3. ed. Stanford: Stanford University, 2025.

BRASIL. Lei nº 13.709, de 14 de agosto de 2018. Lei Geral de Proteção de Dados Pessoais (LGPD). Diário Oficial da União: Brasília, DF, 15 ago. 2018.
