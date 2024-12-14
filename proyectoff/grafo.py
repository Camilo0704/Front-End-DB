import heapq

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, from_node, to_node, weight):
        if from_node not in self.graph:
            self.graph[from_node] = {}
        self.graph[from_node][to_node] = weight

    def dijkstra(self, start, end):
        queue = [(0, start)]
        distances = {node: float('inf') for node in self.graph}
        distances[start] = 0
        shortest_path = {}

        while queue:
            current_distance, current_node = heapq.heappop(queue)

            if current_distance > distances[current_node]:
                continue

            for neighbor, weight in self.graph[current_node].items():
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(queue, (distance, neighbor))
                    shortest_path[neighbor] = current_node

        path, current_node = [], end
        while current_node in shortest_path:
            path.insert(0, current_node)
            current_node = shortest_path[current_node]
        if path:
            path.insert(0, start)
        return path, distances[end]
