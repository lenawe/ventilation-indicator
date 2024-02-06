import unittest
from unittest.mock import MagicMock, patch
from rp_local.sensor.read import load_parameter, read_data

class TestRead(unittest.TestCase):

    @patch('rp_local.sensor.read.smbus2.SMBus')
    @patch('rp_local.sensor.read.bme280.load_calibration_params')
    def test_load_parameter(self, mock_load_calibration_params, mock_SMBus):

        # Mock object
        mock_bus = MagicMock()
        mock_SMBus.return_value = mock_bus

        port = 1
        address = 0x76

        # Call function
        result = load_parameter(port, address)

        # Assert
        self.assertEqual(result, mock_bus)
        mock_SMBus.assert_called_once_with(port)
        mock_load_calibration_params.assert_called_once_with(mock_bus, address)

    def test_read_data(self):

        # Mock object
        mock_sensor_data = MagicMock()
        mock_sensor_data.humidity = 50.0
        mock_sensor_data.temperature = 25.0

        mock_bus = MagicMock()
        address = 0x76

        # Call function
        with patch('rp_local.sensor.read.bme280.sample', return_value=mock_sensor_data):
            humidity, temperature = read_data(mock_bus, address)

        # Assert
        self.assertEqual(humidity, 50.0)
        self.assertEqual(temperature, 25.0)