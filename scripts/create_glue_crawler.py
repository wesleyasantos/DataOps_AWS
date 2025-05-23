import boto3
import yaml

with open('config/config.yaml') as f:
    config = yaml.safe_load(f)

glue = boto3.client('glue', region_name=config['aws']['region'])

def create_crawler():
    glue.create_crawler(
        Name='titanic-crawler',
        Role='arn:aws:iam::SEU_ID:role/service-role/AWSGlueServiceRole',
        DatabaseName=config['aws']['athena_database'],
        Targets={'S3Targets': [{'Path': f"s3://{config['aws']['s3_bucket']}/raw/"}]},
        TablePrefix='raw_',
        SchemaChangePolicy={'UpdateBehavior': 'UPDATE_IN_DATABASE', 'DeleteBehavior': 'DEPRECATE_IN_DATABASE'}
    )
    print('Crawler criado!')

if __name__ == '__main__':
    create_crawler()
