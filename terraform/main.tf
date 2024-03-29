provider "aws" {
  region = "eu-north-1"
  access_key = var.aws_access_key
  secret_key = var.aws_secret_access_key
}

resource "aws_iot_thing" "this" {
    name = "thing_${var.thing_name}"
}

module "iot" {
    source = "./modules/iot"

    thing_name = var.thing_name
    certificate_path = var.certificate_path
}

module "lambda" {
    source = "./modules/lambda"

    thing_name = var.thing_name
    connection_id = var.connection_id
    latitude = var.latitude
    longitude = var.longitude
    app_id = var.app_id
    recipients = var.recipients
    sender = var.sender
}