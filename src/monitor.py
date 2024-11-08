import psutil
import time
from utils import format_bytes, get_processor_name
from alerts import check_thresholds

def monitor_cpu():
    return psutil.cpu_percent(interval=1)

def monitor_memory():
    memory = psutil.virtual_memory()
    return {
        'total': format_bytes(memory.total),
        'used': format_bytes(memory.used),
        'free': format_bytes(memory.free),
        'percent': memory.percent
    }

def monitor_disk():
    disk = psutil.disk_usage('/')
    return {
        'total': format_bytes(disk.total),
        'used': format_bytes(disk.used),
        'free': format_bytes(disk.free),
        'percent': disk.percent
    }

def main():
    print(f"System Monitor Started")
    print(f"CPU: {get_processor_name()}")
    
    try:
        while True:
            cpu_percent = monitor_cpu()
            memory_info = monitor_memory()
            disk_info = monitor_disk()

            print("\n" + "="*50)
            print(f"CPU Usage: {cpu_percent}%")
            print(f"Memory: {memory_info['percent']}% used")
            print(f"Disk: {disk_info['percent']}% used")

            check_thresholds(cpu_percent, memory_info['percent'], disk_info['percent'])
            
            time.sleep(2)
            
    except KeyboardInterrupt:
        print("\nMonitoring stopped by user")

if __name__ == "__main__":
    main()
