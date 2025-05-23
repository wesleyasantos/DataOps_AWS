import boto3
import pandas as pd
import yaml
from io import BytesIO

with open('config/config.yaml') as f:
    config = yaml.safe_load(f)

s3 = boto3.client('s3', region_name=config['aws']['region'])

def transform():
    obj = s3.get_object(Bucket=config['aws']['s3_bucket'], Key=config['aws']['raw_key'])
    df = pd.read_csv(BytesIO(obj['Body'].read()))
    df = df.drop(['PassengerId', 'Name', 'Ticket', 'Cabin'], axis=1)
    df = df.fillna({'Age': df['Age'].median(), 'Embarked': df['Embarked'].mode()[0]})
    out_buffer = BytesIO()
    df.to_csv(out_buffer, index=False)
    s3.put_object(Bucket=config['aws']['s3_bucket'], Key=config['aws']['processed_key'], Body=out_buffer.getvalue())
    print('Dados processados enviados para o S3.')

if __name__ == '__main__':
    transform()
