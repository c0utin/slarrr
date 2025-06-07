import matplotlib.pyplot as plt
import numpy as np
import os

# Simulate data for code generation metrics
time_intervals = np.arange(0, 60, 2)  # 60 minutes, data every 2 minutes
code_snippets = np.random.poisson(lam=2, size=len(time_intervals))  # Simulated number of snippets generated
generation_times = np.random.normal(loc=1.5, scale=0.5, size=len(time_intervals))  # Simulated generation times in seconds

# Plot 1: Code Generation Frequency over Time
plt.figure(figsize=(12, 7))
plt.plot(time_intervals, code_snippets, marker='o', color='#2ecc71', linewidth=2, markersize=8)
plt.title('Code Generation Frequency Over Time', fontsize=14, pad=20)
plt.xlabel('Time (minutes)', fontsize=12)
plt.ylabel('Number of Code Snippets', fontsize=12)
plt.grid(True, alpha=0.3)
plt.fill_between(time_intervals, code_snippets, alpha=0.2, color='#2ecc71')
plt.tight_layout()

# Save with high DPI
plt.savefig('grafana_dashboard.png', dpi=300, bbox_inches='tight')
plt.close()

# Plot 2: Code Generation Time Distribution
plt.figure(figsize=(12, 7))
plt.plot(time_intervals, generation_times, marker='s', color='#3498db', linewidth=2, markersize=8)
plt.title('Code Generation Time Over Time', fontsize=14, pad=20)
plt.xlabel('Time (minutes)', fontsize=12)
plt.ylabel('Generation Time (seconds)', fontsize=12)
plt.grid(True, alpha=0.3)
plt.fill_between(time_intervals, generation_times, alpha=0.2, color='#3498db')
plt.tight_layout()

# Save with high DPI
plt.savefig('metrics_graph.png', dpi=300, bbox_inches='tight')
plt.close()

print('Graphs generated and saved as grafana_dashboard.png and metrics_graph.png') 