terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = "ap-south-1"
}

resource "aws_s3_bucket" "eks_artifacts" {
  bucket = "eks-gitops-artifacts-${data.aws_caller_identity.current.account_id}"

  tags = {
    Project     = "eks-gitops-platform"
    Environment = "dev"
    ManagedBy   = "terraform"
  }
}

resource "aws_s3_bucket_versioning" "eks_artifacts" {
  bucket = aws_s3_bucket.eks_artifacts.id
  versioning_configuration {
    status = "Enabled"
  }
}

data "aws_caller_identity" "current" {}

output "bucket_name" {
  value = aws_s3_bucket.eks_artifacts.bucket
}

output "bucket_arn" {
  value = aws_s3_bucket.eks_artifacts.arn
}