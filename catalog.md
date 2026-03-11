# Sources Catalog - CardioIA Fase 1

## Visão geral
Este catálogo documenta de forma estruturada todas as fontes públicas utilizadas no projeto **CardioIA - Fase 1: Batimentos de Dados**.

O objetivo deste arquivo é registrar:

- a origem de cada conjunto de dados
- o tipo de dado associado a cada fonte
- o formato original dos arquivos
- a finalidade de uso dentro do projeto
- observações relevantes de governança, rastreabilidade e reprodutibilidade

Este documento complementa o `README.md` e fortalece a transparência da coleta e preparação dos dados.

---

## 1. Fonte principal para dados numéricos e visuais

## PTB-XL - PhysioNet

### Identificação da fonte
**Nome da base:** PTB-XL  
**Repositório:** PhysioNet  
**Versão utilizada:** 1.0.3

### URL base
`https://physionet.org/files/ptb-xl/1.0.3/`

### Tipo de dado
- dados numéricos
- metadados clínicos
- sinais de ECG
- dados visuais derivados

### Papel da base no projeto
O PTB-XL foi adotado como a fonte principal do projeto para duas frentes:

1. **Dados numéricos**  
   Os metadados dos exames são organizados em um dataset tabular para uso posterior em análise e modelagem.

2. **Dados visuais**  
   Os sinais de ECG são baixados em formato WFDB e convertidos localmente em imagens PNG para uso em tarefas futuras de Visão Computacional.

### Justificativa da escolha
O PTB-XL foi escolhido por ser uma base pública, amplamente utilizada em pesquisa e altamente coerente com a proposta de um projeto de IA em cardiologia. A base oferece traçados reais de eletrocardiograma, metadados associados e informações diagnósticas relevantes para tarefas multimodais.

---

## 2. Fontes numéricas do PTB-XL

### 2.1 PTB-XL Database CSV

**URL:**  
`https://physionet.org/files/ptb-xl/1.0.3/ptbxl_database.csv`

**Tipo de dado:**  
Dados numéricos e metadados tabulares

**Formato original:**  
CSV

**Uso no projeto:**  
Este arquivo é a principal fonte para geração do dataset numérico. Ele contém informações estruturadas sobre os exames e permite extrair variáveis como:

- `ecg_id`
- `patient_id`
- `age`
- `sex`
- `height`
- `weight`
- `recording_date`
- `device`
- `site`
- `report`
- `heart_axis`
- `infarction_stadium1`
- `infarction_stadium2`
- `scp_codes`
- `filename_lr`
- `filename_hr`

**Saída gerada no projeto:**  
`output/numeric/ptbxl_numeric_dataset.csv`

**Observações de governança:**  
- fonte pública e rastreável
- versão explicitamente documentada
- estrutura adequada para reprodutibilidade
- usada como origem oficial do dataset tabular derivado

---

### 2.2 SCP Statements CSV

**URL:**  
`https://physionet.org/files/ptb-xl/1.0.3/scp_statements.csv`

**Tipo de dado:**  
Dicionário diagnóstico / tabela de apoio

**Formato original:**  
CSV

**Uso no projeto:**  
Esse arquivo funciona como apoio interpretativo aos códigos SCP presentes no `ptbxl_database.csv`. Ele é importante para contextualizar os códigos diagnósticos e facilitar análises futuras relacionadas à classificação clínica.

**Uso futuro potencial:**  
- interpretação de rótulos diagnósticos
- agrupamento por categorias clínicas
- enriquecimento semântico do dataset numérico
- criação de tarefas supervisionadas

**Observações de governança:**  
- mantém consistência entre os metadados e os códigos diagnósticos
- importante para documentação do significado clínico das classes

---

## 3. Fontes visuais derivadas do PTB-XL

### 3.1 Registros WFDB do PTB-XL

**URL base:**  
`https://physionet.org/files/ptb-xl/1.0.3/`

**Tipo de dado:**  
Sinais de ECG

**Formato original:**  
WFDB  
Arquivos utilizados:
- `.hea`
- `.dat`

**Uso no projeto:**  
Os sinais são baixados a partir dos caminhos relativos presentes nas colunas:

- `filename_lr`
- `filename_hr`

Com base nesses caminhos, o projeto gera automaticamente as URLs dos arquivos do exame e realiza o download dos pares:

- `<relative_path>.hea`
- `<relative_path>.dat`

### Exemplo lógico de montagem de URL
Se o caminho relativo do exame for algo como:

`records100/00000/00001_lr`

o projeto monta:

- `https://physionet.org/files/ptb-xl/1.0.3/records100/00000/00001_lr.hea`
- `https://physionet.org/files/ptb-xl/1.0.3/records100/00000/00001_lr.dat`

### Saída gerada no projeto
Os sinais baixados são convertidos localmente em imagens PNG armazenadas em:

- `output/images/ptbxl/*.png`

### Finalidade no projeto
As imagens geradas poderão ser utilizadas futuramente em tarefas como:

- classificação visual de ECG
- reconhecimento de padrões do traçado
- comparação entre exames normais e alterados
- experimentos com Visão Computacional

### Observações de governança
- as imagens não são baixadas prontas; elas são geradas localmente
- isso melhora a rastreabilidade do processo
- o pipeline deixa explícita a relação entre a fonte original e o artefato visual produzido

---

## 4. Fontes textuais

## 4.1 Estatística Cardiovascular – Brasil 2023

**URL:**  
`https://www.scielo.br/j/abc/a/jzFMcdN5y3w6CtjVgdJdSdR/?format=pdf&lang=pt`

**Origem:**  
SciELO

