import unittest
import pytest
from ..sensor import process

class TestProcess(unittest.TestCase):
    def test_get_payload_json(self):
        # Test case 1: Valid input
        humidity = 50.5636784
        temperature = 25.45636457
        expected_result = '{"humidity": 50.5636784, "temperature": 25.45636457}'
        self.assertEqual(process.get_payload_json(humidity, temperature), expected_result)

    def test_get_payload_json_invalid_input(self):
        # Test case 2: Invalid input
        humidity = "high"
        temperature = 25.45636457
        with pytest.raises(ValueError):
            process.get_payload_json(humidity, temperature)

if __name__ == '__main__':
    unittest.main()