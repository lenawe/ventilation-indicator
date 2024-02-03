variable "thing_name" {
  description = "The name of the thing to create."
  type        = string
  default     = "thing"
}

variable "certificate_path" {
  description = "The path to the pem certificate to use."
  type        = string
}

variable "connection_id" {
    description = "The connection id of the thing to create."
    type        = string
}

variable "latitude" {
    description = "The latitude of the raspberry pi."
    type        = string
}

variable "longitude" {
    description = "The longitude of the raspberry pi."
    type        = string
}

variable "app_id" {
    description = "The app id for openweathermap api."
    type        = string
}

variable "aws_access_key" {
    description = "The access key for the AWS account."
    type        = string
    sensitive   = true
}

variable "aws_secret_access_key" {
    description = "The secret access key for the AWS account."
    type        = string
    sensitive   = true
}

variable "recipients" {
    description = "The email address to send the notification to."
    type        = list(string)
}

variable "sender" {
    description = "The email address to send the notification from."
    type        = string
}