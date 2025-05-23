import boto3
import yaml
from io import BytesIO

with open('config/config.yaml') as f:
    config = yaml.safe_load(f)

s3 = boto3.client('s3', region_name=config['aws']['region'])

def load():
    obj = s3.get_object(Bucket=config['aws']['s3_bucket'], Key=config['aws']['processed_key'])
    s3.put_object(Bucket=config['aws']['s3_bucket'], Key='final/titanic_final.csv', Body=obj['Body'].read())
    print('Dados processados copiados para final/titanic_final.csv no S3.')

if __name__ == '__main__':
    load()
