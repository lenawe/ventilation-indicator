import boto3
import json
import urllib3

def lambda_handler(event, context):
    '''
    This function sends an email to the specified address.
    @param event: The event passed to the function.
    @param context: The context passed to the function.
    '''

    client = boto3.client('ses', region_name='eu-north-1')

    message_text = "This is a mail for testing.",
    subject = "Please open the windows!"
    recipients = [] # enter destination address
    sender = 'test@mail.com' # enter source address
    
    return send_notification(message_text, subject, recipients, sender)

def send_notification(message_text, subject, recipients, sender):
    '''
    This function sends an email to the specified address.
    @param message_text: The text of the message.
    @param subject: The subject of the message.
    @param recipients: The recipients of the message.
    @param sender: The sender of the message.
    @return: The status code and a message.
    '''
    client = boto3.client('ses', region_name='eu-north-1')

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

def get_outdoor_measurements(latitude, longitude, app_id):
    '''
    This function returns the outdoor temperature and humidity.
    @param latitude: The latitude of the location.
    @param longitude: The longitude of the location.
    @param app_id: The app id for the openweathermap api.
    @return: The outdoor temperature and humidity.
    '''
    
    http = urllib3.PoolManager()
    api = 'https://api.openweathermap.org/data/3.0/onecall?lat=' + latitude + '&lon=' + longitude + '&appid=' + app_id + '&units=metric'
    api_response = http.request('GET', api)
    
    data = api_response.data.decode('utf-8')

    data = json.loads(data)
    data = data["current"]

    out_humidity = data["humidity"]
    out_temperature = data["temp"]
    
    return out_temperature, out_humidity 
    