# DataOps AWS - Pipeline Titanic

Este projeto demonstra um pipeline DataOps completo utilizando AWS (S3, Glue, Athena), Python, YAML e boas práticas de Engenharia de Dados, com dados reais do Titanic.

## Estrutura

```
etl/
  extract.py      # Baixa e envia dados crus para o S3
  transform.py    # Lê do S3, transforma e salva no S3
  load.py         # Simula carga final
analytics/
  data_quality.py # Checagem de qualidade dos dados
  query_athena.py # Executa consulta Athena
config/
  config.yaml           # Configurações do pipeline
  dataops_infra.yaml    # Configuração da infraestrutura DataOps
scripts/
  create_athena_table.sql  # SQL para criar tabela no Athena
  create_glue_crawler.py   # Script para criar Glue Crawler
  setup_dataops_infra.py   # Script para criar toda a infraestrutura DataOps
  orquestrador_etl.py      # Orquestrador do pipeline ETL
tests/
  test_extract.py, test_transform.py, test_load.py, test_data_quality.py
docs/
  roteiro_aula.md          # Roteiro didático para as aulas
requirements.txt
README.md
.gitignore
```

## Cronograma Didático
Veja o cronograma completo em `docs/roteiro_aula.md` para sugestões de aulas, atividades e desafios.

## Pré-requisitos
- AWS CLI configurado (`aws configure`)
- Permissões para S3, Glue e Athena
- Role do Glue criada e ARN ajustado em `config/dataops_infra.yaml`

## Instalação
```bash
pip install -r requirements.txt
```

## Setup da Infraestrutura DataOps
1. Edite `config/dataops_infra.yaml` com o nome do bucket, pastas, Glue Database, Crawler e ARN da role do Glue.
2. Execute:
   ```bash
   python scripts/setup_dataops_infra.py
   ```
   Isso irá criar:
   - Bucket S3 (se não existir)
   - Pastas (prefixos) no bucket
   - Glue Database
   - Glue Crawler

3. Execute o Glue Crawler pelo console AWS para catalogar os dados após a extração/transformação.
4. Crie a tabela Athena executando o SQL em `scripts/create_athena_table.sql` no console Athena.

## Execução Automática do Pipeline ETL
Execute todo o pipeline de ETL e análise com apenas um comando:

```bash
python scripts/orquestrador_etl.py
```

O orquestrador executa, em sequência:
1. Extração dos dados (etl/extract.py)
2. Transformação dos dados (etl/transform.py)
3. Carga final dos dados (etl/load.py)
4. Checagem de qualidade dos dados (analytics/data_quality.py)
5. Consulta analítica no Athena (analytics/query_athena.py)

Se qualquer etapa falhar, o pipeline é interrompido e o erro é exibido.

## Testes
```bash
pytest tests/
```

## Observações
- Ajuste o nome do bucket, região e role do Glue em `config/dataops_infra.yaml` e `scripts/create_glue_crawler.py`
- O pipeline pode ser expandido para uso com Prefect, Airflow, etc.
- Siga o roteiro didático para aproveitar ao máximo o projeto!

## Sobre DataOps
DataOps integra práticas de DevOps e Engenharia de Dados para automação, versionamento e governança de dados em ambientes modernos, como Data Lakes.
