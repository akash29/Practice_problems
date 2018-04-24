from collections import defaultdict

class Graph:
    def __init__(self,vertices):
       self.vertices = vertices
       self.graph = defaultdict(list)

    def Add_Edge(self,u,v):
        self.graph[u].append(v)

    def DFS(self):
        visited = [False]*self.vertices
        parent = [-1]*self.vertices
        result = False
        for u in range(self.vertices):
            if not visited[u]:
                result = self.Cycle_Check(u,visited,parent)
        return result

    def Cycle_Check(self,u,visited,parent):
        visited[u] = True

        for v in self.graph[u]:
            if not visited[v]:
                parent[v]=u
                if self.Cycle_Check(v,visited,parent):
                    return True
                else:
                    return False
            else:
                if parent[v]!=-1:
                    return True




graph = Graph(4)
graph.Add_Edge(0, 1)
graph.Add_Edge(0, 2)
graph.Add_Edge(1, 2)
graph.Add_Edge(2, 0)
graph.Add_Edge(2, 3)
graph.Add_Edge(3, 3)
print(graph.DFS())



