import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Create a figure and a set of subplots
fig, ax = plt.subplots(figsize=(6, 8))

# Define the segments
segments = [
    ("Stack (Top)\n(Growing Downwards)", 0.2, 'lightcoral'),
    ("Uninitialized Data (BSS)", 0.1, 'lightblue'),
    ("Initialized Data", 0.1, 'lightgreen'),
    ("Text Segment", 0.2, 'lightsalmon'),
    ("Heap\n(Growing Upwards)", 0.2, 'lightyellow'),
    ("Unused Memory Area", 0.2, 'lightgray')
]

# Add a rectangle for each segment
bottom = 0
for name, height, color in segments:
    rect = patches.Rectangle((0, bottom), 1, height, edgecolor='black', facecolor=color)
    ax.add_patch(rect)
    plt.text(0.5, bottom + height / 2, name, ha='center', va='center', fontsize=12)
    bottom += height

# Set the limits and labels
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

# Title
plt.title("Memory Layout in RAM")

# Show the plot
plt.show()
