import psutil
import time

THRESHOLD = 75  # Percentage

def check_memory_usage():
    usage = psutil.virtual_memory().percent
    return usage

if __name__ == "__main__":
    while True:
        memory_usage = check_memory_usage()
        print(f"Memory Usage: {memory_usage}%")
        if memory_usage > THRESHOLD:
            print("Warning: Memory usage exceeded threshold!")
        time.sleep(5)
