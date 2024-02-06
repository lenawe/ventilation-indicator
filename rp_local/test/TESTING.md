# Unit tests on Raspberry Pi

This document provides an overview of the tests in the `test` directory, including what each test covers, how to run them, and how to interpret the results.

## Table of contents
- [Coverage of the tests](#coverage-of-the-tests)
- [Execution of the tests](#execution-of-the-tests)
- [Interpretation of the tests](#interpretation-of-the-tests)

## Coverage of the tests

### test_read.py

The `test_read.py` file contains unit tests for the `load_parameter` and `read_data` functions in the `sensor.read` module.

1. `test_load_parameter`: This test checks whether the `load_parameter` function correctly initializes the SMBus and loads the calibration parameters for the BME280 sensor. It uses mock objects to simulate the SMBus and the `load_calibration_params` function from the `bme280` module.

2. `test_read_data`: This test checks whether the `read_data` function correctly reads the humidity and temperature data from the BME280 sensor. It uses a mock object to simulate the sensor data.

### test_process.py

The `test_process.py` file contains unit tests for the `get_payload_json` function in the `sensor.process` module.

1. `test_get_payload_json`: This test checks whether the `get_payload_json` function correctly converts humidity and temperature data into a JSON string. It uses valid input data for the test.

2. `test_get_payload_json_invalid_input`: This test checks whether the `get_payload_json` function correctly raises a `ValueError` when given invalid input data. It uses an invalid humidity value for the test.

### test_publish.py

The `test_publish.py` file contains unit tests for the `configure_mqtt_client` and `publish_message` functions in the `mqtt.publish` module.

1. `test_configure_mqtt_client`: This test checks whether the `configure_mqtt_client` function correctly configures and connects an AWS IoT MQTT client. It uses a mock object to simulate the AWS IoT MQTT client.

2. `test_publish_message`: This test checks whether the `publish_message` function correctly publishes a message to a topic on the MQTT client. It uses a mock object to simulate the MQTT client.

## Execution of the tests

To run the tests, use the command prompt to navigate to the `test` directory on your Raspberry Pi and use the following command:
```
python -m unittest discover
```

## Interpretation of the tests
The output of the test run indicates whether each test passed or failed. If a test passes, an OK and the number of passed tests appears. If a test fails, FAIL appears, and additional information about the failure is printed at the end of the output.