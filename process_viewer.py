import psutil
import time


processes = []


# Get running processes and initialize CPU measurement
for process in psutil.process_iter(['pid', 'name', 'memory_percent']):
    try:
        if process.info['pid'] == 0:
            continue


        process.cpu_percent(interval=None)
        processes.append(process)


    except (psutil.NoSuchProcess, psutil.AccessDenied):
        continue


# Wait for 1 second to measure CPU usage
time.sleep(1)


# Collect updated CPU and memory information
results = []


for process in processes:
    try:
        results.append({
            'pid': process.pid,
            'name': process.name(),
            'cpu': process.cpu_percent(interval=None),
            'memory': process.memory_percent()
        })


    except (psutil.NoSuchProcess, psutil.AccessDenied):
        continue


# Sort by CPU usage
results.sort(key=lambda x: x['cpu'], reverse=True)


# Display top 5 processes
print("\n========== TOP 5 RUNNING PROCESSES ==========\n")


print("{:<10} {:<25} {:<15} {:<15}".format(
    "PID", "PROCESS NAME", "CPU (%)", "MEMORY (%)"
))


print("-" * 65)


for p in results[:5]:
    print("{:<10} {:<25} {:<15.2f} {:<15.2f}".format(
        p['pid'], p['name'][:24], p['cpu'], p['memory']
    ))


print("\n==============================================")