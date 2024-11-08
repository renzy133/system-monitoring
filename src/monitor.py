import psutil
import time
from utils import format_bytes, get_processor_name
from alerts import check_thresholds
import psutil
import time
from datetime import datetime
from utils import format_bytes, get_processor_name, get_network_usage
from alerts import check_thresholds

class Colors:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'


def get_colored_value(value, warning=70, critical=85):
    if value >= critical:
        return f"{Colors.RED}{value:.1f}%{Colors.ENDC}"
    elif value >= warning:
        return f"{Colors.YELLOW}{value:.1f}%{Colors.ENDC}"
    return f"{Colors.GREEN}{value:.1f}%{Colors.ENDC}"


def monitor_cpu():
    cpu_percent = psutil.cpu_percent(interval=1)
    try:
        cpu_temp = psutil.sensors_temperatures()['coretemp'][0].current
        return cpu_percent, cpu_temp
    except:
        return cpu_percent, None


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
    print(f"{Colors.BLUE}System Monitor Started{Colors.ENDC}")
    print(f"CPU: {get_processor_name()}")

    try:
        while True:
            current_time = datetime.now().strftime('%H:%M:%S')
            cpu_percent, cpu_temp = monitor_cpu()
            memory_info = monitor_memory()
            disk_info = monitor_disk()
            network_info = get_network_usage()

            print("\n" + "=" * 50)
            print(f"Time: {current_time}")
            print(f"CPU Usage: {get_colored_value(cpu_percent)}")
            if cpu_temp:
                print(f"CPU Temperature: {cpu_temp}°C")
            print(f"Memory: {get_colored_value(memory_info['percent'])} ({memory_info['used']}/{memory_info['total']})")
            print(f"Disk: {get_colored_value(disk_info['percent'], 80, 90)} ({disk_info['used']}/{disk_info['total']})")
            print(f"Network: ↑ {network_info['bytes_sent']} | ↓ {network_info['bytes_recv']}")

            check_thresholds(cpu_percent, memory_info['percent'], disk_info['percent'])

            time.sleep(2)

    except KeyboardInterrupt:
        print(f"\n{Colors.BLUE}Monitoring stopped by user{Colors.ENDC}")


if __name__ == "__main__":
    main()