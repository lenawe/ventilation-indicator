# Recommender system for ventilation of interior rooms
This project aims to provide a solution that monitors the humidity status in a given environment. In case a certain threshold is exceeded, it will send a mail notification to a list of recipients.

## Hardware requirements
### Required components
+ [Raspberry Pi 4 Model B](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/)
+ Sensor [BME280](https://www.bosch-sensortec.com/products/environmental-sensors/humidity-sensors-bme280/)
+ Jumper wires

### Set-up
1. For ensuring a stable connection of your sensor, solder a pin header first.
2. Connect sensor to the Raspberry Pi using the jumper wires following the following image: 
![Connection of BME280 sensor to Raspberry Pi](https://projects-static.raspberrypi.org/projects/build-your-own-weather-station/280233af49c74aed6e178ee9f89fb8a713379229/en/images/bme280_bb.png)
3. In case you set-up your raspberry pi the very first time, there are numerous guides to be followed. One example is given here: [How to Set Up a Headless Raspberry Pi, Without Ever Attaching a Monitor](https://www.tomshardware.com/reviews/raspberry-pi-headless-setup-how-to,6028.html)

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
3. Preferably in git bash, navigate to terraform folder:
```
cd terraform
```
4. Initialise terraform:
```
terraform init
```
5. Retrieve an AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY in AWS according to the [documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html). Enter them in the console:
```
export AWS_ACCESS_KEY_ID=kEyId
export AWS_SECRET_ACCESS_KEY=aCeSsKeY
```
6. Check changes in terraform and apply them in AWS:
```
terraform plan
terraform apply
```
7. Copy folder to raspberry pi:
```
scp -r rp_local user@raspberrypi:./ventilation-indicator
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
https://projects.raspberrypi.org/en/projects/build-your-own-weather-station/2
https://www.terraform-best-practices.com/examples
https://docs.aws.amazon.com/iot/