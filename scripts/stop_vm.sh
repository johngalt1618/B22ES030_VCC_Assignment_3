#!/bin/bash
echo "Stopping VM..."
terraform -chdir=deployment/terraform destroy -auto-approve
