# Unit tests for Lambda function

This `TESTING.md` provides an overview of the tests in the `test_lambda_function.py` file, including what each test covers, how to run them, and how to interpret the results.

## Table of contents
- [Coverage of the tests](#coverage-of-the-tests)
- [Execution of the tests](#execution-of-the-tests)
- [Interpretation of the test results](#interpretation-of-the-test-results)

## Coverage of the tests

The `test_lambda_function.py` file contains unit tests for the `send_notification`, `get_outdoor_measurements`, `get_absolute_humidity`, `get_absolute_humidity_difference`, and `get_new_relative_humidity` functions in the `lambda_function` module.

1. `test_send_notification`: This test verifies the correct sending of an email notification using a mock object to simulate the boto3 client.

2. `test_get_outdoor_measurements`: This test verifies the correct retrieval of outdoor measurements using a mock object to simulate the urllib3 PoolManager.

3. `test_get_absolute_humidity`: This test verifies the correct calculation of absolute humidity given temperature and relative humidity.

4. `test_humidity_difference`: This test verifies the correct calculation of the difference between two absolute humidity values.

5. `test_invalid_humidity`: This test verifies that an error is raised when an invalid absolute humidity value is provided.

6. `test_get_new_relative_humidity`: This test verifies the correct calculation of relative humidity given temperature and absolute humidity.

7. `test_get_new_relative_humidity_invalid`: This test verifies that an error is raised when an invalid temperature value is provided.

## Execution of the tests

To run the tests, use the command prompt of your PC to navigate to the `terraform/modules/lambda` directory and install the necessary package by using the following command:
```
pip install pytest-socket
```
Then, run the unit tests:
```
pytest -v --disable-socket -s test/
```

## Interpretation of the test results
The output of the test run indicates whether each test passed or failed. If a test passes, a PASSED appears next to the name of the test. If a test fails, FAIL appears next to the name, and additional information about the failure is printed at the end of the output.