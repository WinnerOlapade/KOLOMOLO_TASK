variable "account_id" {
  # Pass Account ID value in as environmental variable. Set environment variable with [export TF_VAR_account_id="insert_value_here"]
  type = string
}

variable "main_region" {
  type    = string
  default = "us-east-1"
}