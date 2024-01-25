# ventilation-indicator

# References
https://projects.raspberrypi.org/en/projects/build-your-own-weather-station/2
https://www.terraform-best-practices.com/examples
https://www.terraform-best-practices.com/examples/terraform/medium-size-infrastructure

# How-To

1. Install terraform following: https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli
2. Navigate to terraform folder:
   ```
   cd terraform
   ```
4. Initialize terraform in git bash:
   ```
   terraform init
   ```
6. Determine AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY and execute in git bash:
   ```
   export AWS_ACCESS_KEY_ID=kEyId
   export AWS_SECRET_ACCESS_KEY=aCeSsKeY
   ```
7. Check changes and apply them:
    ```
    terraform plan
    terraform apply
    ```