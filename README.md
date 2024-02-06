# Recommender system for ventilation of interior rooms
This project aims to provide a solution that monitors the humidity status in a given environment. In case a certain threshold is exceeded, it will send a mail notification to a list of recipients.

## Table of contents
- [Hardware requirements](#hardware-requirements)
- [Installation](#installation)
- [Run unit tests](#run-unit-tests)
- [References](#references)

## Hardware requirements
### Required components
+ [Raspberry Pi 4 Model B](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/)
+ Sensor [BME280](https://www.bosch-sensortec.com/products/environmental-sensors/humidity-sensors-bme280/)
+ Jumper wires

### Instructions for set-up
1. For ensuring a stable connection of your sensor, solder a pin header first.
2. Connect the sensor to the Raspberry Pi using the jumper wires following the following image:
<p align="center">
  <img src='https://pypi-camo.freetls.fastly.net/e1c7e61175cad5b70af740e8305ea3b1e50b1104/68747470733a2f2f692e696d6775722e636f6d2f38693373536c432e706e67' width='300' alt="Connection of BME280 sensor to Raspberry Pi" style="transform:rotate(90deg);">
</p>
3. In case you set-up your Raspberry Pi the very first time, there are numerous guides to be followed. One example is given here: https://www.tomshardware.com/reviews/raspberry-pi-headless-setup-how-to,6028.html

## Software requirements
### Required software
+ PuTTY
+ [Terraform](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli)
+ Text editor recommended, e.g. [Visual Studio Code](https://code.visualstudio.com/)

### Instructions for set-up
+ Create [AWS](https://aws.amazon.com/) account
+ Create account on [OpenWeather](https://openweathermap.org/api) to access their API

## Structure of the project
This repository is split into two folders. The code that belongs to the Raspberry Pi and is required to run the local program on it is contained in the folder `rp_local`. The files that will be used to deploy the infrastructure on AWS belong to the folder `terraform`.

## Set-up the project in local environment
1. Clone the repository:
```
git clone https://github.com/lenawe/ventilation-indicator.git
```
2. Create AWS IoT client certificates acording to the official documentation [AWS](https://docs.aws.amazon.com/iot/latest/developerguide/device-certs-create.html). Store them in the folder ```rp_local/certs```.
3. From the root directory, navigate to terraform folder:
```
cd terraform
```
4. The instructions on how to deploy the infrastructure to AWS are listed in the `README.md` in the `terraform` folder. The steps listed [there](terraform/README.md) should be followed before proceeding.
5. Navigate back to the root folder.
6. Create a copy ```rp_local/variables.yml``` from ```rp_local/variables.yml.example``` and set valid values for all [variables](rp_local/README.md/#variables).
7. Copy folder ```rp_local``` as ```ventilation-indicator``` to your Raspberry Pi:
```
cd..
scp -r rp_local user@raspberrypi:./ventilation-indicator
```
8. In order to run the program on the Raspberry Pi, follow the [instructions](rp_local/README.md) described in the `README.md` of the `rp_local` folder.

## Testing
The functionality of the code in this repository is ensured via unit tests. An extensive documentation about the [unit tests used in the Lambda function](terraform/modules/lambda/test/TESTING.md) and for those [used for the code on the Raspberry Pi](rp_local/test/TESTING.md) is provided in the respective directory.

## References
https://projects.raspberrypi.org/en/projects/build-your-own-weather-station/2 </br>
https://www.terraform-best-practices.com/examples</br>
https://docs.aws.amazon.com/iot/</br>
https://openweathermap.org/api