from typing import Set
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from graph_data_structure import GraphDataStructure

def solve(graph: GraphDataStructure, visualize: bool = True) -> Set[int]:
    best_set_a = set()
    max_cut_size = 0

    vertices = sorted(graph.get_vertices())
    n = len(vertices)
    total_subsets = 1 << n

    if n >= 20:
        print("Too many subsets for animation (n ≥ 20). Skipping visualization.")
        visualize = False

    print("-----------------Naive Solution----------------")
    print(f"Total Subsets to check: {total_subsets}")

    # Build graph
    G = nx.Graph()
    for u in graph.get_vertices():
        G.add_node(u)
    for u, v in graph.get_edges():
        G.add_edge(u, v)

    pos = nx.spring_layout(G, seed=42)

    if not visualize:
        # Just run without animation
        for mask in range(total_subsets):
            set_a = {vertices[i] for i in range(n) if (mask & (1 << i))}
            cut_size = graph.calculate_cut_size(set_a)
            if cut_size > max_cut_size:
                max_cut_size = cut_size
                best_set_a = set_a
        print(f"Final Max Cut Size: {max_cut_size}")
        return best_set_a

    # ---------- Animation Part ----------
    fig, ax = plt.subplots(figsize=(8, 6))

    # Shared mutable state
    state = {
        'iteration': 0,
        'max_cut': 0,
        'best_set_a': set(),
    }

    def update(frame):
        ax.clear()
        mask = frame
        set_a = {vertices[i] for i in range(n) if (mask & (1 << i))}
        cut_size = graph.calculate_cut_size(set_a)

        # Update max cut if needed
        if cut_size > state['max_cut']:
            state['max_cut'] = cut_size
            state['best_set_a'] = set_a

        node_colors = ['skyblue' if node in set_a else 'lightcoral' for node in G.nodes()]
        cut_edges = [(u, v) for u, v in G.edges() if (u in set_a) != (v in set_a)]

        nx.draw(G, pos, with_labels=True, node_color=node_colors, edge_color='gray', alpha=0.4, ax=ax)
        nx.draw_networkx_edges(G, pos, edgelist=cut_edges, edge_color='black', width=2, ax=ax)

        ax.set_title(f"Iter {frame+1}/{total_subsets} | Cut: {cut_size} | Max Cut: {state['max_cut']}")
        ax.axis('off')

    ani = FuncAnimation(
        fig,
        update,
        frames=total_subsets,
        interval=1,
        repeat=False
    )

    plt.show()

    return state['best_set_a']
