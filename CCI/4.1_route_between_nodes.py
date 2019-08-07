class graph:

    def __init__(self):
        self.adj_list = {}
        self.visited = {}
        self.parent = {}

    def add_edges(self,u,v):
        self.adj_list.setdefault(u,[]).append(v)
        self.visited[u] = False
        self.visited[v] = False

    def BFS(self,node1,node2):
        queue = []
        queue.append(node1)
        while len(queue) > 0 :
            node = queue.pop(0)
            self.visited[node]= True
            if node == node2:
                break
            if node in self.adj_list:
                edges = self.adj_list[node]
                for i in edges:
                    if i not in queue and i != node:
                        self.parent[i] = node
                        queue.append(i)
            else:
                break

        if not self.visited[node2]:
            return False
        else:
            return True

    def DFS(self,node1,node2):
        if not self.visited[node1]:
            return self.explore(node1,node2)

    def explore(self,node1,node2):
        self.visited[node1] = True
        if node1 == node2:
            return True
        if node1 in self.adj_list:
            edges = self.adj_list[node1]
            for i in edges:
                if i!=node1:
                    self.parent[i] = node1
                    return self.explore(i,node2)
                else:
                    continue
        else:
            return False

    def get_parent(self,node):
        if node in self.parent:
            parent = self.parent[node]
            print (parent,"<--",node)
            return self.get_parent(parent)


g = graph()
g.add_edges(0, 1)
g.add_edges(0, 2)
g.add_edges(1, 2)
g.add_edges(2, 4)
g.add_edges(2, 3)
g.add_edges(3, 3)
g.add_edges(3, 5)

#print (g.BFS(0,4))


print (g.DFS(0,4))
g.get_parent(4)