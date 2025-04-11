import networkx as nx
import matplotlib.pyplot as plt
import random
from matplotlib.animation import FuncAnimation

# Create a graph
G = nx.erdos_renyi_graph(n=10, p=0.4)

# Initial random partition
partition = {node: random.choice([0, 1]) for node in G.nodes()}

# Function to compute current cut size
def cut_size(graph, part):
    return sum(
        1 for u, v in graph.edges()
        if part[u] != part[v]
    )

# Optimization step: flip a node's partition if it improves the cut
def local_search_step(graph, part):
    best_gain = 0
    best_node = None
    for node in graph.nodes():
        original = part[node]
        part[node] = 1 - original  # flip
        gain = cut_size(graph, part)
        part[node] = original  # flip back
        if gain > cut_size(graph, part):
            best_gain = gain
            best_node = node
    if best_node is not None:
        part[best_node] = 1 - part[best_node]

# Setup plot
pos = nx.spring_layout(G, seed=42)
fig, ax = plt.subplots()

def update(frame):
    ax.clear()
    local_search_step(G, partition)
    color_map = ['skyblue' if partition[node] == 0 else 'salmon' for node in G.nodes()]
    nx.draw(G, pos, ax=ax, with_labels=True, node_color=color_map, edge_color='gray')
    ax.set_title(f"Step {frame}, Cut size: {cut_size(G, partition)}")

ani = FuncAnimation(fig, update, frames=50, interval=500, repeat=False)
plt.show()
