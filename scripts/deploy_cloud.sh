#!/bin/bash
echo "Deploying application to cloud..."
gcloud functions deploy scale_vm --runtime python39 --trigger-http --allow-unauthenticated
