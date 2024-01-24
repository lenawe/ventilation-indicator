import json

def get_payload_json(humidity, temperature):
    payload = {
        "humidity": humidity,
        "temperature": temperature
    }
    return json.dumps(payload)