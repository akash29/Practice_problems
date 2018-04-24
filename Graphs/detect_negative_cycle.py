from collections import defaultdict

#will use Bellman-Ford

class Graph:
    def __init__(self,num_vertices):
        self.vertices = num_vertices
        self.graph = defaultdict(dict)
        self.dist = defaultdict(dict)

    def Add_Edge(self,u,v,weight):
        self.graph[u][v] = weight
        if u not in self.graph:
            self.dist[u] = float('inf')
        elif v not in self.graph:
            self.dist[v] = float('inf')


    def Find_Neg_Cycle(self,start_vertex):

        self.dist[start_vertex] = 0
        for i in range(1,self.vertices-1):
            for u in self.graph:
                for v in self.graph[u]:
                    self.dist[v] = min(self.dist[v],float(self.dist[u]) + float(self.graph[u][v]))

        for u in self.graph:
            for v in self.graph[u]:
                temp = float(self.dist[u]) + float(self.graph[u][v])
                if self.dist[v] > temp:
                    return True

        return False





graph = Graph(5)
graph.Add_Edge('S','A',-1)
graph.Add_Edge('S','B',4)
graph.Add_Edge('A','B',3)
graph.Add_Edge('A','C',2)
graph.Add_Edge('A','D',2)
graph.Add_Edge('C','B',5)
graph.Add_Edge('C','A',1)
graph.Add_Edge('D','C',-3)

print(graph.Find_Neg_Cycle('S'))



