import json

def get_payload_json(humidity, temperature):
    try:
        payload = {
            "humidity": humidity,
            "temperature": temperature
        }
        return json.dumps(payload)
    except Exception as e:
        print(f"Error occurred while processing payload: {e}")
        return None
