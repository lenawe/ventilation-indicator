# Recommender system for ventilation of interior rooms
This project aims to provide a solution that monitors the humidity status in a given environment. In case a certain threshold is exceeded, it will send a mail notification to a list of recipients.

## Hardware requirements
### Required components
+ [Raspberry Pi 4 Model B](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/)
+ Sensor [BME280](https://www.bosch-sensortec.com/products/environmental-sensors/humidity-sensors-bme280/)
+ Jumper wires

### Set-up
1. For ensuring a stable connection of your sensor, solder a pin header first.
2. Connect the sensor to the Raspberry Pi using the jumper wires following the following image:
<p align="center">
  <img src='https://pypi-camo.freetls.fastly.net/e1c7e61175cad5b70af740e8305ea3b1e50b1104/68747470733a2f2f692e696d6775722e636f6d2f38693373536c432e706e67' width='300' alt="Connection of BME280 sensor to Raspberry Pi" style="transform:rotate(90deg);">
</p>
3. In case you set-up your Raspberry Pi the very first time, there are numerous guides to be followed. One example is given here: [How to Set Up a Headless Raspberry Pi, Without Ever Attaching a Monitor](https://www.tomshardware.com/reviews/raspberry-pi-headless-setup-how-to,6028.html)

## Installation
### Software required to be installed on your laptop
+ PuTTY
+ [Terraform](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli)
+ Text editor recommended, e.g. [Visual Studio Code](https://code.visualstudio.com/)

### Local set-up
1. If not available, set-up [AWS](https://aws.amazon.com/) account.
2. Clone the repository:
```
git clone https://github.com/lenawe/ventilation-indicator.git
```
3. Create AWS IoT client certificates acording to the official documentation [AWS](https://docs.aws.amazon.com/iot/latest/developerguide/device-certs-create.html). Store them in the folder ```rp_local/certs```.
4. Create a copy ```variables.yml``` from ```variables.yml.example``` and set valid values for all variables.
5. Preferably in git bash, navigate to terraform folder:
```
cd terraform
```
6. Set-up a user with the necessary privileges. Retrieve an AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY in AWS according to the [documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html).
7. Create a copy ```terraform.tfvars``` from ```terraform.tfvars.example``` and set valid values for all variables.
8. Initialise terraform:
```
terraform init
```
9. Check changes in terraform and apply them in AWS:
```
terraform plan -var-file="terraform.tfvars"
terraform apply -var-file="terraform.tfvars"
```
10. Navigate to root folder and copy folder ```rp_local``` to your Raspberry Pi:
```
cd..
scp -r rp_local user@raspberrypi:./ventilation-indicator
```
11. On the Raspberry Pi, create a new Python environment, install the required packages, and start the main file.
```
python3 -m venv awsenv
source awsenv/bin/activate
cd ventilation-indicator
pip install -r requirements.txt
python3 main.py
```

## Run local unit tests
### Run unit tests on Raspberry Pi
1. Navigate to ```cd ventilation-indicator/test``` folder.
2. Run unit tests:
```
python -m unittest discover
```

### Run local unit tests for Lambda function
1. Navigate to ```cd ventilation-indicator/terraform/modules/lambda``` folder.
2. Execute pip install:
```
pip install pytest-socket
```
3. Run unit tests:
```
pytest -v --disable-socket -s test/
```

## References
https://projects.raspberrypi.org/en/projects/build-your-own-weather-station/2 </br>
https://www.terraform-best-practices.com/examples</br>
https://docs.aws.amazon.com/iot/