provider "aws" {
  region = "eu-north-1"
}

resource "aws_iot_thing" "this" {
    name = "thing_${var.thing_name}"
}