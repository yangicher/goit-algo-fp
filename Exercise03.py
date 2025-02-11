import heapq

class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_edge(self, u, v, weight):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))
    
    def dijkstra(self, start):
        min_heap = [(0, start)]  
        distances = {vertex: float('inf') for vertex in self.graph}
        distances[start] = 0
        
        while min_heap:
            current_distance, current_vertex = heapq.heappop(min_heap)
            
            if current_distance > distances[current_vertex]:
                continue
            
            for neighbor, weight in self.graph[current_vertex]:
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(min_heap, (distance, neighbor))
        
        return distances

def main():
    g = Graph()
    g.add_edge('A', 'B', 10)
    g.add_edge('A', 'C', 3)
    g.add_edge('B', 'C', 7)
    g.add_edge('B', 'D', 1)
    g.add_edge('C', 'D', 8)

    for node in g.graph:
        print(f"Shortest distances from {node}:", g.dijkstra(node))

if __name__ == "__main__":
    main()
