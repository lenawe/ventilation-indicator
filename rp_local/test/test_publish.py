import unittest
from rp_local.mqtt.publish import configure_mqtt_client, publish_message
from unittest.mock import MagicMock, patch

class TestPublish(unittest.TestCase):
    @patch('rp_local.mqtt.publish.AWSIoTMQTTClient')
    def test_configure_mqtt_client(self, mock_client):

        aws_endpoint = 'aws_endpoint'
        client_id = 'client_id'
        topic = 'topic'

        # Mock object
        mock_instance = mock_client.return_value
        mock_instance.connect.return_value = True

        # Call function
        result = configure_mqtt_client(aws_endpoint, client_id, topic)
        
        # Assert
        mock_client.assert_called_once_with(client_id)
        mock_instance.configureEndpoint.assert_called_once_with(aws_endpoint, 443)
        mock_instance.configureCredentials.assert_called_once_with("certs/Amazon-root-CA-1.pem", "certs/private.pem.key", "certs/device.pem.crt")
        mock_instance.configureOfflinePublishQueueing.assert_called_once_with(-1)
        mock_instance.configureDrainingFrequency.assert_called_once_with(2)
        mock_instance.configureConnectDisconnectTimeout.assert_called_once_with(10)
        mock_instance.configureMQTTOperationTimeout.assert_called_once_with(5)
        mock_instance.connect.assert_called_once()

        self.assertEqual(result, mock_instance)