**Tipo de dado:**  
Texto médico-científico

**Formato original:**  
PDF

**Categoria no projeto:**  
Cardiologia e saúde pública

**Uso no projeto:**  
Esse texto foi selecionado para compor a base textual do projeto por conter informações relevantes sobre epidemiologia cardiovascular, indicadores de saúde e panorama nacional das doenças cardiovasculares.

**Aplicações futuras em NLP:**  
- extração de tópicos
- sumarização
- identificação de termos médicos
- organização de conhecimento sobre saúde cardiovascular

**Saída gerada no projeto:**  
`output/texts/estatistica_cardiovascular_brasil_2023.txt`

**Observações de governança:**  
- fonte pública
- origem confiável
- conteúdo útil para contextualização epidemiológica
- adequado para enriquecimento textual do projeto

---

## 4.2 Insuficiência Cardíaca

**URL:**  
`https://www.scielo.br/j/abc/a/VCQkdfNs5QNyTYhp8WdnMdN/?lang=pt`

**Origem:**  
SciELO

**Tipo de dado:**  
Texto médico-científico

**Formato original:**  
HTML ou PDF, conforme a disponibilidade do acesso

**Categoria no projeto:**  
Cardiologia clínica

**Uso no projeto:**  
Esse texto foi escolhido por tratar de sintomas, diagnóstico, fisiopatologia e tratamento da insuficiência cardíaca, tema altamente relevante para IA em cardiologia.

**Aplicações futuras em NLP:**  
- extração de sintomas
- extração de entidades clínicas
- classificação de tópicos clínicos
- construção de base de conhecimento

**Saída gerada no projeto:**  
`output/texts/insuficiencia_cardiaca.txt`

**Observações de governança:**  
- fonte pública e acadêmica
- conteúdo clinicamente relevante
- útil para tarefas de NLP orientadas à cardiologia

---

## 4.3 Prevenção clínica de doenças cardiovasculares, cerebrovasculares e renais

**URL:**  
`https://bvsms.saude.gov.br/bvs/publicacoes/abcad14.pdf`

**Origem:**  
BVS / Ministério da Saúde

**Tipo de dado:**  
Documento técnico em saúde pública

**Formato original:**  
PDF

**Categoria no projeto:**  
Saúde pública e prevenção

**Uso no projeto:**  
Esse documento foi incluído para enriquecer a base textual com material técnico sobre prevenção clínica, políticas de cuidado e abordagem ampliada das doenças cardiovasculares.

**Aplicações futuras em NLP:**  
- organização de temas de prevenção
- mineração de termos clínicos
- sumarização
- apoio a sistemas de busca semântica
- recuperação de conhecimento em saúde pública

**Saída gerada no projeto:**  
`output/texts/prevencao_clinica_dcv.txt`

**Observações de governança:**  
- documento público institucional
- forte relevância em prevenção e saúde coletiva
- complementa os textos clínicos e epidemiológicos

---

## 5. Mapeamento entre fonte e entregável

## 5.1 Dados numéricos
**Fontes utilizadas:**
- `ptbxl_database.csv`
- `scp_statements.csv`

**Entregável gerado:**
- `output/numeric/ptbxl_numeric_dataset.csv`

---

## 5.2 Dados textuais
**Fontes utilizadas:**
- Estatística Cardiovascular – Brasil 2023
- Insuficiência Cardíaca
- Prevenção clínica de doenças cardiovasculares, cerebrovasculares e renais

**Entregáveis gerados:**
- `output/texts/estatistica_cardiovascular_brasil_2023.txt`
- `output/texts/insuficiencia_cardiaca.txt`
- `output/texts/prevencao_clinica_dcv.txt`

---

## 5.3 Dados visuais
**Fonte utilizada:**
- registros WFDB do PTB-XL

**Entregáveis gerados:**
- `output/images/ptbxl/*.png`

---

## 6. Arquivos de configuração relacionados às fontes

## `configs/ptbxl_sources.yaml`
Este arquivo centraliza:
- URL base do PTB-XL
- URLs dos arquivos de metadados
- resolução dos registros a utilizar
- caminhos locais de saída

## `configs/text_sources.yaml`
Este arquivo centraliza:
- lista das fontes textuais
- nomes lógicos de cada documento
- categorias
- caminhos locais de saída

Esses arquivos fazem parte da estratégia de reprodutibilidade e governança do pipeline.

---

## 7. Controle de rastreabilidade

O projeto mantém um registro persistente do que já foi baixado e processado em:

- `state/manifest.db`

Esse mecanismo permite:

- evitar downloads duplicados
- manter histórico local de processamento
- facilitar reruns do pipeline
- melhorar rastreabilidade técnica da coleta

---

## 8. Observações sobre governança de dados

As fontes listadas neste catálogo foram escolhidas com base nos seguintes critérios:

- relevância clínica
- acesso público
- utilidade para IA em saúde
- possibilidade de rastreabilidade
- coerência com o tema cardiológico do projeto

Mesmo sendo fontes públicas e acadêmicas, o uso futuro desses dados deve considerar:

- possíveis vieses de amostragem
- limitações populacionais
- diferenças entre protocolos clínicos
- restrições de generalização
- necessidade de contextualização diagnóstica

---

## 9. Conclusão
O conjunto de fontes documentado neste catálogo fornece a base multimodal da Fase 1 do CardioIA. A combinação entre PTB-XL, artigos científicos e documentos técnicos em saúde pública cria uma estrutura consistente para alimentar etapas futuras de análise, experimentação e desenvolvimento de soluções de Inteligência Artificial aplicadas à cardiologia.
