# Telling Terraform to build inside AWS
terraform {
    required_providers {
        aws = {
          source = "hashicorp/aws"
          version = "~> 5.0"
        }
    }
}

provider "aws" {
    region = "eu-central-1" # Keeping data in frankfurt so German privacy laws are happy
}

# Step 1: Building the main perimeter fence for the Kiel bank network
resource "aws-vcp" "secure_vcp" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_hostnames = true
  enable_dns_support   = true

  tags = {
    Name         = "Kiel-Central-Bank-VPC"
    Environement = "Kiel-Finance_Prod"
    ManagedBy    = "Terraform"
    Location     = "Kiel-Schleswig-Holstein"
  }
}

# Step 2: Making a locked bank vault that has zero public access from the web
resource "aws_subnet" "private_subnet" {
    vpc_id            = aws_vpc.secure_vpc.id
    cidr_block        = "10.0.1.0/24"
    availability_zone = "eu-central-1a"

    tags = {
        Name = "Kiel-Bank-Vault-Subnet"
    }
}

# Step 3: Setting up the front-gate guard (The firewall)
resource "aws_security_group" "secure_web_sg" {
    name        = "kiel-bank-security-firewall"
    description = "Block all random traffic. Lock it down."
    vpc_id      = aws_vpc.secure_vpc.id

    # Inbound: Only let people in if they use secure HTTPS (Port 443)
    ingress {
        description = "Only safe web traffic allowed inside"
        from_port   = 443
        to_port     = 443
        protocol    = "tcp"
        cidr_blocks = ["0.0.0.0/0"]
    }
  
    # Outbound: Only let servers talk to the outside web to download updates
    egress {
        description = "Only let servers go out for software updates"
        from_port   = 443
        to_port     = 443
        protocol    = "tcp"
        cidr_blocks = ["0.0.0.0/0"]
    }

    tags = {
        Name = "Kiel-Bank-Firewall-Active"
    }
}