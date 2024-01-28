from rp_local.sensor.read import load_parameter, read_data
from rp_local.sensor.process import get_payload_json
from rp_local.mqtt.publish import configure_mqtt_client

if __name__ == '__main__':

    aws_endpoint = "id-ats.iot.eu-north-1.amazonaws.com"
    client_id = "raspberrypi"
    topic = "thing/raspberrypi"
    mqtt_client = configure_mqtt_client(aws_endpoint, client_id, topic)

    port = 1
    address = 0x76

    bus = load_parameter(port, address)
    humidity, temperature = read_data(bus, address)

    json_payload = get_payload_json(humidity, temperature)
    
    print(json_payload)