import requests
import monitor_cpu
import monitor_memory
import monitor_disk

CLOUD_TRIGGER_URL = "https://your-cloud-function-url.com/scale-up"

def check_and_alert():
    cpu = monitor_cpu.check_cpu_usage()
    mem = monitor_memory.check_memory_usage()
    disk = monitor_disk.check_disk_usage()

    if cpu > 75 or mem > 75 or disk > 75:
        print("Threshold exceeded. Triggering auto-scaling...")
        requests.post(CLOUD_TRIGGER_URL, json={"status": "scale_up"})

if __name__ == "__main__":
    check_and_alert()
