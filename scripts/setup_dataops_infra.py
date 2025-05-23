import boto3
import yaml
import botocore

with open('config/dataops_infra.yaml') as f:
    config = yaml.safe_load(f)

region = config['aws']['region']
bucket = config['aws']['s3_bucket']
folders = config['aws']['folders']
glue_database = config['aws']['glue_database']
glue_crawler = config['aws']['glue_crawler']
glue_role_arn = config['aws']['glue_role_arn']

s3 = boto3.client('s3', region_name=region)
glue = boto3.client('glue', region_name=region)

def create_bucket():
    try:
        s3.head_bucket(Bucket=bucket)
        print(f"Bucket '{bucket}' já existe.")
    except botocore.exceptions.ClientError:
        if region == 'us-east-1':
            s3.create_bucket(Bucket=bucket)
        else:
            s3.create_bucket(
                Bucket=bucket,
                CreateBucketConfiguration={'LocationConstraint': region}
            )
        print(f"Bucket '{bucket}' criado.")

def create_folders():
    for folder in folders:
        s3.put_object(Bucket=bucket, Key=(folder if folder.endswith('/') else folder + '/'))
        print(f"Pasta '{folder}' criada no bucket '{bucket}'.")

def create_glue_database():
    try:
        glue.create_database(DatabaseInput={'Name': glue_database})
        print(f"Glue Database '{glue_database}' criado.")
    except glue.exceptions.AlreadyExistsException:
        print(f"Glue Database '{glue_database}' já existe.")

def create_glue_crawler():
    try:
        glue.create_crawler(
            Name=glue_crawler,
            Role=glue_role_arn,
            DatabaseName=glue_database,
            Targets={'S3Targets': [{'Path': f's3://{bucket}/raw/'}]},
            TablePrefix='raw_',
            SchemaChangePolicy={'UpdateBehavior': 'UPDATE_IN_DATABASE', 'DeleteBehavior': 'DEPRECATE_IN_DATABASE'}
        )
        print(f"Crawler '{glue_crawler}' criado.")
    except glue.exceptions.AlreadyExistsException:
        print(f"Crawler '{glue_crawler}' já existe.")

if __name__ == '__main__':
    create_bucket()
    create_folders()
    create_glue_database()
    create_glue_crawler()
    print('Infraestrutura DataOps criada com sucesso!')
