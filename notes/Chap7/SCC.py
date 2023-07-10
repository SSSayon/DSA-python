# ---------- Tarjan's algorithm ----------
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for _ in range(vertices)]
        self.time = 0

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def tarjanDFS(self, v, low, disc, stack, inStack, result):
        disc[v] = self.time
        low[v] = self.time
        self.time += 1
        stack.append(v)
        inStack[v] = True

        for neighbor in self.graph[v]:
            if disc[neighbor] == -1:  # If neighbor is unvisited
                self.tarjanDFS(neighbor, low, disc, stack, inStack, result)
                low[v] = min(low[v], low[neighbor])
            elif inStack[neighbor]:  # If neighbor is in the current SCC
                low[v] = min(low[v], disc[neighbor])

        if low[v] == disc[v]:  # If v is the root of an SCC
            scc = []
            while True:
                node = stack.pop()
                inStack[node] = False
                scc.append(node)
                if node == v:
                    break
            result.append(scc)

    def tarjanSCC(self):
        disc = [-1] * self.V
        low = [-1] * self.V
        stack = []
        inStack = [False] * self.V
        result = []

        for v in range(self.V):
            if disc[v] == -1:
                self.tarjanDFS(v, low, disc, stack, inStack, result)

        return result

g = Graph(5)
g.addEdge(1, 0)
g.addEdge(0, 2)
g.addEdge(2, 1)
g.addEdge(0, 3)
g.addEdge(3, 4)

sccs = g.tarjanSCC()
for scc in sccs:
    print(scc)



# ---------- Kosaraju's algorithm ----------
from collections import defaultdict
class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, v, visited, stack):
        visited[v] = True
        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                self.dfs(neighbor, visited, stack)
        stack.append(v)

    def transposeGraph(self):
        transposed_graph = Graph(self.V)
        for v in self.graph:
            for neighbor in self.graph[v]:
                transposed_graph.addEdge(neighbor, v)
        return transposed_graph

    def dfsUtil(self, v, visited, result):
        visited[v] = True
        result.append(v)
        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                self.dfsUtil(neighbor, visited, result)

    def getStronglyConnectedComponents(self):
        visited = [False] * (self.V)
        stack = []
        for v in range(self.V):
            if not visited[v]:
                self.dfs(v, visited, stack)
        transposed_graph = self.transposeGraph()
        visited = [False] * (self.V)
        strongly_connected_components = []
        while stack:
            v = stack.pop()
            if not visited[v]:
                component = []
                transposed_graph.dfsUtil(v, visited, component)
                strongly_connected_components.append(component)
        return strongly_connected_components

g = Graph(5)
g.addEdge(0, 2)
g.addEdge(2, 1)
g.addEdge(1, 0)
g.addEdge(2, 3)
g.addEdge(3, 4)

sccs = g.getStronglyConnectedComponents()
for scc in sccs:
    print(scc)