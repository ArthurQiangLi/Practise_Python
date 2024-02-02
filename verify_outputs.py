""" verify a1 output of 'gg' command by drawing a figure """
""" paste your data in verify_outputs.txt within the same folder with this file. """
import re
import pylab as pl
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

def parse_output_file(filename):
    with open(filename, 'r') as file:
        content = file.read()

    # Parsing vertices
    vertices_part = re.search(r'V = \{(.*?)\}', content, re.DOTALL).group(1)
    Vs = {}
    for line in vertices_part.split('\n'):
        match = re.search(r'(\w+):\s*\(([\d.]+),\s*([\d.]+)\)', line)
        if match:
            point, x, y = match.groups()
            Vs[point] = (float(x), float(y))

    # Parsing edges
    edges_part = re.search(r'E = \{(.*?)\}', content, re.DOTALL).group(1)
    Edges = set()
    for line in edges_part.split('\n'):
        match = re.search(r'<(\w+),(\w+)>', line)
        if match:
            p1, p2 = match.groups()
            Edges.add((p1, p2))

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