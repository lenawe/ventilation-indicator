def configure_mqtt_client(aws_endpoint, client_id, topic):
    # AWS IoT Core Configuration
    endpoint = aws_endpoint
    root_ca_path = "certs/Amazon-root-CA-1.pem"
    cert_path = "certs/device.pem.crt"
    key_path = "certs/private.pem.key" 
    client_id = client_id
    topic = topic
