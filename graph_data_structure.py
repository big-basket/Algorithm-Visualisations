from typing import Dict, Set, List, Tuple

class GraphDataStructure:
    def __init__(self, adjacency_list: Dict[int, Set[int]] = None):
        self.adjacency_list = adjacency_list if adjacency_list is not None else {}

    def add_vertex(self, vertex: int):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = set()

    def add_edge(self, u: int, v: int):
        self.add_vertex(u)
        self.add_vertex(v)
        self.adjacency_list[u].add(v)
        self.adjacency_list[v].add(u)

    def get_vertices(self) -> Set[int]:
        return set(self.adjacency_list.keys())

    def get_neighbors(self, vertex: int) -> Set[int]:
        return self.adjacency_list.get(vertex, set())

    def calculate_cut_size(self, set_a: Set[int]) -> int:
        cut_edges = 0
        for u in set_a:
            for v in self.adjacency_list.get(u, set()):
                if v not in set_a:
                    cut_edges += 1
        return cut_edges

    def get_edge_count(self) -> int:
        return sum(len(neighbors) for neighbors in self.adjacency_list.values()) // 2

    def display_graph(self) -> str:
        if len(self.adjacency_list) > 100:
            return f"Graph contains {len(self.adjacency_list)} vertices and {self.get_edge_count()} edges. Too large to display."
        return str(self.adjacency_list)

    def has_edge(self, u: int, v: int) -> bool:
        return v in self.adjacency_list.get(u, set())

    def get_edges(self) -> List[Tuple[int, int]]:
        """Returns a list of undirected edges as tuples (u, v)."""
        edges = set()
        for u in self.adjacency_list:
            for v in self.adjacency_list[u]:
                if (v, u) not in edges:
                    edges.add((u, v))
        return list(edges)
