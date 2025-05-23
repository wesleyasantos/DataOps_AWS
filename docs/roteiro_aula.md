# Cronograma - DataOps AWS Titanic

## Atividade 1: Introdução ao DataOps e AWS
- Conceitos de DataOps, Datalake, ETL, versionamento, YAML
- Apresentação da arquitetura do projeto
- Configuração do AWS CLI, permissões, criação de usuário e role

## Atividade 2: Setup da Infraestrutura DataOps
- Explicação do arquivo `config/dataops_infra.yaml`
- Ajuste do bucket, pastas, Glue Database, Crawler e ARN da role
- Execução do script de setup:
  ```bash
  python scripts/setup_dataops_infra.py
  ```
- Verificação dos recursos criados no console AWS (S3, Glue)

## Atividade 3: Execução do Pipeline ETL Orquestrado
- Explicação do orquestrador `scripts/orquestrador_etl.py`
- Execução do pipeline completo:
  ```bash
  python scripts/orquestrador_etl.py
  ```
- Observação dos logs e resultados de cada etapa

## Atividade 4: Catálogo e Consulta de Dados
- Execução do Glue Crawler pelo console AWS para catalogar os dados após a extração/transformação
- Criação da tabela Athena executando o SQL em `scripts/create_athena_table.sql` no console Athena
- Execução da consulta analítica via Athena e análise dos resultados

## Atividade 5: Testes e Qualidade de Dados
- Execução dos testes automatizados:
  ```bash
  pytest tests/
  ```
- Discussão sobre checagem de qualidade dos dados (`analytics/data_quality.py`)

## Atividade 6: Expansão, Automação e Boas Práticas
- Discussão sobre possíveis expansões: Prefect, Airflow, triggers, monitoramento
- Boas práticas de versionamento, documentação e segurança
- Apresentação dos aprendizados e dúvidas

---

**Observações:**
- O fluxo do projeto foi automatizado para facilitar o entendimento do ciclo completo de DataOps na AWS.
- O orquestrador executa todas as etapas do pipeline ETL e análise de forma sequencial.
- O setup da infraestrutura garante que todos os recursos necessários estejam prontos antes do processamento dos dados.
