import boto3
import json

client = boto3.client('ses', region_name='eu-north-1')

def lambda_handler(event, context):
    message_text = "This is a mail for testing.",
    subject = "Please open the windows!"
    recipients = [] # enter destination address
    sender = 'source@mail.com' # enter source address
    
    response = client.send_email(
        Destination={
            'ToAddresses': recipients
        },
            
        Message={
            'Body': {
                'Text': {
                    'Charset': 'UTF-8',
                    'Data': ''.join(message_text)
                }
            },
            'Subject': {
                'Charset': 'UTF-8',
                'Data': subject,
            },
        },
        Source = sender
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps("Email Sent Successfully. MessageId is: " + response['MessageId'])
    }