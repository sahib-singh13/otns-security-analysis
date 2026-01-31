import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch

# --- CONFIGURATION ---
routers = ['Alice (Node 1)', 'Eve (Node 2)']
distances = [141, 141]  # Equidistant (Triangle)
weights = [64, 255]     # Alice = Default, Eve = Attack

# COLORS: Alice is Red (Weak), Eve is Green (Strong/Attack)
weight_colors = ['#FF9999', '#66B266']  # Light Red, Light Green

# Create Plot
fig, ax1 = plt.subplots(figsize=(10, 7))  # Increased height slightly for the legend

# Plot 1: Signal Cost (Distance) - Grey Bars
x = np.arange(len(routers))
width = 0.35
rects1 = ax1.bar(x - width/2, distances, width, label='Distance (Lower is Better)', color='lightgray')

# Plot 2: Leader Weight (The Attack Metric) - Colored Bars
ax2 = ax1.twinx()
rects2 = ax2.bar(x + width/2, weights, width, label='Leader Weight (Higher is Better)', color=weight_colors)

# Labels and Titles
ax1.set_ylabel('Distance to Victim (Units)', fontweight='bold', fontsize=12)
ax2.set_ylabel('Advertised Leader Weight (0-255)', fontweight='bold', fontsize=12)
ax1.set_title('Rogue Router Attack: Triangle Topology Analysis', fontsize=14, fontweight='bold', y=1.02)
ax1.set_xticks(x)
ax1.set_xticklabels(routers, fontsize=12)

# --- THE FIX: Moving the Legend Above the Graph ---
legend_elements = [
    Patch(facecolor='lightgray', label='Distance (Equal)'),
    Patch(facecolor='#FF9999', label='Alice Weight (64)'),
    Patch(facecolor='#66B266', label='Eve Weight (255 - ATTACK)')
]

# bbox_to_anchor=(0.5, 1.15) pushes it UP and OUT of the graph
ax1.legend(handles=legend_elements, loc='lower center', bbox_to_anchor=(0.5, 1.10), ncol=3, frameon=False, fontsize=10)

# Annotations (Adding numbers on top of bars)
def autolabel(rects, ax):
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha='center', va='bottom', fontweight='bold')

autolabel(rects1, ax1)
autolabel(rects2, ax2)

# Adjust layout to make room for the new legend position
plt.tight_layout()
plt.show()
