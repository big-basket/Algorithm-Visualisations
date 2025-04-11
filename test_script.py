from random_graph_generator import generate_random_graph
from naive_solution import solve

def main():
    num_vertices = 19
    num_edges = 60

    print(f"Generating random graph with {num_vertices} vertices and {num_edges} edges...")
    graph = generate_random_graph(num_vertices, num_edges)
    
    print("\nGraph structure:")
    print(graph.display_graph())
    
    print("\nRunning naive max-cut solution...")
    solve(graph)
    
if __name__ == "__main__":
    main()
