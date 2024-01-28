import boto3

client = boto3.client('ses', region_name='eu-north-1')

def lambda_handler(event, context):
    print('Hello from lambda_function.py')