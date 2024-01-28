import boto3

client = boto3.client('ses', region_name='eu-north-1')

def lambda_handler(event, context):
    message_text = "This is a mail for testing.",
