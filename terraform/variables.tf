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