import json

def get_payload_json(humidity, temperature):
    '''
    This function takes in the humidity and temperature values and returns a JSON payload.
    @param humidity: The humidity value.
    @param temperature: The temperature value.
    @return: A JSON payload.
    '''
    try:
        humidity = float(humidity)
        temperature = float(temperature)

        payload = {
            "humidity": humidity,
            "temperature": temperature
        }   
        return json.dumps(payload)
            
    except ValueError as ve:
        raise ValueError("Humidity and temperature must be numbers.")