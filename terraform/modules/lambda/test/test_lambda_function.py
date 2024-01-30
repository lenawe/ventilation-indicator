import unittest
from unittest.mock import MagicMock, patch
from ..lambda_function import lambda_handler, send_notification, get_outdoor_measurements

class TestLambdaFunction(unittest.TestCase):

    @patch('boto3.client')
    def test_send_notification(self, boto3_mock):

        # Test data
        test_message_id = "ID"
        message_text = "This is a mail for testing.",
        subject = "Please open the windows!"
        recipients = ['test@gmail.com'] 
        sender = 'test@iu-study.org'

        # Mock mail response
        client_mock = MagicMock()
        client_mock.send_email.return_value = {'MessageId': test_message_id}
        boto3_mock.return_value = client_mock

        # Call function
        response = send_notification(message_text, subject, recipients, sender)

        # Assertion
        self.assertEqual(response['statusCode'], 200)
        self.assertTrue('Email Sent Successfully' in response['body'])
        self.assertTrue(test_message_id in response['body'])

    @patch('urllib3.PoolManager')
    def test_get_outdoor_measurements(self, pool_manager_mock):
        # Test data
        latitude = "12.345"
        longitude = "67.890"
        app_id = "test_app_id"
        api_response_data = '''
        {
            "current": {
                "humidity": 50,
                "temp": 25
            }
        }
        '''

        # Mock HTTP response
        http_response_mock = MagicMock()
        http_response_mock.data.decode.return_value = api_response_data
        pool_manager_mock.return_value.request.return_value = http_response_mock

        # Call function
        result = get_outdoor_measurements(latitude, longitude, app_id)

        # Assertion
        self.assertEqual(result, (25, 50))

if __name__ == '__main__':
    unittest.main()