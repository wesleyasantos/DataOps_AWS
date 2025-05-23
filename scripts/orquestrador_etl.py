import subprocess
import sys

def run_step(description, command):
    print(f'\n===== {description} =====')
    try:
        subprocess.run([sys.executable] + command, check=True)
        print(f'{description} concluído com sucesso.')
    except subprocess.CalledProcessError as e:
        print(f'Erro ao executar {description}:', e)
        sys.exit(1)

if __name__ == '__main__':
    run_step('Extração dos dados', ['etl/extract.py'])
    run_step('Transformação dos dados', ['etl/transform.py'])
    run_step('Carga final dos dados', ['etl/load.py'])
    run_step('Checagem de qualidade dos dados', ['analytics/data_quality.py'])
    run_step('Consulta analítica no Athena', ['analytics/query_athena.py'])
    print('\nPipeline DataOps executado com sucesso!')
