from google.cloud import compute_v1
import json

def scale_vm(request):
    client = compute_v1.InstancesClient()
    project = "your-gcp-project"
    zone = "us-central1-a"
    instance_template = "your-instance-template"

    instance = client.insert(project=project, zone=zone, instance_body={
        "name": "scaled-instance",
        "machineType": f"zones/{zone}/machineTypes/n1-standard-1",
        "sourceInstanceTemplate": instance_template
    })

    return json.dumps({"status": "Scaling triggered"}), 200
