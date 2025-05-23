import boto3
import requests
import yaml

with open('config/config.yaml') as f:
    config = yaml.safe_load(f)

s3 = boto3.client('s3', region_name=config['aws']['region'])

def extract():
    r = requests.get(config['data_url'])
    r.raise_for_status()
    s3.put_object(Bucket=config['aws']['s3_bucket'], Key=config['aws']['raw_key'], Body=r.content)
    print('Dados crus enviados para o S3.')

if __name__ == '__main__':
    extract()
