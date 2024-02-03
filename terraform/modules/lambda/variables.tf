variable "thing_name" {
  description = "The name of the thing to create."
  type        = string
  default     = "thing"
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