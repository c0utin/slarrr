import matplotlib.pyplot as plt
import numpy as np
import os

# Simulate data for code generation metrics
time_intervals = np.arange(0, 60, 2)  # 60 minutes, data every 2 minutes
code_snippets = np.random.poisson(lam=2, size=len(time_intervals))  # Simulated number of snippets generated
generation_times = np.random.normal(loc=1.5, scale=0.5, size=len(time_intervals))  # Simulated generation times in seconds

# Plot 1: Code Generation Frequency over Time
plt.figure(figsize=(10, 6))
plt.plot(time_intervals, code_snippets, marker='o', color='blue', label='Code Snippets')
plt.title('Code Generation Frequency Over Time')
plt.xlabel('Time (minutes)')
plt.ylabel('Number of Code Snippets')
plt.grid(True)
plt.legend()

# Ensure the directory exists
os.makedirs('../', exist_ok=True)

plt.savefig('../grafana_dashboard.png')
plt.close()

# Plot 2: Code Generation Time Distribution
plt.figure(figsize=(10, 6))
plt.plot(time_intervals, generation_times, marker='s', color='green', label='Generation Time')
plt.title('Code Generation Time Over Time')
plt.xlabel('Time (minutes)')
plt.ylabel('Generation Time (seconds)')
plt.grid(True)
plt.legend()

plt.savefig('../metrics_graph.png')
plt.close()

print('Graphs generated and saved as grafana_dashboard.png and metrics_graph.png') 