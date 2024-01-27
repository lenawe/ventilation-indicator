provider "aws" {
  region = "eu-north-1"
}

resource "aws_iot_thing" "this" {
    name = "thing_${var.thing_name}"
}

resource "aws_iot_policy" "this" {
    name = "policy_${var.thing_name}"
    policy = jsonencode({
      "Version": "2012-10-17",
      "Statement": [
          {
              "Effect": "Allow",
              "Action": "iot:Connect",
              "Resource": "*"
          },
          {
              "Effect": "Allow",
              "Action": "iot:Receive",
              "Resource": "*"
          },
          {
              "Effect": "Allow",
              "Action": "iot:Publish",
              "Resource": "*"
          },
          {
              "Effect": "Allow",
              "Action": "iot:Subscribe",
              "Resource": "*"
          },
          {
              "Effect": "Allow",
              "Action": "iot:PublishRetain",
              "Resource": "*"
          }
      ]
    })
}

resource "aws_iot_certificate" "this" {
    certificate_pem = file(var.certificate_path)
    active = true
}

resource "aws_iot_thing_principal_attachment" "this" {
    thing = aws_iot_thing.this.name
    principal = aws_iot_certificate.this.arn
}

resource "aws_iot_policy_attachment" "this" {
    policy = aws_iot_policy.this.name
    target = aws_iot_certificate.this.arn
}