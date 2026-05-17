
# 🏗️ HDFS vs MinIO

<br><br>

## Overview

The project architecture uses **MinIO** as a modern, lightweight, and academic alternative to **HDFS (Hadoop Distributed File System)**.

<br><br>

## Comparison

| HDFS | MinIO |
|---|---|
| Traditional Hadoop ecosystem | Modern object storage |
| More complex to configure | Simple and lightweight |
| Advanced cluster setup | Easy deployment via Docker |
| Hadoop ecosystem dependency | S3 (AWS)-compatible |

<br><br>

## What is MinIO?

**MinIO** is an **object storage platform compatible with the S3 (Amazon Simple Storage Service) standard**.

It works as a **lightweight local data lake**, widely used in:

- data engineering  
- analytics pipelines  
- machine learning  
- distributed systems  
- academic environments  
- Lakehouse architectures  

<br><br>

## 🧠 Simple Explanation

MinIO works like a “**technical Google Drive**” for data applications.

It stores different types of files used in modern data pipelines, such as:

- JSON  
- Parquet  
- datasets  
- images  
- logs  
- Spark outputs  
- NLP results  

<br><br>

## 📦 What is Object Storage?

Unlike folder-based systems:

```

/folder/file.txt

```

object storage organizes data as:

```

bucket/object

```

Example:

```

s3://bronze/raw/news_001.json

```

<br><br>

## 🏗️ MinIO Usage in This Project

MinIO is used as a **Data Lake**, organized into layers:

| Layer | Function |
|---|---|
| Bronze | Raw data |
| Silver | Cleaned data |
| Gold | Analytical data |

<br><br>

## 🔄 Project Pipeline

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

````

<br><br>

## Why use MinIO?

- lightweight and fast  
- Docker-friendly  
- local AWS S3 simulation  
- easy Spark integration  
- ideal for academic projects  
- used in real-world data architectures  

<br><br>

## Why MinIO instead of HDFS?

Although HDFS is traditional in Hadoop ecosystems, MinIO is more suitable for this project because:

- easier to set up  
- more modern  
- runs locally without a complex cluster  
- better suited for portfolio projects  
- aligned with modern cloud architectures  

Today, many systems use:

- **Amazon S3**  
- **MinIO**  
- **Lakehouse storage (Delta/Iceberg)**  

instead of raw Hadoop stacks.

<br><br>

## 🧩 Real Example

The scraper stores data in MinIO:

```json
{
  "title": "REITs pay record dividends",
  "content": "...",
  "source": "InfoMoney"
}
````

In the bucket:

```
s3://bronze/infomoney/2026/05/article_001.json
```

Then Spark reads it:

```python
spark.read.json("s3a://bronze/infomoney/*")
```

<br><br>

## Summary

MinIO works as:

* distributed storage
* S3-compatible system
* data lake foundation
* Spark-integrated storage layer
* modern alternative to HDFS

In this project, it replaces HDFS while preserving the same architectural concepts, with greater simplicity, scalability, and modern cloud compatibility.


