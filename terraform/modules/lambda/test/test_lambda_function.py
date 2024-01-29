import unittest
from unittest.mock import MagicMock, patch
from ..lambda_function import lambda_handler

class TestLambdaFunction(unittest.TestCase):

    @patch('boto3.client')
    def test_lambda_handler(self, boto3_mock):

        test_message_id = "ID"

        client_mock = MagicMock()
        client_mock.send_email.return_value = {'MessageId': test_message_id}
        boto3_mock.return_value = client_mock

        event = {}
        context = {}
        response = lambda_handler(event, context)

        self.assertEqual(response['statusCode'], 200)
        self.assertTrue('Email Sent Successfully' in response['body'])
        self.assertTrue(test_message_id in response['body'])

if __name__ == '__main__':
    unittest.main()