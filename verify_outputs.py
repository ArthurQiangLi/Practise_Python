""" verify a1 output of 'gg' command by drawing a figure """
""" paste your data in verify_outputs.txt within the same folder with this file. """
""" Arthur 2024, Jan 1st """
import re
import pylab as pl
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

def parse_output_file(filename):
    with open(filename, 'r') as file:
        content = file.read()

    # Extract vertices and edges blocks
    vertices_block = re.search(r"V = \{([\s\S]*?)\}", content).group(1)
    edges_block = re.search(r"E = \{([\s\S]*?)\}", content).group(1)

    # Parse vertices
    Vs = {}
    vertices_pattern = r"(\w+):\s*\((-?\d+\.?\d*),\s*(-?\d+\.?\d*)\)"
    for match in re.finditer(vertices_pattern, vertices_block):
        name, x, y = match.groups()
        Vs[name] = (float(x), float(y))

    # Parse edges
    Edges = set()
    edges_pattern = r"<(\w+),(\w+)>"
    for match in re.finditer(edges_pattern, edges_block):
        Edges.add(match.groups())

    return Vs, Edges

# Your file is named 'verify_outputs.txt'
filename = 'verify_outputs.txt'
Vs, Edges = parse_output_file(filename)

print("Vs =", Vs)
print("Edges =", Edges)


# Extract x and y coordinates
x_values, y_values = zip(*Vs.values())

# Plot the data points
plt.scatter(x_values, y_values)

# Annotate each point with its label
for label, (x, y) in Vs.items():
    plt.annotate(label, (x, y), textcoords="offset points", xytext=(5, 5), ha='center')

# Plot the edges
for edge in Edges:
    start, end = edge
    start_x, start_y = Vs[start]
    end_x, end_y = Vs[end]
    plt.plot([start_x, end_x], [start_y, end_y], 'k-')

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Data Points with Labeled Edges')

# Show the plot
pl.axis('equal') # set the aspect ratio of the two axes to be equal
pl.gca().xaxis.set_major_locator(MultipleLocator(1)) #set custom major grid interval every 1 unit
pl.gca().yaxis.set_major_locator(MultipleLocator(1))
pl.grid(True, which='major', linestyle='--', linewidth=0.5, color='lightgray') # Show major grid lines
plt.axis('equal')
plt.show()