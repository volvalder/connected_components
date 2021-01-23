class Graph:
    def __init__(self, pairs):
        self.adjList = {}
        for pair in pairs:
            self.addNode(pair[0])
            self.addNode(pair[1])
            self.addEdge(pair[0], pair[1])
        self.ids = [None] * len(self.adjList)
        self.count = 0
    def addNode(self, n):
        if n not in self.adjList:
            self.adjList[n] = []

    def addEdge(self, n, e):
        self.adjList[n].append(e)

    def dfs(self, v, visited):
        visited.append(v)
        self.ids[v] = self.count
        for neighbor in self.adjList[v]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)

    def cc(self):
        visited = []
        for v in self.adjList.keys():
            if v not in visited:
                self.dfs(v, visited)
                self.count+=1