# CardioIA - Fase 1 - Cap1: Batimentos de Dados

## Visão geral
Este repositório reúne os dados iniciais do projeto **CardioIA** para apoio às próximas fases de análise, modelagem e experimentação em Inteligência Artificial aplicada à saúde cardiovascular.

A proposta desta fase é organizar três tipos de dados:

1. **Dados numéricos** de pacientes e exames cardíacos  
2. **Dados textuais** relacionados à saúde cardiovascular  
3. **Dados visuais** de exames cardiológicos  

Além da coleta, esta fase considera princípios iniciais de **Governança de Dados**, rastreabilidade, documentação das fontes e análise crítica de possíveis vieses.

---

## Objetivo do projeto
O objetivo deste projeto é construir uma base inicial para o CardioIA, permitindo que, nas fases seguintes, sejam desenvolvidos modelos de Inteligência Artificial capazes de trabalhar com:

- dados tabulares e clínicos
- textos médicos e técnicos
- sinais e imagens de exames cardiológicos

A base construída nesta fase foi planejada para servir de apoio a atividades futuras como:

- classificação diagnóstica
- análise comparativa entre grupos de pacientes
- extração de conhecimento clínico por NLP
- reconhecimento de padrões em exames cardiológicos por Visão Computacional
- Preparação para Exploração de dados sensíveis levando em conta questões (bio)éticas

