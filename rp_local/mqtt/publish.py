from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient

def configure_mqtt_client(aws_endpoint, client_id, topic):
    '''
    Configure MQTT client for AWS IoT Core.
    @param aws_endpoint: AWS IoT Core endpoint
    @param client_id: MQTT client ID
    @param topic: MQTT topic
    @return: MQTT client
    '''
    try:
        # AWS IoT Core Configuration
        endpoint = aws_endpoint
        root_ca_path = "certs/Amazon-root-CA-1.pem"
        cert_path = "certs/device.pem.crt"
        key_path = "certs/private.pem.key" 
        client_id = client_id
        topic = topic

        # Initialise AWS IoT MQTT Client
        mqtt_client = AWSIoTMQTTClient(client_id)
        mqtt_client.configureEndpoint(endpoint, 443)
        mqtt_client.configureCredentials(root_ca_path, key_path, cert_path)

        # Configure connection settings
        mqtt_client.configureOfflinePublishQueueing(-1)
        mqtt_client.configureDrainingFrequency(2)
        mqtt_client.configureConnectDisconnectTimeout(10)
        mqtt_client.configureMQTTOperationTimeout(5)

        # Connect to AWS IoT Core
        mqtt_client.connect()

        return mqtt_client
    except Exception as e:
        print("Error configuring MQTT client:", str(e))
        return None

def publish_message(mqtt_client, topic, json_message):
    mqtt_client.publish(topic, json_message, 1)