import psutil
import matplotlib.pyplot as plt
import os
import time

# Create outputs folder
output_folder = os.path.join(os.path.dirname(__file__), "outputs")
os.makedirs(output_folder, exist_ok=True)

# Lists to store data
time_values = []
cpu_values = []
memory_values = []
print("\n===== CPU AND MEMORY MONITORING =====")
print("Monitoring for 15 seconds...\n")

# Collect CPU and memory usage
for i in range(1, 16):

    cpu_usage = psutil.cpu_percent(interval=1)
    memory_usage = psutil.virtual_memory().percent

    time_values.append(i)
    cpu_values.append(cpu_usage)
    memory_values.append(memory_usage)

    print(
        f"Time: {i} sec | "
        f"CPU: {cpu_usage:.2f}% | "
        f"Memory: {memory_usage:.2f}%"
    )
print("\nMonitoring completed!")

# ---------------- CPU GRAPH ---------------

plt.figure(figsize=(9, 5))
plt.plot(time_values, cpu_values, marker='o')
plt.title("CPU Usage vs Time")
plt.xlabel("Time (Seconds)")
plt.ylabel("CPU Usage (%)")
plt.xticks(time_values)
plt.grid(True)

plt.savefig(os.path.join(output_folder, "cpu_graph.png"))
plt.close()
# ---------------- MEMORY GRAPH ----------------
plt.figure(figsize=(9, 5))
plt.plot(time_values, memory_values, marker='o')
plt.title("Memory Usage vs Time")
plt.xlabel("Time (Seconds)")
plt.ylabel("Memory Usage (%)")
plt.xticks(time_values)
plt.grid(True)
plt.savefig(os.path.join(output_folder, "memory_graph.png"))
plt.close()

print("\nBoth graphs saved successfully!")
print("Location:", output_folder)
print("1. cpu_graph.png")
print("2. memory_graph.png")