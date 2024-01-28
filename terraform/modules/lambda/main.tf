data "aws_iam_policy_document" "this" {
  statement {
    effect = "Allow"

    principals {
      type        = "Service"
      identifiers = ["lambda.amazonaws.com"]
    }

    actions = ["sts:AssumeRole"]
  }
}

resource "aws_iam_policy" "this" {
    name = "policy_${var.thing_name}"
    policy = jsonencode({
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": "sns:Publish",
                "Resource": "arn:aws:sns:*:*:*"
            },
            {
                "Effect": "Allow",
                "Action": "logs:CreateLogGroup",
                "Resource": "arn:aws:logs:eu-north-1:${var.connection_id}:*"
            },
            {
                "Effect": "Allow",
                "Action": [
                    "logs:CreateLogStream",
                    "logs:PutLogEvents"
                ],
                "Resource": [
                    "arn:aws:logs:eu-north-1:${var.connection_id}:log-group:/aws/lambda/*"
                ]
            },
            {
                "Effect": "Allow",
                "Action": [
                    "ses:SendEmail",
                    "ses:SendRawEmail"
                ],
                "Resource": "*"
            }
        ]
    })
}

resource "aws_iam_role" "this" {
    name               = "role_notification${var.thing_name}"
    assume_role_policy = data.aws_iam_policy_document.this.json
    managed_policy_arns = [ aws_iam_policy.this.arn ]
}

data "archive_file" "this" {
    type        = "zip"
    source_file = "./modules/lambda/lambda_function.py"
    output_path = "./modules/lambda/lambda_function.zip"
}
}