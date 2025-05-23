import pandas as pd
import boto3
import yaml
from io import BytesIO

with open('config/config.yaml') as f:
    config = yaml.safe_load(f)

s3 = boto3.client('s3', region_name=config['aws']['region'])

def check_quality():
    obj = s3.get_object(Bucket=config['aws']['s3_bucket'], Key=config['aws']['processed_key'])
    df = pd.read_csv(BytesIO(obj['Body'].read()))
    print('Nulos por coluna:')
    print(df.isnull().sum())
    print('Tipos de dados:')
    print(df.dtypes)
    print('Estatísticas:')
    print(df.describe())

if __name__ == '__main__':
    check_quality()
