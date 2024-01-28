provider "aws" {
  region = "eu-north-1"
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
}