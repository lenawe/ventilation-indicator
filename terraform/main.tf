provider "aws" {
  region = "eu-north-1"
}

resource "aws_iot_thing" "this" {
    name = var.thing_name
}