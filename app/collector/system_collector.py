
import platform
import socket
import psutil
from datetime import datetime


def collect_system_info():

    memory = psutil.virtual_memory()
    disk = psutil.disk_usage("C:\\")

    system_data = {
        "hostname": socket.gethostname(),
        "operating_system": platform.system(),
        "os_version": platform.version(),
        "processor": platform.processor(),
        "cpu_usage_percent": psutil.cpu_percent(interval=1),
        "memory_total_gb": round(memory.total / (1024 ** 3), 2),
        "memory_used_percent": memory.percent,
        "disk_total_gb": round(disk.total / (1024 ** 3), 2),
        "disk_used_percent": disk.percent,
        "timestamp": datetime.now().isoformat()
    }

    return system_data
