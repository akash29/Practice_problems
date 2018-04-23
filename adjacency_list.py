
class Graph:
    def __init__(self):
        self.edges = {}

    def add_vertices(self,vertice):
        self.edges[vertice] = {}

    def add_edge(self,u,v,cost):
        if u not in self.edges.keys():
            self.add_vertices(u)
        if v not in self.edges.keys():
            self.add_vertices(v)
        self.edges[u][v] = cost

    def print_graph(self, graph):
        for k,v in graph.items():
            if isinstance(v,dict):
                print("Head",k)
                print('-->')
                self.print_graph(v)
            else:
                print("Edge {0} and cost {1}".format(k,v))

    def get_graph(self):
        return self.edges



if __name__=="__main__":
    g = Graph()
    for i in range(1,6):
        g.add_vertices(i)
    # add the edges
    g.add_edge(1, 2, 1)
    g.add_edge(1, 4, 2)
    g.add_edge( 2, 3, 0)
    g.add_edge( 2, 4, 1)
    g.add_edge(2, 5, 3)
    g.add_edge(3, 4, 4)
    g.add_edge(3, 5, 5)
    g.add_edge(5, 1, 2)
    g.add_edge(4, 5, 1)
    g.add_edge(4, 2, 6)
    edges = g.get_graph()
    g.print_graph(edges)
