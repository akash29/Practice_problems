from collections import defaultdict,deque

class Graph:
    def __init__(self,v):
        self.adjgraph = defaultdict(list)
        self.V = v
    def add_edge(self,src,dst):
        self.adjgraph[src].append(dst)

    def topological_sort(self):
        visited = [False]*self.V
        stack = deque()
        for i in range(self.V):
            if not visited[i]:
                self.visit(i,visited,stack)

        print( stack)

    def visit(self,vertex,visited_list,stack):
        visited_list[vertex] = True

        for node in self.adjgraph[vertex]:
            if not visited_list[node]:
               self.visit(node,visited_list,stack)

        stack.appendleft(vertex)


g= Graph(6)
g.add_edge(5, 2)
g.add_edge(5, 0)
g.add_edge(4, 0)
g.add_edge(4, 1)
g.add_edge(2, 3)
g.add_edge(3, 1)
g.topological_sort()