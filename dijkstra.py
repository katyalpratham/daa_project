class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_node(self, node):
        if node not in self.adjacency_list:
            self.adjacency_list[node] = {}

    def add_edge(self, start, end, weight):
        self.adjacency_list[start][end] = weight
        self.adjacency_list[end][start] = weight  # Undirected graph

    def dijkstra(self, start):
        distances = {node: float('infinity') for node in self.adjacency_list}
        distances[start] = 0

        visited = set()
        nodes = list(self.adjacency_list.keys())

        while nodes:
            current_node = min(
                nodes,
                key=lambda node: distances[node] if node not in visited else float('infinity')
            )

            nodes.remove(current_node)
            visited.add(current_node)

            for neighbor, weight in self.adjacency_list[current_node].items():
                if neighbor not in visited:
                    new_distance = distances[current_node] + weight
                    if new_distance < distances[neighbor]:
                        distances[neighbor] = new_distance

        return distances