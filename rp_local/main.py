import time

from sensor.read import load_parameter, read_data
from sensor.process import get_payload_json
from mqtt.publish import configure_mqtt_client, publish_message
import yaml

if __name__ == '__main__':
    '''
    Main function to read data from the sensor and publish it to the AWS IoT Core.
    '''

    # Load the variables from the variables.yml file
    with open('variables.yml', 'r') as file:
        variables = yaml.safe_load(file)

    aws_endpoint = variables['aws_endpoint']
    client_id = "raspberrypi"
    topic = "thing/" + client_id

    # Configure the MQTT client
    mqtt_client = configure_mqtt_client(aws_endpoint, client_id, topic)

    port = variables['port']
    address = variables['address']

    # Load the calibration parameters from the sensor
    bus = load_parameter(port, address)

    try:
        while True:
            # Read the data from the sensor and get the payload in JSON format
            humidity, temperature = read_data(bus, address)
            json_payload = get_payload_json(humidity, temperature)

            # Print the data to the console
            print("Humidity: " + str(humidity) + ", Temperature: " + str(temperature))

            # Publish the data to the AWS IoT Core
            publish_message(mqtt_client, "thing/raspberrypi", json_payload)

            # Wait for 10 minutes before reading the data again
            time.sleep(600)
    
    except KeyboardInterrupt:
        # Terminate the script if the user presses Ctrl+C
        print("Script terminated by user.")
        mqtt_client.disconnect()

if __name__ == '__main__':
    main()