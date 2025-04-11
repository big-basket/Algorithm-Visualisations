import random
from graph_data_structure import GraphDataStructure

def generate_random_graph(num_vertices: int, num_edges: int) -> GraphDataStructure:
    graph = GraphDataStructure()

    for i in range(1, num_vertices):
        v = random.randint(0, i - 1)
        graph.add_edge(i, v)

    remaining_edges = num_edges - (num_vertices - 1)
    while remaining_edges > 0:
        u = random.randint(0, num_vertices - 1)
        v = random.randint(0, num_vertices - 1)
        if u != v and not graph.has_edge(u, v):
            graph.add_edge(u, v)
            remaining_edges -= 1

    return graph
