# BM25 Foundation — Mathematical Reference

**Investor Intelligence Platform - FIIs Brasil 🇧🇷**

## Overview

BM25 (Best Matching 25) is the primary relevance ranking algorithm used to score
the 21 monitored sources by FII content relevance.

## Formula

```
BM25(D,Q) = Σ IDF(qi) · [f(qi,D)·(k1+1)] / [f(qi,D) + k1·(1−b+b·|D|/avgdl)]
```

| Parameter | Default | Effect |
|-----------|---------|--------|
| k1 | 1.5 | Term saturation |
| b  | 0.75 | Length normalization |

## Role in this project

- **BM25** = source relevance ranking layer
- **TF-IDF** = term weighting for topic modeling

## XAI Alignment

Every BM25 score decomposes into per-term contributions (NB05).

## Reference

Robertson & Zaragoza (2009). The Probabilistic Relevance Framework: BM25 and Beyond.
Foundations and Trends in IR, 3(4), 333–389.
