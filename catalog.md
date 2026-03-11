
---

## `sources_catalog.md`

```md
# Sources Catalog - CardioIA Fase 1

## Objetivo
Este catálogo documenta as fontes públicas utilizadas pelo projeto para coleta de dados numéricos, textuais e visuais, além de registrar a finalidade de cada fonte no pipeline.

---

## 1. Fonte principal para dados numéricos e visuais

### PTB-XL - PhysioNet
**Base URL:**  
`https://physionet.org/files/ptb-xl/1.0.3/`

**Metadados principais:**  
- `https://physionet.org/files/ptb-xl/1.0.3/ptbxl_database.csv`
- `https://physionet.org/files/ptb-xl/1.0.3/scp_statements.csv`

**Tipo de dado:**  
- Numérico/tabular
- Sinais ECG
- Visual derivado (PNG gerado localmente)

**Formato:**  
- CSV
- WFDB (`.hea` e `.dat`)
- PNG gerado pelo projeto

**Uso no projeto:**  
- gerar dataset numérico
- baixar registros de ECG
- converter sinais em imagens

**Observações de governança:**  
- fonte pública para pesquisa
- metadados documentados
- rastreável por versão
- exige cuidado com reuso e documentação acadêmica

---

## 2. Fontes textuais

### Texto 1 - Estatística Cardiovascular – Brasil 2023
**URL:**  
`https://www.scielo.br/j/abc/a/jzFMcdN5y3w6CtjVgdJdSdR/?format=pdf&lang=pt`

**Tipo:**  
Texto médico/científico

**Formato original:**  
PDF

**Uso:**  
- saúde pública
- epidemiologia cardiovascular
- extração de entidades e tópicos

---

### Texto 2 - Insuficiência Cardíaca
**URL:**  
`https://www.scielo.br/j/abc/a/VCQkdfNs5QNyTYhp8WdnMdN/?lang=pt`

**Tipo:**  
Texto médico/científico

**Formato original:**  
HTML/PDF conforme disponibilidade

**Uso:**  
- sintomas
- diagnóstico
- tratamento
- classificação de conteúdo clínico

---

### Texto 3 - Prevenção clínica de doenças cardiovasculares, cerebrovasculares e renais
**URL:**  
`https://bvsms.saude.gov.br/bvs/publicacoes/abcad14.pdf`

**Tipo:**  
Documento técnico em saúde pública

**Formato original:**  
PDF

**Uso:**  
- prevenção
- políticas públicas
- organização de conhecimento médico

---

## 3. Mapeamento por entregável

### Numérico
- PTB-XL `ptbxl_database.csv`
- PTB-XL `scp_statements.csv`

### Textual
- SciELO
- BVS / Ministério da Saúde

### Visual
- PTB-XL registros WFDB convertidos em PNG

---

## 4. Observações finais
Todas as fontes listadas aqui devem ser mantidas no README e nos arquivos YAML para garantir:
- rastreabilidade
- reprodutibilidade
- clareza para correção acadêmica
- alinhamento com governança de dados
