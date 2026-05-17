# 🥇 Arquitetura Medallion

<br><br>

## Visão Geral

A Arquitetura Medallion organiza os dados em múltiplas camadas de processamento, melhorando a estrutura, a qualidade e a escalabilidade ao longo do pipeline de dados.

<br><br>

## Camada Bronze

Camada de ingestão de dados brutos.

<br>

- dados não processados  
- coletados diretamente das fontes  
- armazenados sem alterações  
- contêm ruído e inconsistências  

<br><br>

## Camada Silver

Camada de dados limpos e padronizados.

<br>

- limpeza e normalização de dados  
- remoção de inconsistências  
- estruturação dos dados  
- preparação para análise  

<br><br>

## Camada Gold

Camada de dados analíticos e prontos para negócio.

<br>

- datasets agregados  
- estrutura pronta para analytics  
- suporte para dashboards e modelos de ML  
- otimização para geração de insights  

<br><br>

## Aplicação

O pipeline segue um fluxo estruturado:





























