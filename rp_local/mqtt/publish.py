from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient

def configure_mqtt_client(aws_endpoint, client_id, topic):
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
