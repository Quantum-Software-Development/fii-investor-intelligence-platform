
# 🏗️ HDFS vs MinIO

<br><br>

## Visão Geral

A arquitetura do projeto utiliza o **MinIO** como uma alternativa moderna, leve e acadêmica ao **HDFS (Hadoop Distributed File System)**.

<br><br>

## Comparação

| HDFS | MinIO |
|---|---|
| Hadoop tradicional | Object Storage moderno |
| Mais complexo de configurar | Simples e leve |
| Setup avançado em cluster | Execução fácil via Docker |
| Ecossistema Hadoop | Compatível com S3 (AWS) |

<br><br>

## O que é MinIO?

O **MinIO** é uma plataforma de **armazenamento de objetos compatível com o padrão S3 (Amazon Simple Storage Service)**.

Ele funciona como um **data lake leve e local**, amplamente utilizado em:

- engenharia de dados  
- pipelines de analytics  
- machine learning  
- sistemas distribuídos  
- ambientes acadêmicos  
- arquiteturas Lakehouse  

<br><br>

## 🧠 Explicação Simples

O MinIO funciona como um “**Google Drive técnico**” para aplicações de dados.

Ele armazena diferentes tipos de arquivos usados em pipelines modernos, como:

- JSON  
- Parquet  
- datasets  
- imagens  
- logs  
- outputs do Spark  
- resultados de NLP  

<br><br>

## 📦 O que é Object Storage?

Diferente de sistemas baseados em pastas:

```

/pasta/arquivo.txt

```

o object storage organiza dados como:

```
bucket/objeto
```

Exemplo:

```
s3://bronze/raw/news_001.json
```

<br><br>


## 🏗️ Uso do MinIO neste Projeto

O MinIO é utilizado como um **Data Lake**, organizado em camadas:

| Camada | Função |
|---|---|
| Bronze | Dados brutos |
| Silver | Dados tratados |
| Gold | Dados analíticos |

<br><br>

## 🔄 Fluxo do Projeto

```
Scrapers
↓
MinIO (Bronze)
↓
PySpark ETL
↓
MinIO (Silver)
↓
NLP + Sentiment Analysis
↓
MinIO (Gold)
↓
Dashboard + FastAPI
```

<br><br>

## Por que usar MinIO?

- leve e rápido  
- compatível com Docker  
- simula AWS S3 localmente  
- fácil de integrar com Spark  
- ideal para projetos acadêmicos  
- usado em arquiteturas reais de dados  

<br><br>

## Por que MinIO no lugar do HDFS?

Embora o HDFS seja tradicional em ecossistemas Hadoop, o MinIO é mais adequado para este projeto porque:

- é mais simples de configurar  
- é mais moderno  
- funciona localmente sem cluster complexo  
- é mais adequado para portfólio acadêmico  
- se alinha com arquiteturas cloud modernas  

Hoje, muitos sistemas utilizam:

- **Amazon S3**  
- **MinIO**  
- **Lakehouse storage (Delta/Iceberg)**  

em vez de Hadoop puro.

<br><br>

## 🧩 Exemplo Real

O scraper salva dados no MinIO:

```json
{
  "title": "FIIs pagam dividendos recordes",
  "content": "...",
  "source": "InfoMoney"
}
```

No bucket:

```
s3://bronze/infomoney/2026/05/article_001.json
```

Depois o Spark consome:

```python
spark.read.json("s3a://bronze/infomoney/*")
```

<br><br>

## Resumo

O MinIO funciona como:

* armazenamento distribuído
* compatível com S3
* base de Data Lake
* integração com Spark
* suporte a pipelines de engenharia de dados
* alternativa moderna ao HDFS

No projeto, ele substitui o HDFS mantendo os mesmos conceitos de arquitetura, porém com maior simplicidade, escalabilidade e aderência a ambientes modernos.



