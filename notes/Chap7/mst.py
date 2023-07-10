import heapq

class DisjointSet:
    def __init__(self, num_vertices):
        self.parent = list(range(num_vertices))  # Initialize each vertex as a separate set
        self.rank = [0] * num_vertices  # Maintain the rank of each set
    
    def find(self, x):
        if self.parent[x] != x:  # If x is not the representative of its set
            self.parent[x] = self.find(self.parent[x])  # Path compression: update x's parent to its representative
        return self.parent[x]  # Return the representative of x's set
    
    def union(self, x, y):
        x_root = self.find(x)  # Find the representative of x's set
        y_root = self.find(y)  # Find the representative of y's set
        
        if x_root == y_root:  # If both vertices belong to the same set (same representative)
            return
        
        if self.rank[x_root] < self.rank[y_root]:  # Attach the smaller rank tree to the larger rank tree
            self.parent[x_root] = y_root
        elif self.rank[x_root] > self.rank[y_root]:
            self.parent[y_root] = x_root
        else:  # If both trees have the same rank, attach one tree to the other and increment the rank
            self.parent[y_root] = x_root
            self.rank[x_root] += 1

class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_list = [[] for _ in range(num_vertices)]
    
    def add_edge(self, u, v, weight):
        self.adj_list[u].append((v, weight))
        self.adj_list[v].append((u, weight))
    
    def prim(self):
        mst = set()
        visited = [False] * self.num_vertices
        pq = []
        
        start_vertex = 0 
        visited[start_vertex] = True
        
        for edge in self.adj_list[start_vertex]:
            heapq.heappush(pq, (edge[1], start_vertex, edge[0]))
        
        while pq:
            weight, u, v = heapq.heappop(pq)
            
            if visited[v]:
                continue
            
            mst.add((u, v, weight))
            visited[v] = True
            
            for edge in self.adj_list[v]:
                heapq.heappush(pq, (edge[1], v, edge[0]))
        
        return mst
    
    def kruskal(self):
        mst = set()
        disjoint_set = DisjointSet(self.num_vertices)
        
        edges = []
        for u in range(self.num_vertices):
            for v, weight in self.adj_list[u]:
                edges.append((weight, u, v))
        
        edges.sort()
        
        for weight, u, v in edges:
            if disjoint_set.find(u) != disjoint_set.find(v):
                mst.add((u, v, weight))
                disjoint_set.union(u, v)
            
            if len(mst) == self.num_vertices - 1:
                break
        
        return mst


# Create a graph with 5 vertices
g = Graph(5)

# Add edges to the graph
g.add_edge(0, 1, 2)
g.add_edge(0, 3, 6)
g.add_edge(1, 2, 3)
g.add_edge(1, 3, 8)
g.add_edge(1, 4, 5)
g.add_edge(2, 4, 7)
g.add_edge(3, 4, 9)

# Test Prim's algorithm
prim_mst = g.prim()
print("Minimum Spanning Tree (Prim's algorithm):")
for u, v, weight in prim_mst:
    print(f"Edge: {u} - {v}, Weight: {weight}")
print()

# Test Kruskal's algorithm
kruskal_mst = g.kruskal()
print("Minimum Spanning Tree (Kruskal's algorithm):")
for u, v, weight in kruskal_mst:
    print(f"Edge: {u} - {v}, Weight: {weight}")
