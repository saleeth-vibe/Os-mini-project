
import platform
import psutil
from datetime import datetime


# Get operating system information
os_name = platform.system()
os_version = platform.version()


# Get CPU information
cpu_cores = psutil.cpu_count(logical=True)


# Get RAM information
memory = psutil.virtual_memory()
total_ram = memory.total / (1024 ** 3)
available_ram = memory.available / (1024 ** 3)


# Get current system time
current_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")


# Display system information
print("\n========== SYSTEM INFORMATION ==========")


print("Operating System :", os_name)
print("OS Version       :", os_version)
print("CPU Cores        :", cpu_cores)
print("Total RAM        : {:.2f} GB".format(total_ram))
print("Available RAM    : {:.2f} GB".format(available_ram))
print("Current Time     :", current_time)


print("========================================")