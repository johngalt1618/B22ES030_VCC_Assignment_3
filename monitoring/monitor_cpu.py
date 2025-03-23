import psutil
import time

THRESHOLD = 75  # Percentage

def check_cpu_usage():
    usage = psutil.cpu_percent(interval=1)
    return usage

if __name__ == "__main__":
    while True:
        cpu_usage = check_cpu_usage()
        print(f"CPU Usage: {cpu_usage}%")
        if cpu_usage > THRESHOLD:
            print("Warning: CPU usage exceeded threshold!")
        time.sleep(5)
