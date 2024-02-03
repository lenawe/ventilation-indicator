import boto3
import json
import urllib3
import math
import os

def lambda_handler(event, context):
    '''
    This function sends an email to the specified address.
    @param event: The event passed to the function.
    @param context: The context passed to the function.
    '''
    latitude = os.environ['latitude']
    longitude = os.environ['longitude']
    app_id = os.environ['app_id']

    # INDOOR MEASUREMENTS
    in_temperature, in_humidity_rel = round(event['temperature'], 2), round(event['humidity'], 2)
    in_humidity_abs = get_absolute_humidity(in_temperature, in_humidity_rel)

    # OUTDOOR MEASUREMENTS
    out_temperature, out_humidity_rel = get_outdoor_measurements(latitude, longitude, app_id)
    out_humidity_abs = get_absolute_humidity(out_temperature, out_humidity_rel)

    # SUGGESTION
    humidity_abs_difference = get_absolute_humidity_difference(in_humidity_abs, out_humidity_abs)
    new_in_humidity_rel = get_new_relative_humidity(in_temperature, out_humidity_abs)

    send_mail = False
    if humidity_abs_difference > 0:
        send_mail = True

    message_text =  '''
INDOOR MEASUREMENTS:
Temperature: ''' + str(in_temperature) + ''' degrees celsius
Relative humidity: ''' + str(in_humidity_rel) + ''' percent
Absolute humidity: ''' + str(in_humidity_abs) + ''' g/m3

OUTDOOR MEASUREMENTS:
Temperature: ''' + str(out_temperature) + ''' degrees celsius
Humidity: ''' + str(out_humidity_rel) + ''' percent
Absolute humidity: ''' + str(out_humidity_abs) + ''' g/m3

SUGGESTION:
The absolute humidity inside is ''' + str(humidity_abs_difference) + ''' g/m3 higher than outside. Please open the windows!
The new relative humidity inside at a temperature of ''' + str(in_temperature) + ''' degrees celsius would be ''' + str(new_in_humidity_rel) + ''' percent.
                    '''
    subject = "Please open the windows!"
    recipients = json.loads(os.environ['recipients'])
    sender = os.environ['sender']
    
    if send_mail: 
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
    
def get_absolute_humidity(temperature, humidity_rel):
    '''
    This function returns the absolute humidity.
    @param temperature: The temperature.
    @param humidity_rel: The relative humidity.
    @return: The absolute humidity.
    '''
    try:
        temperature = float(temperature)
        humidity_rel = float(humidity_rel)

        e_exp = math.exp((17.67 * temperature) / (temperature + 243.5))
        humidity_abs = (6.112 * e_exp * humidity_rel * 2.1674) / (273.15 + temperature)

        return round(humidity_abs, 3)

    except ValueError:
        raise ValueError("Temperature and humidity must be numbers.")

def get_absolute_humidity_difference (in_humidity_abs, out_humidity_abs):
    '''
    This function returns the absolute humidity difference.
    @param in_humidity_abs: The absolute humidity inside.
    @param out_humidity_abs: The absolute humidity outside.
    @return: The absolute humidity difference.
    '''
    try:
        in_humidity_abs = float(in_humidity_abs)
        out_humidity_abs = float(out_humidity_abs)

        humidity_abs_difference = in_humidity_abs - out_humidity_abs

        return round(humidity_abs_difference, 3)

    except ValueError:
        raise ValueError("Humidity must be numbers.")

def get_new_relative_humidity(temperature, humidity_abs):
    '''
    This function returns the relative humidity.
    @param temperature: The temperature.
    @param humidity_abs: The absolute humidity.
    @return: The relative humidity.
    '''
    try:
        temperature = float(temperature)
        humidity_abs = float(humidity_abs)

        e_exp = math.exp((17.67 * temperature) / (temperature + 243.5))
        humidity_rel = (humidity_abs * (273.15 + temperature)) / (6.112 * e_exp * 2.1674)

        return round(humidity_rel, 3)

    except ValueError:
        raise ValueError("Temperature and humidity must be numbers.")