---
## Link Todos os dados
[Link Dropbox](https://www.dropbox.com/scl/fo/t1upiupbbj59hg48tlcnz/AHW3rXgl24x4vh9Wl8DstBA?rlkey=z8ea1294h03qb1o94heiroywu&st=8qhqspiv&dl=0)
---

## 1. Dados Numéricos

### Base escolhida
Para a parte numérica do projeto foi adotada a base **PTB-XL**, disponibilizada no **PhysioNet**.

O PTB-XL é um grande conjunto de dados de eletrocardiogramas de 12 derivações, amplamente utilizado em pesquisa médica e em projetos de Inteligência Artificial aplicada à cardiologia. A base contém metadados clínicos e diagnósticos associados aos exames, o que permite a construção de um dataset numérico estruturado para análises futuras.

### Origem dos dados
Os dados utilizados nesta etapa são **reais**, públicos e disponibilizados para pesquisa científica por meio do PhysioNet.

### Fontes utilizadas
- `https://physionet.org/files/ptb-xl/1.0.3/ptbxl_database.csv`
- `https://physionet.org/files/ptb-xl/1.0.3/scp_statements.csv`


### Arquivo gerado no projeto
- [data/numeric/ptbxl_numeric_dataset.csv](https://www.dropbox.com/scl/fi/37v16zzlcebbb86vmqh4e/ptbxl_numeric_dataset.csv?rlkey=q0zjc1t5swm46exmfowh9yb7r&st=obrhr9f0&dl=0)

### Variáveis de maior relevância clínica
A partir do PTB-XL, o projeto organiza um dataset numérico derivado dos metadados do exame. Entre as variáveis consideradas mais relevantes estão:

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

### Justificativa clínica
Essas variáveis são importantes porque permitem relacionar cada exame a informações demográficas, técnicas e diagnósticas. Do ponto de vista clínico e computacional, elas podem ser usadas em tarefas como:

- classificação de exames
- estratificação por perfis de pacientes
- agrupamento por características clínicas
- associação entre metadados e padrões do ECG
- construção de modelos de apoio à decisão

Mesmo quando algumas dessas variáveis não representam diretamente fatores de risco tradicionais como pressão arterial e colesterol, elas são altamente relevantes no contexto do PTB-XL porque conectam o sinal do ECG ao contexto clínico e diagnóstico do exame.

---

## 2. Dados Textuais

### Fontes escolhidas
Para a parte textual do projeto foram selecionados documentos e artigos públicos relacionados à cardiologia, saúde pública e prevenção de doenças cardiovasculares.

As fontes utilizadas foram:

1. **Estatística Cardiovascular – Brasil 2023**  
   URL:  
   `https://www.scielo.br/j/abc/a/jzFMcdN5y3w6CtjVgdJdSdR/?format=pdf&lang=pt`

2. **Insuficiência Cardíaca**  
   URL:  
   `https://www.scielo.br/j/abc/a/VCQkdfNs5QNyTYhp8WdnMdN/?lang=pt`

3. **Prevenção clínica de doenças cardiovasculares, cerebrovasculares e renais**  
   URL:  
   `https://bvsms.saude.gov.br/bvs/publicacoes/abcad14.pdf`

### Origem dos dados textuais
Os textos utilizados são **reais**, públicos e provenientes de fontes confiáveis da área de saúde, incluindo SciELO e BVS/Ministério da Saúde.

### Arquivos gerados no projeto
Os textos baixados e convertidos ficam armazenados em: [Dados Textuais](https://www.dropbox.com/scl/fo/873q0pnen8w2n7r7ovmid/AJ4SONdWa1oBqe62IVYO4Ak?rlkey=u0nlfqrm5hu4emrgq94166o0x&st=3k70d3xl&dl=0)

- `output/texts/estatistica_cardiovascular_brasil_2023.txt`
- `output/texts/insuficiencia_cardiaca.txt`
- `output/texts/prevencao_clinica_dcv.txt`

### Link para armazenamento público
Todos os dados utilizados e gerados: [Dados Textuais](https://www.dropbox.com/scl/fo/873q0pnen8w2n7r7ovmid/AJ4SONdWa1oBqe62IVYO4Ak?rlkey=u0nlfqrm5hu4emrgq94166o0x&st=3k70d3xl&dl=0) 

### Possíveis aplicações de NLP
Os textos selecionados podem ser explorados por algoritmos de Processamento de Linguagem Natural em tarefas como:

- extração de sintomas
- identificação de fatores de risco
- classificação de tópicos
- sumarização automática
- extração de entidades clínicas
- construção de base de conhecimento médico
- apoio a busca semântica e recuperação de informação

### Relevância para IA em saúde
Esses textos são relevantes porque reúnem informações sobre epidemiologia, sintomas, tratamento, prevenção e organização do cuidado cardiovascular. Isso permite que o projeto utilize dados textuais como complemento aos dados tabulares e visuais, tornando a base mais rica e mais próxima de um cenário real de IA em saúde.

---

## 3. Dados Visuais

### Base escolhida
Para a parte visual do projeto também foi adotado o **PTB-XL**, utilizando os sinais de ECG em formato WFDB como fonte para geração de imagens.

O projeto baixa os arquivos do exame e converte os sinais em imagens PNG, permitindo a criação de um conjunto visual a partir de registros reais de eletrocardiograma.

### Origem dos dados
Os dados visuais são derivados de exames reais públicos disponibilizados no PhysioNet. As imagens não são baixadas prontas; elas são **geradas localmente pelo projeto Python** a partir dos sinais do ECG.

### Fonte utilizada
Base principal:
- `https://physionet.org/files/ptb-xl/1.0.3/`

Os sinais são obtidos a partir dos caminhos relativos presentes nas colunas:
- `filename_lr`
- `filename_hr`

A partir desses caminhos, o projeto monta e baixa pares de arquivos:

- `<relative_path>.hea`
- `<relative_path>.dat`

### Arquivos gerados no projeto
As imagens geradas ficam armazenadas em:

- `output/images/ptbxl/*.png`

### Quantidade mínima de imagens
O projeto foi preparado para gerar pelo menos **100 imagens** de ECG, atendendo ao requisito da atividade.

### Link para armazenamento público
Imagens Geradas: [Imagens](https://www.dropbox.com/scl/fo/kqou384d562s9pnbppq8z/AEMAWIlYb2VNYHrey7RqUPQ?rlkey=g9cq58qvg2023pwjogz07ylx3&st=m5uzbjdb&dl=0)

### Possíveis aplicações de Visão Computacional
As imagens de ECG produzidas a partir do PTB-XL podem ser utilizadas por algoritmos de Visão Computacional para:

- reconhecimento de padrões no traçado
- classificação entre exames normais e alterados
- detecção de anomalias morfológicas
- comparação entre grupos diagnósticos
- apoio à triagem automatizada

### Relevância para IA em saúde
A análise visual de traçados de ECG é altamente relevante em cardiologia. Ao converter os sinais em imagens, o projeto cria uma base que pode ser usada futuramente em experimentos com redes neurais convolucionais, classificação supervisionada e comparação entre abordagens baseadas em sinal bruto e imagem.

---

## Automação do processo de coleta

### Projeto Python desenvolvido
Foi criado um projeto Python com interface de linha de comando para automatizar a coleta e preparação dos dados.

O projeto possui dois fluxos principais:

1. **PTB-XL**
   - baixa metadados
   - gera dataset numérico
   - baixa registros de ECG
   - converte os sinais em imagens PNG

2. **Textos**
   - baixa documentos textuais
   - converte conteúdos em `.txt`
   - organiza os arquivos para uso futuro em NLP

### Parametrização
O projeto foi construído para ser reutilizável e reproduzível, contendo:

- CLI parametrizada com quantidade de registros a baixar
- arquivos YAML com as fontes utilizadas
- controle persistente do que já foi baixado
- rastreabilidade local via banco SQLite

### Controle de downloads
O estado dos downloads e do processamento é mantido em:

- `state/manifest.db`

Isso evita retrabalho, impede duplicidade e melhora a governança do pipeline.

---

## Como executar o projeto

### 1. Criar ambiente virtual
    python -m venv .venv
    source .venv/bin/activate

### 2. Instalar dependências
    pip install -U pip
    pip install -r requirements.txt
    pip install -e .

### 3. Baixar e processar PTB-XL
    cardioia ptbxl --config configs/ptbxl_sources.yaml --count 100

### 4. Baixar textos
    cardioia texts --config configs/text_sources.yaml --count 3

---

## Arquivos de configuração

### `configs/ptbxl_sources.yaml`
Arquivo responsável por definir:
- URL base do PTB-XL
- URLs dos metadados
- resolução dos sinais (`lr` ou `hr`)
- caminhos locais de saída

### `configs/text_sources.yaml`
Arquivo responsável por definir:
- lista de textos públicos
- nomes lógicos de cada fonte
- categorias textuais
- caminhos locais de saída

---

## Governança de Dados e Viés

### Governança
A governança de dados foi considerada desde a estruturação inicial do projeto. Foram adotadas as seguintes práticas:

- documentação clara da origem de cada base
- uso de fontes públicas e rastreáveis
- separação entre dados numéricos, textuais e visuais
- parametrização centralizada por YAML
- registro persistente do que já foi baixado
- organização de saídas por categoria
- reprodutibilidade do pipeline

Essas medidas ajudam a garantir clareza, rastreabilidade e maior facilidade de auditoria acadêmica e técnica.

### Possíveis vieses
Mesmo sendo uma base pública e amplamente utilizada, o PTB-XL e os textos selecionados podem apresentar limitações importantes, como:

- desbalanceamento entre classes diagnósticas
- distribuição desigual por sexo e idade
- população limitada ao contexto de origem da base
- diferenças entre protocolos clínicos e institucionais
- ruído ou inconsistência em rótulos e laudos
- limitações de generalização para outros cenários clínicos

Esses fatores devem ser considerados nas próximas fases do CardioIA para evitar conclusões indevidas e melhorar a confiabilidade dos modelos.

---

## Entregáveis

- um `README.md` detalhado
- automação em Python para coleta dos dados
- configuração por arquivos YAML
- controle do estado de downloads
- organização dos dados textuais, numéricos e visuais
- catálogo das fontes em `sources_catalog.md`
- preparação para hospedagem pública dos artefatos em Google Drive, OneDrive ou equivalente

---

## Catálogo das fontes
O detalhamento completo das fontes utilizadas está disponível em:

- `catalog.md`

---



## Conclusões
Esta fase representa a construção da base multimodal do CardioIA. Ao reunir dados tabulares, textuais e visuais em uma única estrutura organizada e reproduzível, o projeto estabelece uma fundação sólida para as próximas etapas de análise, treinamento de modelos e desenvolvimento de soluções inteligentes em cardiologia.

A escolha do **PTB-XL** como fonte principal para dados numéricos e visuais trouxe maior coerência clínica ao projeto, enquanto os textos selecionados ampliam a capacidade futura de exploração com técnicas de NLP. Além disso, a preocupação com governança, rastreabilidade e viés fortalece a qualidade técnica e acadêmica desta entrega.


---

## Estrutura do repositório

    ├── .gitignore
    ├── pyproject.toml
    ├── requirements.txt
    ├── README.md
    ├── sources_catalog.md
    ├── configs/
    │   ├── ptbxl_sources.yaml
    │   └── text_sources.yaml
    ├── data/  (Compartilhado no Dropbox)
    │   ├── downloads
    │   └── imagens
    │   └── numeric
    │   └── state
    └── src/
        └── cardioia/
            ├── __init__.py
            ├── cli.py
            ├── config.py
            ├── state.py
            ├── utils.py
            └── downloader/
                ├── __init__.py
                ├── ptbxl.py
                └── texts.py

---

## Executando Projeto - geração dos dados


Execute o make, que já tem mapeado os comandos
```bash
make
```

ou pode criar o ambiente manualmente

```bash
python -m venv .venv
source .venv/bin/activate
```

```bash
pip install -U pip
pip install -r requirements.txt
pip install -e .
```

Gerando os arquivos (download, conversão e armazenamento de estado)

baixa dados numericos e imagens
```bash
cardioia ptbxl --config configs/ptbxl_sources.yaml --count 100
```

baixa dados textuais

```bash
cardioia texts --config configs/text_sources.yaml --count 3
```
