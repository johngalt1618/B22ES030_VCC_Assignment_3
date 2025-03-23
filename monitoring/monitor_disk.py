import psutil
import time

THRESHOLD = 75  # Percentage

def check_disk_usage():
    usage = psutil.disk_usage('/').percent
    return usage

if __name__ == "__main__":
    while True:
        disk_usage = check_disk_usage()
        print(f"Disk Usage: {disk_usage}%")
        if disk_usage > THRESHOLD:
            print("Warning: Disk usage exceeded threshold!")
        time.sleep(5)
