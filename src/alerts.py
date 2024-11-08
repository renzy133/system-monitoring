import time
from datetime import datetime

THRESHOLDS = {
    'cpu': 80,
    'memory': 85,
    'disk': 90
}

last_alert = {
    'cpu': 0,
    'memory': 0,
    'disk': 0
}

ALERT_INTERVAL = 300  # 5 min cooldown between alerts

def log_alert(component, value):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    alert_message = f"[{timestamp}] WARNING: High {component} usage: {value}%"
    print(f"\033[91m{alert_message}\033[0m")
    
    with open('alerts.log', 'a') as f:
        f.write(alert_message + '\n')

def can_send_alert(component):
    current_time = time.time()
    if current_time - last_alert[component] > ALERT_INTERVAL:
        last_alert[component] = current_time
        return True
    return False

def check_thresholds(cpu_percent, memory_percent, disk_percent):
    if cpu_percent > THRESHOLDS['cpu'] and can_send_alert('cpu'):
        log_alert('CPU', cpu_percent)
    
    if memory_percent > THRESHOLDS['memory'] and can_send_alert('memory'):
        log_alert('Memory', memory_percent)
    
    if disk_percent > THRESHOLDS['disk'] and can_send_alert('disk'):
        log_alert('Disk', disk_percent)
