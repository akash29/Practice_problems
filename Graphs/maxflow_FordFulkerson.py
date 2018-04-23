
class Graph:
    def __init__(self,graph):
        self.graph = graph
        self.vertices = len(graph)

    def find_max_flow(self,s,t):
        visited = [False]*self.vertices
        parents = [-1]*self.vertices
        max_flow = 0
        while self.BFS(s,t,parents,visited):
            temp_flow = float('inf')
            sink = t
            while sink!=s and sink!=-1:
                parent = parents[sink]
                temp_flow = min(temp_flow,self.graph[parent][sink])
                sink = parent
            max_flow+=temp_flow

            if not temp_flow>0:
                break
            sink = t
            while sink!=s and sink!=-1:
                parent = parents[sink]
                self.graph[parent][sink]-=temp_flow
                self.graph[sink][parent]+=temp_flow
                sink = parent

            visited = [False] * self.vertices
            parents = [-1] * self.vertices

        return max_flow,parents

    def BFS(self,s,t,parents,visited):
        visited[s] = True
        queue = []
        queue.append(s)
        while queue:
            source = queue.pop(0)
            for u,j in enumerate(self.graph[source]):
                if not visited[u]:
                    if j >0:
                        queue.append(u)
                        parents[u] = source
                        visited[u] = True

        if visited[t]!=-1:
            return True
        else:
            return False




graph = [[0, 16, 13, 0, 0, 0],
        [0, 0, 10, 12, 0, 0],
        [0, 4, 0, 0, 14, 0],
        [0, 0, 9, 0, 0, 20],
        [0, 0, 0, 7, 0, 4],
        [0, 0, 0, 0, 0, 0]]
graph = Graph(graph)
max_flow,parents = graph.find_max_flow(0,5)
print (max_flow)
print(parents)


