variable "region" {
  description = "AWS region to deploy resources"
  type        = string
  default     = "eu-west-3"
}

variable "project_name" {
  description = "Project name used in tags and naming"
  type        = string
  default     = "mini-projet-mlops"
}

variable "environment" {
  description = "Deployment environment"
  type        = string
  default     = "dev"
}

variable "bucket_name" {
  description = "Unique S3 bucket name for Terraform state"
  type        = string
}

variable "dynamodb_table_name" {
  description = "DynamoDB table name used for Terraform state locking"
  type        = string
  default     = "tf-lock-mini-projet-mlops"
}
