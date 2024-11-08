import psutil
import platform

def format_bytes(bytes):
    """Convert bytes to human readable format"""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if bytes < 1024:
            return f"{bytes:.2f} {unit}"
        bytes /= 1024

def get_processor_name():
    """Get the processor name"""
    if platform.system() == "Windows":
        return platform.processor()
    elif platform.system() == "Darwin":
        return platform.processor()
    elif platform.system() == "Linux":
        command = "cat /proc/cpuinfo"
        return platform.processor()
    return "Unknown processor"

def get_network_usage():
    """Get network usage statistics"""
    network = psutil.net_io_counters()
    return {
        'bytes_sent': format_bytes(network.bytes_sent),
        'bytes_recv': format_bytes(network.bytes_recv)
    }
