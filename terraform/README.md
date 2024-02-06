# Terraform configuration for Ventilation Indicator

This directory contains the Terraform configuration for setting up the Ventilation Indicator project on AWS.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Structure of the Terraform configuration](#structure-of-the-terraform-configuration)
- [Instructions for set-up](#instructions-for-set-up)

## Prerequisites

All prerequistes for this set-up are described in the `README.md` of the root directory of this repository.

## Structure of the Terraform configuration

### Directory

The Terraform configuration is organised as follows:

- `main.tf`: Contains the main configuration for the AWS provider and resources.
- `variables.tf`: Defines the input variables used in the configuration.
- `terraform.tfvars.example`: Serves as a template for creating a `terraform.tfvars` file, which is used to provide input values for Terraform [variables](#variables) during the deployment process.
- `versions.tf`: Contains the version information for the Terraform modules used in the project.
- `modules/`: Contains reusable modules used in the configuration. They are further described in the [section below](#modules).

### Modules

This Terraform configuration uses the following modules:
- `iot`: Sets up the AWS IoT resources.
- `lambda`: Deploys the AWS Lambda function.

### Variables

The following list provides documentation for the variables used in the Terraform configuration file `terraform.tfvars.example`.

- `thing_name`: Custom name of thing specifies a unique name for your Raspberry Pi in AWS.

- `certificate_path`: This variable should contain the file path where the certificate and private key for your Raspberry Pi are stored.  Make sure to securely manage this file and protect it from unauthorized access. 

- `connection_id`: The connection ID to AWS is used for establishing a connection between your device and AWS services.

- `latitude`: The latitude of the location specifies where the Raspberry Pi is deployed. It is used for retrieving the current weather situation from the API.

- `longitude`: The longitude of the location specifies where the Raspberry Pi is deployed. It is used for retrieving the current weather situation from the API.

- `app_id`: The API Key can be retrieved from your OpenWeatherMap account. Make sure to securely manage this API key and avoid exposing it publicly.

- `aws_access_key`: The AWS access key can be retrieved from your AWS account. Make sure to securely manage this access key and avoid exposing it publicly.

- `aws_secret_access_key`: The AWS secret access key can be retrieved from your AWS account. Make sure to securely manage this secret access key and avoid exposing it publicly.

- `recipients`: A list of email addresses that specifies the recipients who will receive notifications from the system.

- `sender`: An email address that is used for the sender for notifications from the system.

Make sure to securely manage sensitive variables such as `certificate_path`, `app_id`, `aws_access_key`, and `aws_secret_access_key`. Avoid committing these values to version control systems or sharing them publicly.

## Instructions for set-up

1. Set-up a user in AWS with the necessary privileges. Retrieve an AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY in AWS according to the [documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html).
2. Create a copy ```terraform.tfvars``` from ```terraform.tfvars.example``` and set valid values for all variables. Details on these variables are given [above](#variables).
3. Initialise terraform:
```
terraform init
```
4. Check changes in terraform:
```
terraform plan -var-file="terraform.tfvars"
```
4. Apply changes in AWS:
```
terraform apply -var-file="terraform.tfvars"
```