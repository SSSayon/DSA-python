import heapq

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        self.vertices[vertex] = {}

    def add_edge(self, start_vertex, end_vertex, weight):
        self.vertices[start_vertex][end_vertex] = weight

    def get_neighbors(self, vertex):
        return self.vertices[vertex]

    def dijkstra(self, start_vertex):
        distances = {vertex: float('inf') for vertex in self.vertices}
        distances[start_vertex] = 0
        priority_queue = [(0, start_vertex)]
        visited = set()

        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)

            if current_distance > distances[current_vertex]:
                continue

            for neighbor, weight in self.get_neighbors(current_vertex).items():
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances


# Example usage:

# Create a graph
graph = Graph()

# Add vertices
graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")
graph.add_vertex("D")
graph.add_vertex("E")

# Add edges
graph.add_edge("A", "B", 4)
graph.add_edge("A", "C", 2)
graph.add_edge("B", "E", 3)
graph.add_edge("C", "D", 2)
graph.add_edge("D", "E", 3)
graph.add_edge("C", "B", 1)

# Find the shortest distances from vertex 'A' using Dijkstra's algorithm
distances = graph.dijkstra("A")

# Print the shortest distances
for vertex, distance in distances.items():
    print(f"Shortest distance from A to {vertex}: {distance}")
