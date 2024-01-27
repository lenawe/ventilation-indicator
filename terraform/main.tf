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
