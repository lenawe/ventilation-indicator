import time

from sensor.read import load_parameter, read_data
from sensor.process import get_payload_json
from mqtt.publish import configure_mqtt_client, publish_message

if __name__ == '__main__':

    aws_endpoint = "id-ats.iot.eu-north-1.amazonaws.com"
    client_id = "raspberrypi"
    topic = "thing/raspberrypi"
    mqtt_client = configure_mqtt_client(aws_endpoint, client_id, topic)

    port = 1
    address = 0x76

    bus = load_parameter(port, address)

    try:
        while True:
            humidity, temperature = read_data(bus, address)
            json_payload = get_payload_json(humidity, temperature)
            print("Humidity: " + str(humidity) + ", Temperature: " + str(temperature))
            publish_message(mqtt_client, "thing/raspberrypi", json_payload)
            time.sleep(5)
    
    except KeyboardInterrupt:
        print("Script terminated by user.")
        mqtt_client.disconnect()