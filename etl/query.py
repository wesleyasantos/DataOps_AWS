import boto3
import yaml
import time

with open('config/config.yaml') as f:
    config = yaml.safe_load(f)

athena = boto3.client('athena', region_name=config['aws']['region'])

def query():
    query_str = 'SELECT Sex, AVG(Age) as avg_age FROM "{}"."{}" GROUP BY Sex'.format(
        config['aws']['athena_database'], config['aws']['athena_table']
    )
    response = athena.start_query_execution(
        QueryString=query_str,
        QueryExecutionContext={'Database': config['aws']['athena_database']},
        ResultConfiguration={'OutputLocation': f"s3://{config['aws']['s3_bucket']}/{config['aws']['athena_output']}"}
    )
    query_execution_id = response['QueryExecutionId']
    while True:
        result = athena.get_query_execution(QueryExecutionId=query_execution_id)
        state = result['QueryExecution']['Status']['State']
        if state in ['SUCCEEDED', 'FAILED', 'CANCELLED']:
            break
        time.sleep(2)
    print(f"Consulta finalizada com estado: {state}")

if __name__ == '__main__':
    query()
