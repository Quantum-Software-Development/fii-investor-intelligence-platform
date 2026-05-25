

# 🔍 Revisão Conceitual — BM25, TF-IDF, XAI e Reddit no Projeto FII Intelligence Platform


<br><br>

## 1. O que é XAI (IA Explicável)?

**XAI (Inteligência Artificial Explicável)** é um conjunto de métodos, técnicas e princípios que tornam os resultados de sistemas de IA **compreensíveis, auditáveis e interpretáveis por humanos**.

Em vez de apenas produzir uma resposta (“caixa-preta”), sistemas com XAI conseguem explicar:

* **por que** uma decisão foi tomada;
* **quais variáveis influenciaram o resultado**;
* **como o algoritmo chegou à conclusão**;
* **quais limitações ou incertezas existem**.

### Exemplo simples

Uma IA tradicional poderia dizer:

> “A Fonte X é a melhor para marketing de FIIs.”

Uma abordagem com XAI explicaria:

> “A Fonte X recebeu uma pontuação maior porque apresentou maior frequência dos termos *dividend yield*, *vacância*, *gestão* e *P/VP*, além de maior densidade semântica relacionada ao universo de FIIs.”


<br><br>

## 2. Faz sentido citar XAI se o projeto usa Reddit?

**Sim — mas com o escopo correto.**

O uso do **Reddit não elimina a necessidade de XAI**.

Na verdade, XAI continua importante porque o projeto realiza **ranking, PLN e inferência analítica** sobre conteúdo textual.

Porém, é importante ajustar como XAI é descrito academicamente, evitando exageros ou aparência de “overengineering corporativo”.

### ✅ Formulação correta para este projeto

O projeto utiliza uma abordagem de **interpretabilidade analítica inspirada em princípios de XAI**, pois os métodos empregados são **transparentes e auditáveis**.

Isso é possível porque:

| Técnica                        | Explicável?     | Motivo                                         |
| ------------------------------ | --------------- | ---------------------------------------------- |
| **Contagem de palavras**       | ✅ Sim           | Frequências são totalmente auditáveis          |
| **BM25**                       | ✅ Sim           | Score matemático interpretável                 |
| **Análise de sentimento**      | ⚠️ Parcialmente | Polaridade é explicável, mas depende do modelo |
| **Modelagem de tópicos (LDA)** | ⚠️ Parcialmente | Requer interpretação humana                    |
| **Enriquecimento via Reddit**  | ✅ Sim           | Fonte transparente e rastreável                |


<br><br>

## 3. BM25 em vez de TF-IDF — ainda faz sentido?

### ✅ Sim, mas precisa ser bem justificado.

A pergunta é:

> Por que usar **BM25 em vez de TF-IDF**?

A resposta deve estar alinhada ao **objetivo do sistema**, que é ranqueamento de textos financeiros e recuperação de informação.


<br><br>

## 4. Limitações do TF-IDF neste projeto

O TF-IDF é eficaz para medir a importância de palavras em documentos, mas possui limitações para tarefas de ranqueamento financeiro.

### 1. Não lida bem com saturação de termos

Se um documento repete:

> “dividend yield”

O TF-IDF pode supervalorizar isso excessivamente.

Exemplo:

* Documento A: “dividend yield” (3 vezes)
* Documento B: “dividend yield” (30 vezes)

O TF-IDF tende a recompensar repetição de forma desproporcional, mesmo quando isso não aumenta relevância.

O BM25 mitiga esse comportamento.


<br><br>

### 2. Normalização fraca por tamanho de documento

No ecossistema de FIIs:

* algumas fontes publicam análises longas;
* outras publicam textos curtos.

O TF-IDF tende a favorecer documentos maiores.

O BM25 introduz normalização pelo tamanho do documento, reduzindo esse viés.

Isso é essencial ao comparar:

* InfoMoney
* Funds Explorer
* Clube FII
* Reddit
* Valor Investe
* Investing.com Brasil
* entre outros

Cada fonte possui estilos editoriais e tamanhos de texto diferentes.

<br><br>


### 3. BM25 é mais adequado para Recuperação de Informação (IR)

O problema central do projeto é:

> Quais fontes possuem maior concentração de conteúdo relevante sobre FIIs?

Esse é um problema clássico de **Recuperação de Informação (IR)**.

O BM25 foi projetado exatamente para esse contexto e é amplamente utilizado em:

* motores de busca
* sistemas de ranqueamento de documentos
* pipelines de recuperação de informação
* sistemas clássicos de busca semântica

<br><br>

## 5. Comparação BM25 vs TF-IDF

| Critério                        | TF-IDF      | BM25                  | Melhor para o projeto |
| ------------------------------- | ----------- | --------------------- | --------------------- |
| Frequência de termos            | Sim         | Sim                   | Empate                |
| Controle de saturação de termos | ❌ Fraco     | ✅ Forte               | BM25                  |
| Normalização por tamanho        | ⚠️ Limitada | ✅ Forte               | BM25                  |
| Qualidade de ranqueamento       | ⚠️ Básica   | ✅ Robusta             | BM25                  |
| Interpretabilidade              | ✅ Alta      | ✅ Alta                | Empate                |
| Explicabilidade (visão XAI)     | ✅ Sim       | ✅ Sim                 | Empate                |
| Uso em sistemas IR              | ⚠️ Médio    | ✅ Padrão da indústria | BM25                  |
| Robustez multi-fonte            | ⚠️ Média    | ✅ Alta                | BM25                  |

<br><br>

## 🧠 Conclusão

O BM25 é preferido em relação ao TF-IDF neste projeto porque fornece:

* melhor estabilidade de ranqueamento entre fontes heterogêneas;
* melhor normalização para diferentes tamanhos de documentos;
* maior alinhamento com princípios de Recuperação de Informação;
* e mantém interpretabilidade adequada para um sistema inspirado em XAI.
