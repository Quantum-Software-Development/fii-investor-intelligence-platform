<!-- LANGUAGE BUTTONS -->
**\[[🇧🇷 Português](LGPD_ALIGNMENT.md)\] \[**[🇬🇧 English](../../🇬🇧English/governance/LGPD_ALIGNMENT.md)**\]**

<br><br>

## [Alinhamento com a LGPD]()
### Investor Intelligence Platform — FIIs Brasil 🇧🇷

<br><br>

**Referência:** Brasil. (2018). *Lei nº 13.709 — Lei Geral de Proteção de Dados Pessoais (LGPD).*

<br><br>

## [Avaliação Resumida]()

<br><br>

| Requisito | Status | Evidência |
|---|---|---|
| Dados pessoais processados? | ✅ Não | Apenas conteúdo editorial público |
| Base legal estabelecida? | ✅ Sim | Interesse legítimo (pesquisa acadêmica) |
| Minimização de dados aplicada? | ✅ Sim | Retidos apenas título, corpo, fonte e data |
| Limitação de finalidade? | ✅ Sim | Exclusivamente inteligência de marketing |
| Transparência? | ✅ Sim | Metodologia aberta, fontes documentadas |
| Medidas de segurança? | ✅ Sim | Nenhum PII armazenado; secrets via `st.secrets` |
| Direitos do titular aplicáveis? | N/A | Nenhum dado pessoal coletado |

<br><br>

**Status geral LGPD:** ✅ **Conforme** — fora do escopo de tratamento de dados pessoais.

<br><br>

## [Classificação de Dados]()

<br><br>

[***Dados Coletados e Processados***]()

<br><br>

| Tipo de Dado | Classificação | Aplicabilidade LGPD |
|---|---|---|
| Título do artigo | Conteúdo editorial público | Não é dado pessoal |
| Corpo do artigo | Conteúdo editorial público | Não é dado pessoal |
| Domínio do portal | Identificador técnico | Não é dado pessoal |
| Data de publicação | Metadado | Não é dado pessoal |
| Nome do autor (RSS) | Potencialmente pessoal | Minimizado — usado apenas no campo `author` |

<br><br>

[***Dados NÃO Coletados***]()

<br><br>

- Identidades de usuários
- Endereços IP
- Fingerprints de navegador
- Rastreamento comportamental
- Dados de cookies
- Dados geográficos
- Dados financeiros de indivíduos

<br><br>

## [Base Legal (Art. 7º LGPD)]()

<br><br>

**Art. 7º, IX — Interesse Legítimo:**

<br><br>

O tratamento é conduzido para **pesquisa acadêmica** (Projeto Integrador — PUC-SP FACEI), com interesse legítimo em compreender a dinâmica de canais digitais no mercado de FIIs. O tratamento está limitado a conteúdo editorial publicamente disponível.

<br><br>

**Condições atendidas:**

<br><br>

- Tratamento necessário para finalidade legítima
- Direitos fundamentais dos titulares não são sobrepostos
- Nenhum impacto adverso sobre indivíduos

<br><br>

## [Nomes de Autores de Artigos — Consideração Especial]()

<br><br>

Feeds RSS podem incluir nomes de autores (ex.: "Maria Silva"). Tratamento:

<br><br>

1. **Armazenado como metadado** para atribuição de fonte, não para profiling
2. **Não cruzado** com nenhuma base de dados pessoal
3. **Não publicado** nos outputs do dashboard
4. **Minimizado** — usado apenas para documentação de proveniência de dados
5. **Removível** — o campo `author` pode ser descartado sem impactar nenhuma análise

<br><br>

> **Recomendação:** em caso de deploy público além do escopo acadêmico, remover o campo `author` durante a transformação Silver.

<br><br>

## [Retenção de Dados]()

<br><br>

| Camada | Retenção | Justificativa |
|---|---|---|
| Bronze | Duração do projeto | Trilha de auditoria para avaliação acadêmica |
| Silver | Duração do projeto | Requisito de reprodutibilidade |
| Gold | Duração do projeto | Serving da API em produção |
| External (frozen) | Indefinida | Reprodutibilidade determinística |

<br><br>

Pós-projeto: todas as camadas exceto `data/external/` devem ser removidas do armazenamento local.

<br><br>

## [Dados do Reddit — Considerações Adicionais]()

<br><br>

Posts do Reddit são **conteúdo publicamente visível**. Entretanto:

<br><br>

- Usernames podem ser pseudônimos (não necessariamente anonimizados)
- Posts são coletados de **subreddits focados em investimento** (`r/investimentos`, `r/farialimabets`)
- Nenhum cruzamento com outros datasets ocorre
- Reddit é **apenas a Camada Comportamental (Fonte #21)** — pode ser totalmente excluído sem impacto no restante do pipeline

<br><br>

> **Recomendação:** para deploy público, remover o campo `author` do Reddit e usar apenas título e corpo do post.

<br><br>

## [Dashboard — Privacidade do Usuário]()

<br><br>

O dashboard Streamlit:

<br><br>

- Coleta **nenhum dado de usuário**
- Não usa **cookies** (comportamento padrão do Streamlit com `gatherUsageStats = false`)
- Não registra **endereços IP** (responsabilidade do Streamlit Cloud)
- Não requer **autenticação**
- Não possui **contas de usuário**

<br><br>

## [Contato e Supervisão]()

<br><br>

| Papel | Pessoa / Instituição |
|---|---|
| Supervisão acadêmica | Eduardo Savino Gomes · Carlos Eduardo Paes — PUC-SP / FACEI |
| Autora e controladora de dados | Fabiana Campanari |
| Instituição | Pontifícia Universidade Católica de São Paulo |

<br><br>

## [Ver Também]()

<br><br>

- **[`RESPONSIBLE_AI.md`](RESPONSIBLE_AI.md)** — documentação mais ampla de IA Responsável e model cards
- **[`RISK_REGISTER.md`](RISK_REGISTER.md)** — riscos de privacidade (R12) e suas mitigações
- **[`DOCUMENTO_OFICIAL.md`](../documento_oficial/DOCUMENTO_OFICIAL.md)**, seção 19 — resumo de LGPD em contexto

<br><br>

---

<br><br>

*Alinhamento com a LGPD v2.0.0 · Investor Intelligence Platform FIIs Brasil*
