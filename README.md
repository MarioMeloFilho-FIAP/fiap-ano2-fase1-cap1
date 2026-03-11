# CardioIA - Fase 1 - Cap1: Batimentos de Dados

## Introdução
Dados iniciais do projeto CardioIA para apoio às próximas fases de análise, modelagem e experimentação em Inteligência Artificial aplicada à saúde cardiovascular.
Além da coleta, esta fase considera princípios iniciais de Governança de Dados, rastreabilidade, documentação das fontes e análise crítica de possíveis vieses.

---


Além da coleta, esta fase considera princípios iniciais de Governança de Dados, rastreabilidade, documentação das fontes e análise crítica de possíveis vieses.

---

## Decisões adotadas neste projeto

### Dados Numéricos
Foi adotada a **Opção B**, usando o **PTB-XL no PhysioNet** como base principal.
O projeto Python realiza:
- download dos metadados do PTB-XL
- organização tabular dos registros
- geração de um dataset numérico derivado dos metadados
- controle persistente do que já foi baixado via SQLite
- parametrização via CLI
- parametrização via arquivos YAML com as URLs das fontes

### Dados Textuais
Foi criado um projeto Python com CLI para:
- baixar textos médicos/científicos públicos
- limitar a quantidade de arquivos baixados
- manter controle persistente do que já foi baixado
- usar arquivo YAML com as fontes configuradas

### Dados Visuais
Foi adotado o **PTB-XL** também para a parte visual.
O projeto:
- baixa sinais ECG em formato WFDB
- converte os traçados em imagens PNG
- permite definir a quantidade de imagens a gerar por linha de comando

---

## Estrutura do projeto

```text
configs/
src/
README.md
catalog.md
requirements.txt
pyproject.toml
