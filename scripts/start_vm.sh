#!/bin/bash
echo "Starting VM..."
terraform -chdir=deployment/terraform apply -auto-approve
