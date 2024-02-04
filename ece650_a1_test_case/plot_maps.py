""" verify a1 output of 'gg' command by drawing a figure """
""" paste your data in verify_outputs.txt within the same folder with this file. """
""" Arthur 2024, Jan 1st: build """
""" Arthur 2024, Jan 2nd: add plot original streets function"""
import re
import pylab as pl
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import collections  as mc
from matplotlib.ticker import MultipleLocator

def parse_cmd_file(filename):
    lines = []
    coordinate_pattern = re.compile(r'\s*\(\s*(\-?\d+)\s*,\s*(\-?\d+)\s*\)\s*')

    with open(filename, 'r') as file:
        for line in file:
            if line.startswith("add"):
                # Find all coordinate pairs in the line
                coordinates = coordinate_pattern.findall(line)
                # Convert string coordinates to tuples of integers
                coordinates = [tuple(map(int, coord)) for coord in coordinates]
                lines.append(coordinates)
    
    return lines

def parse_output_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
    if(len(content) < 10):
        return [], []
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

##################################################################################
#[1] plot things in cmd.txt file
filename = 'cmd.txt'  # Path to your cmd.txt file
lines = parse_cmd_file(filename)
if(lines):
    c = np.array([(1, 0, 0, 1), (0, 1, 0, 1), (0, 0, 1, 1)])
    lc = mc.LineCollection(lines, colors='lightgreen', linewidths=5)
    fig, ax = pl.subplots()
    ax.add_collection(lc)
    ax.autoscale()
#[2] read outputs.txt and plot 
filename = 'verify_outputs.txt'
Vs, Edges = parse_output_file(filename)
print("Vs =", Vs)
print("Edges =", Edges)
len_vs = len(Vs)
len_edges = len(Edges)
if(Vs):
    x_values, y_values = zip(*Vs.values())# Extract x and y coordinates
    plt.scatter(x_values, y_values, c='red', s=150)# Plot the data points
    # Annotate each point with its label
    for label, (x, y) in Vs.items():
        plt.annotate(label, (x, y), textcoords="offset points", xytext=(5, 5), ha='center')
if(Edges):
    # Plot the edges
    for edge in Edges:
        start, end = edge
        start_x, start_y = Vs[start]
        end_x, end_y = Vs[end]
        plt.plot([start_x, end_x], [start_y, end_y], 'k-')

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title(f'Plot {len_vs} Vs, {len_edges} Edges', fontsize = 18)

# Show the plot
pl.axis('equal') # set the aspect ratio of the two axes to be equal
pl.gca().xaxis.set_major_locator(MultipleLocator(1)) #set custom major grid interval every 1 unit
pl.gca().yaxis.set_major_locator(MultipleLocator(1))
pl.grid(True, which='major', linestyle='--', linewidth=0.5, color='lightgray') # Show major grid lines
#plt.axis('equal')
plt.show()