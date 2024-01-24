import json

def get_payload_json(humidity, temperature):
    '''
    This function takes in the humidity and temperature values and returns a JSON payload.
    @param humidity: The humidity value.
    @param temperature: The temperature value.
    @return: A JSON payload.
    '''
    try:
        payload = {
            "humidity": humidity,
            "temperature": temperature
        }
        return json.dumps(payload)
    except Exception as e:
        print(f"Error occurred while processing payload: {e}")
        return None