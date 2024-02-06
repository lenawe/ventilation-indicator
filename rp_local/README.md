# Raspberry Pi configuration for Ventilation Indicator

This directory contains the configuration for setting up the Ventilation Indicator project on the Raspberry Pi.

## Table of contents
- [Prerequisites](#prerequisites)
- [Structure of the Terraform configuration](#structure-of-the-terraform-configuration)
- [Instructions for set-up](#instructions-for-set-up)

## Prerequisites

All prerequistes for this set-up are described in the `README.md` of the root directory of this repository.

## Structure of the Raspberry Pi configuration

### Directory

The Raspberry Pi project is organised as follows:

- `main.py`: Contains the main Python code for the project.
- `requirements.txt`: Lists the dependencies (package names + version numbers) required by the project.
- `variables.yml.example`: Serves as a template for creating a `variables.yml` file, which is used to provide input values for Python [variables](#variables) during the runtime.
- `mqtt/`: Contains all Python files that are related to the MQTT client.
- `sensor/`: Contains all Python files that are related to the sensor operation.
- `test/`: Contains test related to files in `mqtt/` and `sensor/` directory.

### Variables

The following list provides documentation for the variables used in the Raspberry Pi configuration file `variables.yml.example`.

- `aws_endpoint`: The AWS IoT endpoint that the Raspberry Pi will connect to. It is used to establish a connection with the AWS IoT service.

- `port`: The port number that will be used for the communication.

- `address`: The address of the sensor connected to the Raspberry Pi.

## Instructions for set-up

1. On the Raspberry Pi, create a new Python environment.
```
python3 -m venv awsenv
source awsenv/bin/activate
```

2. Install the required packages.
```
cd ventilation-indicator
pip install -r requirements.txt
```

3. Start the main file.
```
python3 main.py
```