import psutil
import platform
import re
from datetime import datetime

def format_bytes(bytes):
    """Convert bytes to human readable format"""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if bytes < 1024:
            return f"{bytes:.2f} {unit}"
        bytes /= 1024

def get_processor_name():
    """Get detailed processor information"""
    if platform.system() == "Windows":
        return platform.processor()
    elif platform.system() == "Darwin":  # macOS
        command = 'sysctl -n machdep.cpu.brand_string'
        return platform.processor()
    elif platform.system() == "Linux":
        with open('/proc/cpuinfo') as f:
            for line in f:
                if "model name" in line:
                    return re.sub(".*model name.*:", "", line, 1).strip()
    return platform.processor()

def get_network_usage():
    """Get current network usage statistics"""
    network = psutil.net_io_counters()
    return {
        'bytes_sent': format_bytes(network.bytes_sent),
        'bytes_recv': format_bytes(network.bytes_recv),
        'packets_sent': network.packets_sent,
        'packets_recv': network.packets_recv
    }

def get_system_info():
    """Get general system information"""
    return {
        'system': platform.system(),
        'release': platform.release(),
        'version': platform.version(),
        'machine': platform.machine(),
        'processor': get_processor_name()
    }