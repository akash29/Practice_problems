from collections import defaultdict

class Graph:
    def __init__(self,vertices):
        self.graph = defaultdict(list)
        self.vertices = vertices

    def add_Edge(self,u,v):
        self.graph[u].append(v)

    def dfs(self):
        visited = [False]*self.vertices
        top_sort_list = []
        for v in range(self.vertices):
            if not visited[v]:
                self.top_sort(v,top_sort_list,visited)

        return top_sort_list

    def top_sort(self,v,sort_list,visited):
        visited[v] = True

        for u in self.graph[v]:
            if not visited[u]:
                self.top_sort(u,sort_list,visited)

        sort_list.insert(0,v)


graph = Graph(6)
graph.add_Edge(5,2)
graph.add_Edge(2,3)
graph.add_Edge(3,1)
graph.add_Edge(5,0)
graph.add_Edge(4,0)
graph.add_Edge(4,1)
print(graph.dfs())
